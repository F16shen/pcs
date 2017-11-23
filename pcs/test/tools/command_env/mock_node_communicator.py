from __future__ import (
    absolute_import,
    division,
    print_function,
)

try:
    # python 2
    from urlparse import parse_qs
except ImportError:
    # python 3
    from urllib.parse import parse_qs

from pcs.common import pcs_pycurl as pycurl
from pcs.common.node_communicator import(
    RequestTarget,
    RequestData,
    Request,
    Response,
)
from pcs.test.tools.custom_mock import MockCurlSimple

CALL_TYPE_HTTP_ADD_REQUESTS = "CALL_TYPE_HTTP_ADD_REQUESTS"
CALL_TYPE_HTTP_START_LOOP = "CALL_TYPE_HTTP_START_LOOP"

def log_request(request):
    label_data = [
            ("action", request.action),
            ("label", request.target.label),
            ("data", parse_qs(request.data)),
        ]

    if request.target.address_list != [request.target.label]:
        label_data.append(("addres_list", request.target.address_list))

    if request.target.port != "2224":
        label_data.append(("port", request.target.port))


    return "  ".join([
        "{0}:'{1}'".format(key, value) for key, value in label_data
    ])

def log_response(response, indent=0):
    label_data = [
        ("action", response.request.action),
        ("label", response.request.target.label),
    ]

    if response.request.target.address_list != [response.request.target.label]:
        label_data.append(("addres_list", response.request.target.address_list))

    label_data.append(("was_connected", response.was_connected))

    if response.request.target.port != "2224":
        label_data.append(("port", response.request.target.port))

    if response.was_connected:
        label_data.append(("respose_code", response.response_code))
    else:
        label_data.extend([
            ("errno", response.errno),
            ("error_msg", response.error_msg),
        ])

    label_data.append(("data", parse_qs(response.request.data)))

    return "{0}{1}".format(
        "  "*indent,
        "  ".join([
            "{0}:'{1}'".format(key, value) for key, value in label_data
        ]),
    )

def different_request_lists(expected_request_list, request_list):
    return AssertionError(
        (
            "Method add_request of NodeCommunicator expected"
            " request_list:\n  * {0}\nbut got: \n  * {1}"
        )
        .format(
            "\n  * ".join(log_request(r) for r in expected_request_list),
            "\n  * ".join(log_request(r) for r in request_list),
        )
    )

def bad_request_list_content(errors):
    return AssertionError(
        "Method add_request of NodeCommunicator get different requests"
        " than expected (key: (expected, real)): \n  {0}".format(
            "\n  ".join([
                "{0}:\n    {1}".format(
                    index,
                    "\n    ".join([
                        "{0}:\n      {1}\n      {2}"
                        .format(key, pair[0], pair[1])
                        for key, pair in value.items()
                    ])
                )
                for index, value in errors.items()
            ]),
        )
    )

def _communication_to_response(
    label, address_list, action, param_list, port, token, response_code,
    output, debug_output, was_connected, errno, error_msg
):
    return Response(
        MockCurlSimple(
            info={pycurl.RESPONSE_CODE: response_code},
            output=output.encode("utf-8"),
            debug_output=debug_output.encode("utf-8"),
            request=Request(
                RequestTarget(label, address_list, port, token),
                RequestData(action, param_list),
            )
        ),
        was_connected=was_connected,
        errno=6,
        error_msg=error_msg,
    )


def create_communication(
    communication_list, action="", param_list=None, port=None, token=None,
    response_code=None, output="", debug_output="", was_connected=True,
    errno=0, error_msg_template=None
):
    """
    list of dict communication_list -- is setting for one request - response
        it accepts keys:
            label -- required, see RequestTarget
            action -- pcsd url, see RequestData
            param_list -- list of pairs, see RequestData
            port -- see RequestTarget
            token=None -- see RequestTarget
            response_code -- http response code
            output -- http response output
            debug_output -- pycurl debug output
            was_connected -- see Response
            errno -- see Response
            error_msg -- see Response
        if some key is not present, it is put here from common values - rest
        args of this fuction(except name, communication_list,
        error_msg_template)
    string error_msg_template -- template, the keys for format function will
        be taken from appropriate item of communication_list
    string action -- pcsd url, see RequestData
    list of pairs (tuple) param_list -- see RequestData
    string port -- see RequestTarget
    string token=None -- see RequestTarget
    string response_code -- http response code
    string output -- http response output
    string debug_output -- pycurl debug output
    bool was_connected -- see Response
    int errno -- see Response
    string error_msg -- see Response
    """
    response_list = []

    common = dict(
        action=action,
        param_list=param_list if param_list else [],
        port=port,
        token=token,
        response_code=response_code,
        output=output,
        debug_output=debug_output,
        was_connected=was_connected,
        errno=errno,
    )
    for communication in communication_list:
        if "address_list" not in communication:
            communication["address_list"] = [communication["label"]]

        full = common.copy()
        full.update(communication)

        if "error_msg" not in full:
            full["error_msg"] = (
                "" if not error_msg_template
                else error_msg_template.format(**full)
            )


        response_list.append(
            _communication_to_response(**full)
        )

    request_list = [response.request for response in response_list]

    return request_list, response_list


class AddRequestCall(object):
    type = CALL_TYPE_HTTP_ADD_REQUESTS

    def __init__(self, request_list):
        self.request_list = request_list

    def format(self):
        return "Requests:\n    * {0}".format(
            "\n    * ".join([
                log_request(request) for request in self.request_list
            ])
        )

    def __repr__(self):
        return str("<HttpAddRequest '{0}'>").format(self.request_list)

class StartLoopCall(object):
    type = CALL_TYPE_HTTP_START_LOOP

    def format(self):
        return "Responses:\n    * {0}".format(
            "\n    * ".join([
                log_response(response) for response in self.response_list
            ])
        )

    def __init__(self, response_list):
        self.response_list = response_list

    def __repr__(self):
        return str("<HttpStartLoop '{0}'>").format(self.response_list)

class NodeCommunicator(object):
    def __init__(self, call_queue=None):
        self.__call_queue = call_queue

    def add_requests(self, request_list):
        _, add_request_call = self.__call_queue.take(
            CALL_TYPE_HTTP_ADD_REQUESTS,
            request_list,
        )

        expected_request_list = add_request_call.request_list

        if len(expected_request_list) != len(request_list):
            raise different_request_lists(expected_request_list, request_list)

        errors = {}
        for i, real_request in enumerate(request_list):
            expected_request = add_request_call.request_list[i]

            diff = {}
            if expected_request.action != real_request.action:
                diff["action"] = (
                    expected_request.action,
                    real_request.action
                )

            if expected_request.target.label != real_request.target.label:
                diff["target.label"] = (
                    expected_request.target.label,
                    real_request.target.label
                )

            if expected_request.target.token != real_request.target.token:
                diff["target.token"] = (
                    expected_request.target.token,
                    real_request.target.token
                )

            if expected_request.target.port != real_request.target.port:
                diff["target.port"] = (
                    expected_request.target.port,
                    real_request.target.port
                )

            if expected_request.data != real_request.data:
                diff["data"] = (
                    parse_qs(expected_request.data),
                    parse_qs(real_request.data)
                )

            if diff:
                errors[i] = diff

        if errors:
            raise self.__call_queue.error_with_context(
                bad_request_list_content(errors)
            )


    def start_loop(self):
        _, call = self.__call_queue.take(CALL_TYPE_HTTP_START_LOOP)
        return call.response_list

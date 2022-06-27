# pylint: disable=wildcard-import, unused-wildcard-import
# Wildcard import of deprecated report codes will prevent creation of a new
# report with the code of deprecated report
from .deprecated_codes import *
from .types import ForceCode as F
from .types import MessageCode as M

# force categories
FORCE = F("FORCE")
SKIP_OFFLINE_NODES = F("SKIP_OFFLINE_NODES")


# messages


ADD_REMOVE_ITEMS_NOT_SPECIFIED = M("ADD_REMOVE_ITEMS_NOT_SPECIFIED")
ADD_REMOVE_ITEMS_DUPLICATION = M("ADD_REMOVE_ITEMS_DUPLICATION")
ADD_REMOVE_CANNOT_ADD_ITEMS_ALREADY_IN_THE_CONTAINER = M(
    "ADD_REMOVE_CANNOT_ADD_ITEMS_ALREADY_IN_THE_CONTAINER"
)
ADD_REMOVE_CANNOT_REMOVE_ITEMS_NOT_IN_THE_CONTAINER = M(
    "ADD_REMOVE_CANNOT_REMOVE_ITEMS_NOT_IN_THE_CONTAINER"
)
ADD_REMOVE_CANNOT_ADD_AND_REMOVE_ITEMS_AT_THE_SAME_TIME = M(
    "ADD_REMOVE_CANNOT_ADD_AND_REMOVE_ITEMS_AT_THE_SAME_TIME"
)
ADD_REMOVE_CANNOT_REMOVE_ALL_ITEMS_FROM_THE_CONTAINER = M(
    "ADD_REMOVE_CANNOT_REMOVE_ALL_ITEMS_FROM_THE_CONTAINER"
)
ADD_REMOVE_ADJACENT_ITEM_NOT_IN_THE_CONTAINER = M(
    "ADD_REMOVE_ADJACENT_ITEM_NOT_IN_THE_CONTAINER"
)
ADD_REMOVE_CANNOT_PUT_ITEM_NEXT_TO_ITSELF = M(
    "ADD_REMOVE_CANNOT_PUT_ITEM_NEXT_TO_ITSELF"
)
ADD_REMOVE_CANNOT_SPECIFY_ADJACENT_ITEM_WITHOUT_ITEMS_TO_ADD = M(
    "ADD_REMOVE_CANNOT_SPECIFY_ADJACENT_ITEM_WITHOUT_ITEMS_TO_ADD"
)
AGENT_GENERIC_ERROR = M("AGENT_GENERIC_ERROR")
AGENT_IMPLEMENTS_UNSUPPORTED_OCF_VERSION = M(
    "AGENT_IMPLEMENTS_UNSUPPORTED_OCF_VERSION"
)
AGENT_NAME_GUESS_FOUND_MORE_THAN_ONE = M("AGENT_NAME_GUESS_FOUND_MORE_THAN_ONE")
AGENT_NAME_GUESS_FOUND_NONE = M("AGENT_NAME_GUESS_FOUND_NONE")
AGENT_NAME_GUESSED = M("AGENT_NAME_GUESSED")
BAD_CLUSTER_STATE_FORMAT = M("BAD_CLUSTER_STATE_FORMAT")
BOOTH_ADDRESS_DUPLICATION = M("BOOTH_ADDRESS_DUPLICATION")
BOOTH_ALREADY_IN_CIB = M("BOOTH_ALREADY_IN_CIB")
BOOTH_CANNOT_DETERMINE_LOCAL_SITE_IP = M("BOOTH_CANNOT_DETERMINE_LOCAL_SITE_IP")
BOOTH_CONFIG_ACCEPTED_BY_NODE = M("BOOTH_CONFIG_ACCEPTED_BY_NODE")
BOOTH_CONFIG_DISTRIBUTION_NODE_ERROR = M("BOOTH_CONFIG_DISTRIBUTION_NODE_ERROR")
BOOTH_CONFIG_DISTRIBUTION_STARTED = M("BOOTH_CONFIG_DISTRIBUTION_STARTED")
BOOTH_CONFIG_IS_USED = M("BOOTH_CONFIG_IS_USED")
BOOTH_CONFIG_UNEXPECTED_LINES = M("BOOTH_CONFIG_UNEXPECTED_LINES")
BOOTH_DAEMON_STATUS_ERROR = M("BOOTH_DAEMON_STATUS_ERROR")
BOOTH_EVEN_PEERS_NUM = M("BOOTH_EVEN_PEERS_NUM")
BOOTH_FETCHING_CONFIG_FROM_NODE = M("BOOTH_FETCHING_CONFIG_FROM_NODE")
BOOTH_INVALID_NAME = M("BOOTH_INVALID_NAME")
BOOTH_LACK_OF_SITES = M("BOOTH_LACK_OF_SITES")
BOOTH_MULTIPLE_TIMES_IN_CIB = M("BOOTH_MULTIPLE_TIMES_IN_CIB")
BOOTH_NOT_EXISTS_IN_CIB = M("BOOTH_NOT_EXISTS_IN_CIB")
BOOTH_PATH_NOT_EXISTS = M("BOOTH_PATH_NOT_EXISTS")
BOOTH_PEERS_STATUS_ERROR = M("BOOTH_PEERS_STATUS_ERROR")
BOOTH_TICKET_DOES_NOT_EXIST = M("BOOTH_TICKET_DOES_NOT_EXIST")
BOOTH_TICKET_DUPLICATE = M("BOOTH_TICKET_DUPLICATE")
BOOTH_TICKET_NAME_INVALID = M("BOOTH_TICKET_NAME_INVALID")
BOOTH_TICKET_OPERATION_FAILED = M("BOOTH_TICKET_OPERATION_FAILED")
BOOTH_TICKET_STATUS_ERROR = M("BOOTH_TICKET_STATUS_ERROR")
BOOTH_UNSUPPORTED_FILE_LOCATION = M("BOOTH_UNSUPPORTED_FILE_LOCATION")
CANNOT_BAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = M(
    "CANNOT_BAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
)
CANNOT_BAN_RESOURCE_STOPPED_NO_NODE_SPECIFIED = M(
    "CANNOT_BAN_RESOURCE_STOPPED_NO_NODE_SPECIFIED"
)
CANNOT_GROUP_RESOURCE_WRONG_TYPE = M("CANNOT_GROUP_RESOURCE_WRONG_TYPE")
CANNOT_LEAVE_GROUP_EMPTY_AFTER_MOVE = M("CANNOT_LEAVE_GROUP_EMPTY_AFTER_MOVE")
CANNOT_MOVE_RESOURCE_BUNDLE = M("CANNOT_MOVE_RESOURCE_BUNDLE")
CANNOT_MOVE_RESOURCE_CLONE = M("CANNOT_MOVE_RESOURCE_CLONE")
CANNOT_MOVE_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = M(
    "CANNOT_MOVE_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
)
CANNOT_MOVE_RESOURCE_PROMOTABLE_INNER = M(
    "CANNOT_MOVE_RESOURCE_PROMOTABLE_INNER"
)
CANNOT_MOVE_RESOURCE_NOT_RUNNING = M("CANNOT_MOVE_RESOURCE_NOT_RUNNING")
CANNOT_MOVE_RESOURCE_STOPPED_NO_NODE_SPECIFIED = M(
    "CANNOT_MOVE_RESOURCE_STOPPED_NO_NODE_SPECIFIED"
)
CANNOT_REMOVE_ALL_CLUSTER_NODES = M("CANNOT_REMOVE_ALL_CLUSTER_NODES")
CANNOT_SET_ORDER_CONSTRAINTS_FOR_RESOURCES_IN_THE_SAME_GROUP = M(
    "CANNOT_SET_ORDER_CONSTRAINTS_FOR_RESOURCES_IN_THE_SAME_GROUP"
)
CANNOT_UNMOVE_UNBAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = M(
    "CANNOT_UNMOVE_UNBAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
)
CIB_ACL_ROLE_IS_ALREADY_ASSIGNED_TO_TARGET = M(
    "CIB_ACL_ROLE_IS_ALREADY_ASSIGNED_TO_TARGET"
)
CIB_ACL_ROLE_IS_NOT_ASSIGNED_TO_TARGET = M(
    "CIB_ACL_ROLE_IS_NOT_ASSIGNED_TO_TARGET"
)
CIB_ACL_TARGET_ALREADY_EXISTS = M("CIB_ACL_TARGET_ALREADY_EXISTS")
CIB_ALERT_RECIPIENT_ALREADY_EXISTS = M("CIB_ALERT_RECIPIENT_ALREADY_EXISTS")
CIB_ALERT_RECIPIENT_VALUE_INVALID = M("CIB_ALERT_RECIPIENT_VALUE_INVALID")
CIB_CANNOT_FIND_MANDATORY_SECTION = M("CIB_CANNOT_FIND_MANDATORY_SECTION")
CIB_DIFF_ERROR = M("CIB_DIFF_ERROR")
CIB_FENCING_LEVEL_ALREADY_EXISTS = M("CIB_FENCING_LEVEL_ALREADY_EXISTS")
CIB_FENCING_LEVEL_DOES_NOT_EXIST = M("CIB_FENCING_LEVEL_DOES_NOT_EXIST")
CIB_LOAD_ERROR_BAD_FORMAT = M("CIB_LOAD_ERROR_BAD_FORMAT")
CIB_LOAD_ERROR = M("CIB_LOAD_ERROR")
CIB_LOAD_ERROR_GET_NODES_FOR_VALIDATION = M(
    "CIB_LOAD_ERROR_GET_NODES_FOR_VALIDATION"
)
CIB_NVSET_AMBIGUOUS_PROVIDE_NVSET_ID = M("CIB_NVSET_AMBIGUOUS_PROVIDE_NVSET_ID")
CIB_LOAD_ERROR_SCOPE_MISSING = M("CIB_LOAD_ERROR_SCOPE_MISSING")
CIB_PUSH_ERROR = M("CIB_PUSH_ERROR")
CIB_SAVE_TMP_ERROR = M("CIB_SAVE_TMP_ERROR")
CIB_SIMULATE_ERROR = M("CIB_SIMULATE_ERROR")
CIB_UPGRADE_FAILED = M("CIB_UPGRADE_FAILED")
CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION = M(
    "CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION"
)
CIB_UPGRADE_SUCCESSFUL = M("CIB_UPGRADE_SUCCESSFUL")
CLUSTER_DESTROY_STARTED = M("CLUSTER_DESTROY_STARTED")
CLUSTER_DESTROY_SUCCESS = M("CLUSTER_DESTROY_SUCCESS")
CLUSTER_ENABLE_STARTED = M("CLUSTER_ENABLE_STARTED")
CLUSTER_ENABLE_SUCCESS = M("CLUSTER_ENABLE_SUCCESS")
CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES = M(
    "CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES"
)
CLUSTER_SETUP_SUCCESS = M("CLUSTER_SETUP_SUCCESS")
CLUSTER_START_STARTED = M("CLUSTER_START_STARTED")
CLUSTER_START_SUCCESS = M("CLUSTER_START_SUCCESS")
CLUSTER_UUID_ALREADY_SET = M("CLUSTER_UUID_ALREADY_SET")
CLUSTER_WILL_BE_DESTROYED = M("CLUSTER_WILL_BE_DESTROYED")
COMMAND_INVALID_PAYLOAD = M("COMMAND_INVALID_PAYLOAD")
COMMAND_UNKNOWN = M("COMMAND_UNKNOWN")
LIVE_ENVIRONMENT_NOT_CONSISTENT = M("LIVE_ENVIRONMENT_NOT_CONSISTENT")
LIVE_ENVIRONMENT_REQUIRED = M("LIVE_ENVIRONMENT_REQUIRED")
LIVE_ENVIRONMENT_REQUIRED_FOR_LOCAL_NODE = M(
    "LIVE_ENVIRONMENT_REQUIRED_FOR_LOCAL_NODE"
)
RESOURCE_STONITH_COMMANDS_MISMATCH = M("RESOURCE_STONITH_COMMANDS_MISMATCH")
COROSYNC_ADDRESS_IP_VERSION_WRONG_FOR_LINK = M(
    "COROSYNC_ADDRESS_IP_VERSION_WRONG_FOR_LINK"
)
COROSYNC_AUTHKEY_WRONG_LENGTH = M("COROSYNC_AUTHKEY_WRONG_LENGTH")
COROSYNC_BAD_NODE_ADDRESSES_COUNT = M("COROSYNC_BAD_NODE_ADDRESSES_COUNT")
COROSYNC_CLUSTER_NAME_INVALID_FOR_GFS2 = M(
    "COROSYNC_CLUSTER_NAME_INVALID_FOR_GFS2"
)
COROSYNC_CONFIG_ACCEPTED_BY_NODE = M("COROSYNC_CONFIG_ACCEPTED_BY_NODE")
COROSYNC_CONFIG_CANNOT_SAVE_INVALID_NAMES_VALUES = M(
    "COROSYNC_CONFIG_CANNOT_SAVE_INVALID_NAMES_VALUES"
)
COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR = M(
    "COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR"
)
COROSYNC_CONFIG_DISTRIBUTION_STARTED = M("COROSYNC_CONFIG_DISTRIBUTION_STARTED")
COROSYNC_CONFIG_MISSING_NAMES_OF_NODES = M(
    "COROSYNC_CONFIG_MISSING_NAMES_OF_NODES"
)
COROSYNC_CONFIG_NO_NODES_DEFINED = M("COROSYNC_CONFIG_NO_NODES_DEFINED")
COROSYNC_CONFIG_RELOADED = M("COROSYNC_CONFIG_RELOADED")
COROSYNC_CONFIG_RELOAD_ERROR = M("COROSYNC_CONFIG_RELOAD_ERROR")
COROSYNC_CONFIG_RELOAD_NOT_POSSIBLE = M("COROSYNC_CONFIG_RELOAD_NOT_POSSIBLE")
COROSYNC_CONFIG_UNSUPPORTED_TRANSPORT = M(
    "COROSYNC_CONFIG_UNSUPPORTED_TRANSPORT"
)
COROSYNC_IP_VERSION_MISMATCH_IN_LINKS = M(
    "COROSYNC_IP_VERSION_MISMATCH_IN_LINKS"
)
COROSYNC_CANNOT_ADD_REMOVE_LINKS_BAD_TRANSPORT = M(
    "COROSYNC_CANNOT_ADD_REMOVE_LINKS_BAD_TRANSPORT"
)
COROSYNC_CANNOT_ADD_REMOVE_LINKS_NO_LINKS_SPECIFIED = M(
    "COROSYNC_CANNOT_ADD_REMOVE_LINKS_NO_LINKS_SPECIFIED"
)
COROSYNC_CANNOT_ADD_REMOVE_LINKS_TOO_MANY_FEW_LINKS = M(
    "COROSYNC_CANNOT_ADD_REMOVE_LINKS_TOO_MANY_FEW_LINKS"
)
COROSYNC_LINK_ALREADY_EXISTS_CANNOT_ADD = M(
    "COROSYNC_LINK_ALREADY_EXISTS_CANNOT_ADD"
)
COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_REMOVE = M(
    "COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_REMOVE"
)
COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_UPDATE = M(
    "COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_UPDATE"
)
COROSYNC_LINK_NUMBER_DUPLICATION = M("COROSYNC_LINK_NUMBER_DUPLICATION")
COROSYNC_NODE_ADDRESS_COUNT_MISMATCH = M("COROSYNC_NODE_ADDRESS_COUNT_MISMATCH")
COROSYNC_NODE_CONFLICT_CHECK_SKIPPED = M("COROSYNC_NODE_CONFLICT_CHECK_SKIPPED")
COROSYNC_NODES_MISSING = M("COROSYNC_NODES_MISSING")
COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR = M(
    "COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR"
)
COROSYNC_NOT_RUNNING_CHECK_STARTED = M("COROSYNC_NOT_RUNNING_CHECK_STARTED")
COROSYNC_NOT_RUNNING_ON_NODE = M("COROSYNC_NOT_RUNNING_ON_NODE")
COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE = M(
    "COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE"
)
COROSYNC_QUORUM_ATB_CANNOT_BE_DISABLED_DUE_TO_SBD = M(
    "COROSYNC_QUORUM_ATB_CANNOT_BE_DISABLED_DUE_TO_SBD"
)
COROSYNC_QUORUM_ATB_WILL_BE_ENABLED_DUE_TO_SBD = M(
    "COROSYNC_QUORUM_ATB_WILL_BE_ENABLED_DUE_TO_SBD"
)
COROSYNC_QUORUM_GET_STATUS_ERROR = M("COROSYNC_QUORUM_GET_STATUS_ERROR")
COROSYNC_QUORUM_HEURISTICS_ENABLED_WITH_NO_EXEC = M(
    "COROSYNC_QUORUM_HEURISTICS_ENABLED_WITH_NO_EXEC"
)
COROSYNC_QUORUM_LOSS_UNABLE_TO_CHECK = M("COROSYNC_QUORUM_LOSS_UNABLE_TO_CHECK")
COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR = M(
    "COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR"
)
COROSYNC_QUORUM_WILL_BE_LOST = M("COROSYNC_QUORUM_WILL_BE_LOST")
COROSYNC_RUNNING_ON_NODE = M("COROSYNC_RUNNING_ON_NODE")
COROSYNC_TOO_MANY_LINKS_OPTIONS = M("COROSYNC_TOO_MANY_LINKS_OPTIONS")
COROSYNC_TRANSPORT_UNSUPPORTED_OPTIONS = M(
    "COROSYNC_TRANSPORT_UNSUPPORTED_OPTIONS"
)
CRM_MON_ERROR = M("CRM_MON_ERROR")
DEFAULTS_CAN_BE_OVERRIDDEN = M("DEFAULTS_CAN_BE_OVERRIDDEN")
DEPRECATED_OPTION = M("DEPRECATED_OPTION")
DEPRECATED_OPTION_VALUE = M("DEPRECATED_OPTION_VALUE")
DR_CONFIG_ALREADY_EXIST = M("DR_CONFIG_ALREADY_EXIST")
DR_CONFIG_DOES_NOT_EXIST = M("DR_CONFIG_DOES_NOT_EXIST")
DUPLICATE_CONSTRAINTS_EXIST = M("DUPLICATE_CONSTRAINTS_EXIST")
DUPLICATE_CONSTRAINTS_LIST = M("DUPLICATE_CONSTRAINTS_LIST")
EMPTY_RESOURCE_SET_LIST = M("EMPTY_RESOURCE_SET_LIST")
FENCE_HISTORY_COMMAND_ERROR = M("FENCE_HISTORY_COMMAND_ERROR")
FENCE_HISTORY_NOT_SUPPORTED = M("FENCE_HISTORY_NOT_SUPPORTED")
FILES_DISTRIBUTION_SKIPPED = M("FILES_DISTRIBUTION_SKIPPED")
FILES_DISTRIBUTION_STARTED = M("FILES_DISTRIBUTION_STARTED")
FILES_REMOVE_FROM_NODES_STARTED = M("FILES_REMOVE_FROM_NODES_STARTED")
FILES_REMOVE_FROM_NODES_SKIPPED = M("FILES_REMOVE_FROM_NODES_SKIPPED")
FILE_ALREADY_EXISTS = M("FILE_ALREADY_EXISTS")
FILE_DISTRIBUTION_ERROR = M("FILE_DISTRIBUTION_ERROR")
FILE_DISTRIBUTION_SUCCESS = M("FILE_DISTRIBUTION_SUCCESS")
FILE_IO_ERROR = M("FILE_IO_ERROR")
FILE_REMOVE_FROM_NODE_ERROR = M("FILE_REMOVE_FROM_NODE_ERROR")
FILE_REMOVE_FROM_NODE_SUCCESS = M("FILE_REMOVE_FROM_NODE_SUCCESS")
HOST_NOT_FOUND = M("HOST_NOT_FOUND")
HOST_ALREADY_AUTHORIZED = M("HOST_ALREADY_AUTHORIZED")
HOST_ALREADY_IN_CLUSTER_CONFIG = M("HOST_ALREADY_IN_CLUSTER_CONFIG")
HOST_ALREADY_IN_CLUSTER_SERVICES = M("HOST_ALREADY_IN_CLUSTER_SERVICES")
ID_ALREADY_EXISTS = M("ID_ALREADY_EXISTS")
ID_BELONGS_TO_UNEXPECTED_TYPE = M("ID_BELONGS_TO_UNEXPECTED_TYPE")
ID_NOT_FOUND = M("ID_NOT_FOUND")
INVALID_CIB_CONTENT = M("INVALID_CIB_CONTENT")
INVALID_ID_BAD_CHAR = M("INVALID_ID_BAD_CHAR")
INVALID_ID_IS_EMPTY = M("INVALID_ID_IS_EMPTY")
INVALID_OPTIONS = M("INVALID_OPTIONS")
INVALID_USERDEFINED_OPTIONS = M("INVALID_USERDEFINED_OPTIONS")
INVALID_OPTION_TYPE = M("INVALID_OPTION_TYPE")
INVALID_OPTION_VALUE = M("INVALID_OPTION_VALUE")
INVALID_RESOURCE_AGENT_NAME = M("INVALID_RESOURCE_AGENT_NAME")
INVALID_RESPONSE_FORMAT = M("INVALID_RESPONSE_FORMAT")
INVALID_SCORE = M("INVALID_SCORE")
INVALID_STONITH_AGENT_NAME = M("INVALID_STONITH_AGENT_NAME")
INVALID_TIMEOUT_VALUE = M("INVALID_TIMEOUT_VALUE")
MULTIPLE_RESULTS_FOUND = M("MULTIPLE_RESULTS_FOUND")
MUTUALLY_EXCLUSIVE_OPTIONS = M("MUTUALLY_EXCLUSIVE_OPTIONS")
NO_ACTION_NECESSARY = M("NO_ACTION_NECESSARY")
NODE_ADDRESSES_ALREADY_EXIST = M("NODE_ADDRESSES_ALREADY_EXIST")
NODE_ADDRESSES_CANNOT_BE_EMPTY = M("NODE_ADDRESSES_CANNOT_BE_EMPTY")
NODE_ADDRESSES_DUPLICATION = M("NODE_ADDRESSES_DUPLICATION")
NODE_ADDRESSES_UNRESOLVABLE = M("NODE_ADDRESSES_UNRESOLVABLE")
NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL = M(
    "NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL"
)
NODE_COMMUNICATION_DEBUG_INFO = M("NODE_COMMUNICATION_DEBUG_INFO")
NODE_COMMUNICATION_ERROR = M("NODE_COMMUNICATION_ERROR")
NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED = M(
    "NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED"
)
NODE_COMMUNICATION_ERROR_PERMISSION_DENIED = M(
    "NODE_COMMUNICATION_ERROR_PERMISSION_DENIED"
)
NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT = M(
    "NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT"
)
NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND = M(
    "NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND"
)
NODE_COMMUNICATION_ERROR_TIMED_OUT = M("NODE_COMMUNICATION_ERROR_TIMED_OUT")
NODE_COMMUNICATION_FINISHED = M("NODE_COMMUNICATION_FINISHED")
NODE_COMMUNICATION_NOT_CONNECTED = M("NODE_COMMUNICATION_NOT_CONNECTED")
NODE_COMMUNICATION_NO_MORE_ADDRESSES = M("NODE_COMMUNICATION_NO_MORE_ADDRESSES")
NODE_COMMUNICATION_PROXY_IS_SET = M("NODE_COMMUNICATION_PROXY_IS_SET")
NODE_COMMUNICATION_RETRYING = M("NODE_COMMUNICATION_RETRYING")
NODE_COMMUNICATION_STARTED = M("NODE_COMMUNICATION_STARTED")
NODE_NAMES_ALREADY_EXIST = M("NODE_NAMES_ALREADY_EXIST")
NODE_NAMES_DUPLICATION = M("NODE_NAMES_DUPLICATION")
NODE_NOT_FOUND = M("NODE_NOT_FOUND")
NODE_REMOVE_IN_PACEMAKER_FAILED = M("NODE_REMOVE_IN_PACEMAKER_FAILED")
NONE_HOST_FOUND = M("NONE_HOST_FOUND")
NODE_USED_AS_TIE_BREAKER = M("NODE_USED_AS_TIE_BREAKER")
NODES_TO_REMOVE_UNREACHABLE = M("NODES_TO_REMOVE_UNREACHABLE")
NODE_TO_CLEAR_IS_STILL_IN_CLUSTER = M("NODE_TO_CLEAR_IS_STILL_IN_CLUSTER")
NODE_IN_LOCAL_CLUSTER = M("NODE_IN_LOCAL_CLUSTER")
NOT_AUTHORIZED = M("NOT_AUTHORIZED")
OMITTING_NODE = M("OMITTING_NODE")
OBJECT_WITH_ID_IN_UNEXPECTED_CONTEXT = M("OBJECT_WITH_ID_IN_UNEXPECTED_CONTEXT")
PACEMAKER_SIMULATION_RESULT = M("PACEMAKER_SIMULATION_RESULT")
PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND = M("PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND")
PARSE_ERROR_COROSYNC_CONF = M("PARSE_ERROR_COROSYNC_CONF")
PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_AFTER_OPENING_BRACE = M(
    "PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_AFTER_OPENING_BRACE"
)
PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_BEFORE_OR_AFTER_CLOSING_BRACE = M(
    "PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_BEFORE_OR_AFTER_CLOSING_BRACE"
)
PARSE_ERROR_COROSYNC_CONF_LINE_IS_NOT_SECTION_NOR_KEY_VALUE = M(
    "PARSE_ERROR_COROSYNC_CONF_LINE_IS_NOT_SECTION_NOR_KEY_VALUE"
)
PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE = M(
    "PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE"
)
PARSE_ERROR_COROSYNC_CONF_MISSING_SECTION_NAME_BEFORE_OPENING_BRACE = M(
    "PARSE_ERROR_COROSYNC_CONF_MISSING_SECTION_NAME_BEFORE_OPENING_BRACE"
)
PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE = M(
    "PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE"
)
PARSE_ERROR_JSON_FILE = M("PARSE_ERROR_JSON_FILE")
PCSD_VERSION_TOO_OLD = M("PCSD_VERSION_TOO_OLD")
PCSD_SSL_CERT_AND_KEY_DISTRIBUTION_STARTED = M(
    "PCSD_SSL_CERT_AND_KEY_DISTRIBUTION_STARTED"
)
PCSD_SSL_CERT_AND_KEY_SET_SUCCESS = M("PCSD_SSL_CERT_AND_KEY_SET_SUCCESS")
PREREQUISITE_OPTION_MUST_BE_ENABLED_AS_WELL = M(
    "PREREQUISITE_OPTION_MUST_BE_ENABLED_AS_WELL"
)
PREREQUISITE_OPTION_MUST_BE_DISABLED = M("PREREQUISITE_OPTION_MUST_BE_DISABLED")
PREREQUISITE_OPTION_MUST_NOT_BE_SET = M("PREREQUISITE_OPTION_MUST_NOT_BE_SET")
PREREQUISITE_OPTION_IS_MISSING = M("PREREQUISITE_OPTION_IS_MISSING")
QDEVICE_ALREADY_DEFINED = M("QDEVICE_ALREADY_DEFINED")
QDEVICE_ALREADY_INITIALIZED = M("QDEVICE_ALREADY_INITIALIZED")
QDEVICE_CERTIFICATE_ACCEPTED_BY_NODE = M("QDEVICE_CERTIFICATE_ACCEPTED_BY_NODE")
QDEVICE_CERTIFICATE_DISTRIBUTION_STARTED = M(
    "QDEVICE_CERTIFICATE_DISTRIBUTION_STARTED"
)
QDEVICE_CERTIFICATE_REMOVAL_STARTED = M("QDEVICE_CERTIFICATE_REMOVAL_STARTED")
QDEVICE_CERTIFICATE_REMOVED_FROM_NODE = M(
    "QDEVICE_CERTIFICATE_REMOVED_FROM_NODE"
)
QDEVICE_CERTIFICATE_IMPORT_ERROR = M("QDEVICE_CERTIFICATE_IMPORT_ERROR")
QDEVICE_CERTIFICATE_SIGN_ERROR = M("QDEVICE_CERTIFICATE_SIGN_ERROR")
QDEVICE_DESTROY_ERROR = M("QDEVICE_DESTROY_ERROR")
QDEVICE_DESTROY_SUCCESS = M("QDEVICE_DESTROY_SUCCESS")
QDEVICE_GET_STATUS_ERROR = M("QDEVICE_GET_STATUS_ERROR")
QDEVICE_INITIALIZATION_ERROR = M("QDEVICE_INITIALIZATION_ERROR")
QDEVICE_INITIALIZATION_SUCCESS = M("QDEVICE_INITIALIZATION_SUCCESS")
QDEVICE_NOT_DEFINED = M("QDEVICE_NOT_DEFINED")
QDEVICE_NOT_INITIALIZED = M("QDEVICE_NOT_INITIALIZED")
QDEVICE_NOT_RUNNING = M("QDEVICE_NOT_RUNNING")
QDEVICE_CLIENT_RELOAD_STARTED = M("QDEVICE_CLIENT_RELOAD_STARTED")
QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED = M(
    "QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED"
)
QDEVICE_USED_BY_CLUSTERS = M("QDEVICE_USED_BY_CLUSTERS")
CLONING_STONITH_RESOURCES_HAS_NO_EFFECT = M(
    "CLONING_STONITH_RESOURCES_HAS_NO_EFFECT"
)
REQUIRED_OPTIONS_ARE_MISSING = M("REQUIRED_OPTIONS_ARE_MISSING")
REQUIRED_OPTION_OF_ALTERNATIVES_IS_MISSING = M(
    "REQUIRED_OPTION_OF_ALTERNATIVES_IS_MISSING"
)
RESOURCE_BAN_PCMK_ERROR = M("RESOURCE_BAN_PCMK_ERROR")
RESOURCE_BAN_PCMK_SUCCESS = M("RESOURCE_BAN_PCMK_SUCCESS")
RESOURCE_BUNDLE_ALREADY_CONTAINS_A_RESOURCE = M(
    "RESOURCE_BUNDLE_ALREADY_CONTAINS_A_RESOURCE"
)
RESOURCE_BUNDLE_UNSUPPORTED_CONTAINER_TYPE = M(
    "RESOURCE_BUNDLE_UNSUPPORTED_CONTAINER_TYPE"
)
RESOURCE_CLEANUP_ERROR = M("RESOURCE_CLEANUP_ERROR")
RESOURCE_DOES_NOT_RUN = M("RESOURCE_DOES_NOT_RUN")
RESOURCE_DISABLE_AFFECTS_OTHER_RESOURCES = M(
    "RESOURCE_DISABLE_AFFECTS_OTHER_RESOURCES"
)
RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE = M(
    "RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE"
)
RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE = M("RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE")
RESOURCE_INSTANCE_ATTR_VALUE_NOT_UNIQUE = M(
    "RESOURCE_INSTANCE_ATTR_VALUE_NOT_UNIQUE"
)
RESOURCE_INSTANCE_ATTR_GROUP_VALUE_NOT_UNIQUE = M(
    "RESOURCE_INSTANCE_ATTR_GROUP_VALUE_NOT_UNIQUE"
)
RESOURCE_IS_GUEST_NODE_ALREADY = M("RESOURCE_IS_GUEST_NODE_ALREADY")
RESOURCE_IS_UNMANAGED = M("RESOURCE_IS_UNMANAGED")
RESOURCE_MANAGED_NO_MONITOR_ENABLED = M("RESOURCE_MANAGED_NO_MONITOR_ENABLED")
RESOURCE_MOVE_PCMK_ERROR = M("RESOURCE_MOVE_PCMK_ERROR")
RESOURCE_MOVE_PCMK_SUCCESS = M("RESOURCE_MOVE_PCMK_SUCCESS")
RESOURCE_OPERATION_INTERVAL_ADAPTED = M("RESOURCE_OPERATION_INTERVAL_ADAPTED")
RESOURCE_OPERATION_INTERVAL_DUPLICATION = M(
    "RESOURCE_OPERATION_INTERVAL_DUPLICATION"
)
RESOURCE_REFRESH_ERROR = M("RESOURCE_REFRESH_ERROR")
RESOURCE_REFRESH_TOO_TIME_CONSUMING = M("RESOURCE_REFRESH_TOO_TIME_CONSUMING")
RESOURCE_RUNNING_ON_NODES = M("RESOURCE_RUNNING_ON_NODES")
RESOURCE_UNMOVE_UNBAN_PCMK_ERROR = M("RESOURCE_UNMOVE_UNBAN_PCMK_ERROR")
RESOURCE_UNMOVE_UNBAN_PCMK_SUCCESS = M("RESOURCE_UNMOVE_UNBAN_PCMK_SUCCESS")
RESOURCE_UNMOVE_UNBAN_PCMK_EXPIRED_NOT_SUPPORTED = M(
    "RESOURCE_UNMOVE_UNBAN_PCMK_EXPIRED_NOT_SUPPORTED"
)
RESOURCE_MAY_OR_MAY_NOT_MOVE = M("RESOURCE_MAY_OR_MAY_NOT_MOVE")
RESOURCE_MOVE_CONSTRAINT_CREATED = M("RESOURCE_MOVE_CONSTRAINT_CREATED")
RESOURCE_MOVE_CONSTRAINT_REMOVED = M("RESOURCE_MOVE_CONSTRAINT_REMOVED")
RESOURCE_MOVE_NOT_AFFECTING_RESOURCE = M("RESOURCE_MOVE_NOT_AFFECTING_RESOURCE")
RESOURCE_MOVE_AFFECTS_OTRHER_RESOURCES = M(
    "RESOURCE_MOVE_AFFECTS_OTRHER_RESOURCES"
)
RESOURCE_MOVE_AUTOCLEAN_SIMULATION_FAILURE = M(
    "RESOURCE_MOVE_AUTOCLEAN_SIMULATION_FAILURE"
)
RULE_IN_EFFECT_STATUS_DETECTION_NOT_SUPPORTED = M(
    "RULE_IN_EFFECT_STATUS_DETECTION_NOT_SUPPORTED"
)
RULE_EXPRESSION_NOT_ALLOWED = M("RULE_EXPRESSION_NOT_ALLOWED")
RULE_EXPRESSION_OPTIONS_DUPLICATION = M("RULE_EXPRESSION_OPTIONS_DUPLICATION")
RULE_EXPRESSION_PARSE_ERROR = M("RULE_EXPRESSION_PARSE_ERROR")
RULE_EXPRESSION_SINCE_GREATER_THAN_UNTIL = M(
    "RULE_EXPRESSION_SINCE_GREATER_THAN_UNTIL"
)
RUN_EXTERNAL_PROCESS_ERROR = M("RUN_EXTERNAL_PROCESS_ERROR")
RUN_EXTERNAL_PROCESS_FINISHED = M("RUN_EXTERNAL_PROCESS_FINISHED")
RUN_EXTERNAL_PROCESS_STARTED = M("RUN_EXTERNAL_PROCESS_STARTED")
SBD_CHECK_STARTED = M("SBD_CHECK_STARTED")
SBD_CHECK_SUCCESS = M("SBD_CHECK_SUCCESS")
SBD_CONFIG_ACCEPTED_BY_NODE = M("SBD_CONFIG_ACCEPTED_BY_NODE")
SBD_CONFIG_DISTRIBUTION_STARTED = M("SBD_CONFIG_DISTRIBUTION_STARTED")
SBD_DEVICE_DOES_NOT_EXIST = M("SBD_DEVICE_DOES_NOT_EXIST")
SBD_DEVICE_DUMP_ERROR = M("SBD_DEVICE_DUMP_ERROR")
SBD_DEVICE_INITIALIZATION_ERROR = M("SBD_DEVICE_INITIALIZATION_ERROR")
SBD_DEVICE_INITIALIZATION_STARTED = M("SBD_DEVICE_INITIALIZATION_STARTED")
SBD_DEVICE_INITIALIZATION_SUCCESS = M("SBD_DEVICE_INITIALIZATION_SUCCESS")
SBD_DEVICE_IS_NOT_BLOCK_DEVICE = M("SBD_DEVICE_IS_NOT_BLOCK_DEVICE")
SBD_DEVICE_LIST_ERROR = M("SBD_DEVICE_LIST_ERROR")
SBD_DEVICE_MESSAGE_ERROR = M("SBD_DEVICE_MESSAGE_ERROR")
SBD_DEVICE_PATH_NOT_ABSOLUTE = M("SBD_DEVICE_PATH_NOT_ABSOLUTE")
SBD_LIST_WATCHDOG_ERROR = M("SBD_LIST_WATCHDOG_ERROR")
SBD_NO_DEVICE_FOR_NODE = M("SBD_NO_DEVICE_FOR_NODE")
SBD_NOT_USED_CANNOT_SET_SBD_OPTIONS = M("SBD_NOT_USED_CANNOT_SET_SBD_OPTIONS")
SBD_TOO_MANY_DEVICES_FOR_NODE = M("SBD_TOO_MANY_DEVICES_FOR_NODE")
SBD_WITH_DEVICES_NOT_USED_CANNOT_SET_DEVICE = M(
    "SBD_WITH_DEVICES_NOT_USED_CANNOT_SET_DEVICE"
)
SBD_WATCHDOG_NOT_SUPPORTED = M("SBD_WATCHDOG_NOT_SUPPORTED")
SBD_WATCHDOG_VALIDATION_INACTIVE = M("SBD_WATCHDOG_VALIDATION_INACTIVE")
SBD_WATCHDOG_TEST_ERROR = M("SBD_WATCHDOG_TEST_ERROR")
SBD_WATCHDOG_TEST_MULTIPLE_DEVICES = M("SBD_WATCHDOG_TEST_MULTIPLE_DEVICES")
SBD_WATCHDOG_TEST_FAILED = M("SBD_WATCHDOG_TEST_FAILED")
SERVICE_ACTION_STARTED = M("SERVICE_ACTION_STARTED")
SERVICE_ACTION_FAILED = M("SERVICE_ACTION_FAILED")
SERVICE_ACTION_SUCCEEDED = M("SERVICE_ACTION_SUCCEEDED")
SERVICE_ACTION_SKIPPED = M("SERVICE_ACTION_SKIPPED")
SERVICE_NOT_INSTALLED = M("SERVICE_NOT_INSTALLED")
SERVICE_VERSION_MISMATCH = M("SERVICE_VERSION_MISMATCH")
UNABLE_TO_GET_RESOURCE_OPERATION_DIGESTS = M(
    "UNABLE_TO_GET_RESOURCE_OPERATION_DIGESTS"
)
STONITH_WATCHDOG_TIMEOUT_CANNOT_BE_SET = M(
    "STONITH_WATCHDOG_TIMEOUT_CANNOT_BE_SET"
)
STONITH_WATCHDOG_TIMEOUT_CANNOT_BE_UNSET = M(
    "STONITH_WATCHDOG_TIMEOUT_CANNOT_BE_UNSET"
)
STONITH_WATCHDOG_TIMEOUT_TOO_SMALL = M("STONITH_WATCHDOG_TIMEOUT_TOO_SMALL")
STONITH_RESOURCES_DO_NOT_EXIST = M("STONITH_RESOURCES_DO_NOT_EXIST")
STONITH_RESTARTLESS_UPDATE_MISSING_MPATH_KEYS = M(
    "STONITH_RESTARTLESS_UPDATE_MISSING_MPATH_KEYS"
)
STONITH_RESTARTLESS_UPDATE_OF_SCSI_DEVICES_NOT_SUPPORTED = M(
    "STONITH_RESTARTLESS_UPDATE_OF_SCSI_DEVICES_NOT_SUPPORTED"
)
STONITH_RESTARTLESS_UPDATE_UNSUPPORTED_AGENT = M(
    "STONITH_RESTARTLESS_UPDATE_UNSUPPORTED_AGENT"
)
STONITH_UNFENCING_FAILED = M("STONITH_UNFENCING_FAILED")
STONITH_UNFENCING_DEVICE_STATUS_FAILED = M(
    "STONITH_UNFENCING_DEVICE_STATUS_FAILED"
)
STONITH_UNFENCING_SKIPPED_DEVICES_FENCED = M(
    "STONITH_UNFENCING_SKIPPED_DEVICES_FENCED"
)
STONITH_RESTARTLESS_UPDATE_UNABLE_TO_PERFORM = M(
    "STONITH_RESTARTLESS_UPDATE_UNABLE_TO_PERFORM"
)
SERVICE_COMMANDS_ON_NODES_STARTED = M("SERVICE_COMMANDS_ON_NODES_STARTED")
SERVICE_COMMANDS_ON_NODES_SKIPPED = M("SERVICE_COMMANDS_ON_NODES_SKIPPED")
SERVICE_COMMAND_ON_NODE_ERROR = M("SERVICE_COMMAND_ON_NODE_ERROR")
SERVICE_COMMAND_ON_NODE_SUCCESS = M("SERVICE_COMMAND_ON_NODE_SUCCESS")
SERVICE_UNABLE_TO_DETECT_INIT_SYSTEM = M("SERVICE_UNABLE_TO_DETECT_INIT_SYSTEM")
SYSTEM_WILL_RESET = M("SYSTEM_WILL_RESET")
# TODO: remove, use ADD_REMOVE reports
TAG_ADD_REMOVE_IDS_DUPLICATION = M("TAG_ADD_REMOVE_IDS_DUPLICATION")
# TODO: remove, use ADD_REMOVE reports
TAG_ADJACENT_REFERENCE_ID_NOT_IN_THE_TAG = M(
    "TAG_ADJACENT_REFERENCE_ID_NOT_IN_THE_TAG"
)
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_ADD_AND_REMOVE_IDS_AT_THE_SAME_TIME = M(
    "TAG_CANNOT_ADD_AND_REMOVE_IDS_AT_THE_SAME_TIME"
)
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_ADD_REFERENCE_IDS_ALREADY_IN_THE_TAG = M(
    "TAG_CANNOT_ADD_REFERENCE_IDS_ALREADY_IN_THE_TAG"
)
TAG_CANNOT_CONTAIN_ITSELF = M("TAG_CANNOT_CONTAIN_ITSELF")
TAG_CANNOT_CREATE_EMPTY_TAG_NO_IDS_SPECIFIED = M(
    "TAG_CANNOT_CREATE_EMPTY_TAG_NO_IDS_SPECIFIED"
)
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_PUT_ID_NEXT_TO_ITSELF = M("TAG_CANNOT_PUT_ID_NEXT_TO_ITSELF")
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_REMOVE_ADJACENT_ID = M("TAG_CANNOT_REMOVE_ADJACENT_ID")
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_REMOVE_REFERENCES_WITHOUT_REMOVING_TAG = M(
    "TAG_CANNOT_REMOVE_REFERENCES_WITHOUT_REMOVING_TAG"
)
TAG_CANNOT_REMOVE_TAG_REFERENCED_IN_CONSTRAINTS = M(
    "TAG_CANNOT_REMOVE_TAG_REFERENCED_IN_CONSTRAINTS"
)
TAG_CANNOT_REMOVE_TAGS_NO_TAGS_SPECIFIED = M(
    "TAG_CANNOT_REMOVE_TAGS_NO_TAGS_SPECIFIED"
)
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_SPECIFY_ADJACENT_ID_WITHOUT_IDS_TO_ADD = M(
    "TAG_CANNOT_SPECIFY_ADJACENT_ID_WITHOUT_IDS_TO_ADD"
)
# TODO: remove, use ADD_REMOVE reports
TAG_CANNOT_UPDATE_TAG_NO_IDS_SPECIFIED = M(
    "TAG_CANNOT_UPDATE_TAG_NO_IDS_SPECIFIED"
)
# TODO: remove, use ADD_REMOVE reports
TAG_IDS_NOT_IN_THE_TAG = M("TAG_IDS_NOT_IN_THE_TAG")
TMP_FILE_WRITE = M("TMP_FILE_WRITE")
UNABLE_TO_CONNECT_TO_ANY_REMAINING_NODE = M(
    "UNABLE_TO_CONNECT_TO_ANY_REMAINING_NODE"
)
UNABLE_TO_CONNECT_TO_ALL_REMAINING_NODE = M(
    "UNABLE_TO_CONNECT_TO_ALL_REMAINING_NODE"
)
UNABLE_TO_GET_AGENT_METADATA = M("UNABLE_TO_GET_AGENT_METADATA")
UNABLE_TO_GET_SBD_CONFIG = M("UNABLE_TO_GET_SBD_CONFIG")
UNABLE_TO_GET_SBD_STATUS = M("UNABLE_TO_GET_SBD_STATUS")
UNABLE_TO_PERFORM_OPERATION_ON_ANY_NODE = M(
    "UNABLE_TO_PERFORM_OPERATION_ON_ANY_NODE"
)
WATCHDOG_INVALID = M("WATCHDOG_INVALID")
UNSUPPORTED_OPERATION_ON_NON_SYSTEMD_SYSTEMS = M(
    "UNSUPPORTED_OPERATION_ON_NON_SYSTEMD_SYSTEMS"
)
USE_COMMAND_NODE_ADD_REMOTE = M("USE_COMMAND_NODE_ADD_REMOTE")
USE_COMMAND_NODE_ADD_GUEST = M("USE_COMMAND_NODE_ADD_GUEST")
USE_COMMAND_NODE_REMOVE_GUEST = M("USE_COMMAND_NODE_REMOVE_GUEST")
USING_DEFAULT_ADDRESS_FOR_HOST = M("USING_DEFAULT_ADDRESS_FOR_HOST")
USING_DEFAULT_WATCHDOG = M("USING_DEFAULT_WATCHDOG")
WAIT_FOR_IDLE_STARTED = M("WAIT_FOR_IDLE_STARTED")
WAIT_FOR_IDLE_ERROR = M("WAIT_FOR_IDLE_ERROR")
WAIT_FOR_IDLE_NOT_LIVE_CLUSTER = M("WAIT_FOR_IDLE_NOT_LIVE_CLUSTER")
WAIT_FOR_IDLE_TIMED_OUT = M("WAIT_FOR_IDLE_TIMED_OUT")
WAIT_FOR_NODE_STARTUP_ERROR = M("WAIT_FOR_NODE_STARTUP_ERROR")
WAIT_FOR_NODE_STARTUP_STARTED = M("WAIT_FOR_NODE_STARTUP_STARTED")
WAIT_FOR_NODE_STARTUP_TIMED_OUT = M("WAIT_FOR_NODE_STARTUP_TIMED_OUT")
WAIT_FOR_NODE_STARTUP_WITHOUT_START = M("WAIT_FOR_NODE_STARTUP_WITHOUT_START")
WATCHDOG_NOT_FOUND = M("WATCHDOG_NOT_FOUND")

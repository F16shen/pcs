from pcs import (
    prop,
    usage,
)
from pcs.cli.common.routing import create_router

property_cmd = create_router(
    {
        "help": lambda _lib, _argv, _modifiers: print(usage.property(_argv)),
        "set": prop.set_property,
        "unset": prop.unset_property,
        # TODO remove, deprecated command
        # replaced with 'config'
        "list": prop.list_property_deprecated,
        # TODO remove, deprecated command
        # replaced with 'config'
        "show": prop.list_property_deprecated,
        "config": prop.list_property,
        "get_cluster_properties_definition": (
            prop.print_cluster_properties_definition
        ),
    },
    ["property"],
    default_cmd="config",
)

"""An AWS Python Pulumi program"""

# import pulumi_aws as aws
from common import register_auto_tags

# from pulumi import export

import configuration

config = configuration.load()
register_auto_tags(
    {
        "Project": config["metadata"]["project"],
        "Stack": config["metadata"]["stack"],
        "Client": config["tagging"]["client"],
        "Environment": config["tagging"]["environment"],
    }
)

resource_name_prefix = f'{config["metadata"]["project"]}-{config["metadata"]["stack"]}'

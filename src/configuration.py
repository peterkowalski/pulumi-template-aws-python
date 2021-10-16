"""An AWS Python Pulumi configuration module"""

from typing import TypedDict

import common
import pulumi


class Configuration(TypedDict):
    """Main configuration dictionary."""

    metadata: common.Metadata
    tagging: common.Tags


def load() -> Configuration:
    """Load configuration from YAML file.

    Returns:
        A configuration dictionary."""
    tags_config = pulumi.Config("tags")
    aws_config = pulumi.Config("aws")

    return Configuration(
        metadata={
            "project": pulumi.get_project(),
            "stack": pulumi.get_stack().split(".")[1],
            "region": aws_config.require("region"),
        },
        tagging={
            "client": tags_config.require("client"),
            "environment": tags_config.require("environment"),
        },
    )

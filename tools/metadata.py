from dataclasses import dataclass


@dataclass(frozen=True)
class ToolMetadata:
    """
    Metadata describing a tool.
    """

    name: str
    description: str
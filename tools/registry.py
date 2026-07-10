import logging

from tools.base import BaseTool


class ToolRegistry:
    """
    Stores and manages all available tools.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self._tools = {}

    def register(self, tool: BaseTool):

        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' is already registered."
            )

        self._tools[tool.name] = tool

        self.logger.info(
            f"Registered tool: {tool.name}"
        )

    def get(self, name: str) -> BaseTool:

        if name not in self._tools:
            raise ValueError(
                f"Tool '{name}' not found."
            )

        return self._tools[name]

    def execute(self, name: str, **kwargs):

        tool = self.get(name)

        return tool.execute(**kwargs)

    def list_tools(self):

        return list(self._tools.keys())
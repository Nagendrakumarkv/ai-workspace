from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for every tool in the system.

    Every new tool must inherit from this class.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Human readable description.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool.

        Returns:
            Any result produced by the tool.
        """
        pass
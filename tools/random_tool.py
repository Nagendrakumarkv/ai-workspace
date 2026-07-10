import logging
import random

from tools.base import BaseTool


class RandomTool(BaseTool):
    """
    Tool for generating random integers.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

    @property
    def name(self) -> str:
        return "random"

    @property
    def description(self) -> str:
        return "Generates a random integer within a given range."

    def execute(self, **kwargs):

        start = kwargs.get("start")
        end = kwargs.get("end")

        if start is None:
            raise ValueError("start is required.")

        if end is None:
            raise ValueError("end is required.")

        if start > end:
            raise ValueError("start cannot be greater than end.")

        self.logger.info(
            f"Generating random number between {start} and {end}"
        )

        value = random.randint(start, end)

        self.logger.info(f"Generated number: {value}")

        return value
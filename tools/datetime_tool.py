from datetime import datetime
import logging

from tools.base import BaseTool


class DateTimeTool(BaseTool):
    """
    Tool for retrieving the current system date and time.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

    @property
    def name(self) -> str:
        return "datetime"

    @property
    def description(self) -> str:
        return "Returns the current system date and time."

    def execute(self, **kwargs):

        self.logger.info("Fetching current date and time.")

        current_time = datetime.now()

        return {
            "date": current_time.strftime("%Y-%m-%d"),
            "time": current_time.strftime("%H:%M:%S"),
            "datetime": current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
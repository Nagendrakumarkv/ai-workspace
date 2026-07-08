import logging

from config.logging_config import configure_logging
from config.settings import get_settings


class Application:

    def __init__(self):

        configure_logging()

        self.logger = logging.getLogger("application")

        self.settings = get_settings()

    def start(self):

        self.logger.info("Starting application")

        self.logger.info(
            f"Application: {self.settings.app_name}"
        )

        self.logger.info(
            f"Model: {self.settings.model_name}"
        )

        self.logger.info("Application started successfully")
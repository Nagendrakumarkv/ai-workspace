import logging

from google import genai
from google.genai.errors import ClientError

from config.settings import Settings
from llm.base import BaseLLMClient
from llm.exceptions import (
    LLMConnectionError,
    LLMResponseError,
)
from prompts.base import Prompt

class GeminiClient(BaseLLMClient):
    """
    Gemini LLM Client
    """

    def __init__(self, settings: Settings):

        self.settings = settings

        self.logger = logging.getLogger(__name__)

        self.client = genai.Client(
            api_key=self.settings.gemini_api_key
        )

        self.model = self.settings.model_name

        self.logger.info("Gemini Client Initialized")

    def generate(self, prompt: Prompt) -> str:

        try:

            self.logger.info("Sending request to Gemini")

            response = self.client.models.generate_content(
                model=self.model,
                contents=f""",
                {prompt.system}
                User:
                {prompt.user}
                """,
            )

            if not response.text:
                raise LLMResponseError(
                    "Gemini returned an empty response."
                )

            self.logger.info("Response received successfully")

            return response.text

        except ClientError as error:

            self.logger.exception(error)

            raise LLMConnectionError(
                "Failed to connect to Gemini."
            ) from error

        except Exception as error:

            self.logger.exception(error)

            raise LLMResponseError(str(error)) from error
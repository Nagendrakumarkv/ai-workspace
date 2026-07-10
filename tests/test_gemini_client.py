from unittest.mock import Mock, patch

from llm.gemini_client import GeminiClient
from config.settings import get_settings
from prompts.base import Prompt


def test_generate():

    settings = get_settings()

    prompt = Prompt(
        system="System",
        user="Hello"
    )

    with patch("llm.gemini_client.genai.Client") as mock_client:

        fake_response = Mock()
        fake_response.text = "Hello from Gemini"

        mock_client.return_value.models.generate_content.return_value = fake_response

        client = GeminiClient(settings)

        response = client.generate(prompt)

        assert response == "Hello from Gemini"
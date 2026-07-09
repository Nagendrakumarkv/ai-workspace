from config.settings import get_settings


def test_settings_loaded():

    settings = get_settings()

    assert settings.app_name == "AI Workspace"

    assert settings.model_name == "gemini-2.5-flash"

    assert settings.gemini_api_key != ""
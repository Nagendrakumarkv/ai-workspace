from prompts.builder import PromptBuilder


def test_prompt_builder():

    builder = PromptBuilder()

    prompt = builder.build("Hello")

    assert prompt.user == "Hello"

    assert "AI Workspace" in prompt.system
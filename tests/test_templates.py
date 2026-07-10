from prompts.builder import PromptBuilder


def test_prompt_template():

    builder = PromptBuilder()

    prompt = builder.build(
        "Hello",
        [],
    )

    assert "Hello" in prompt.user

    assert "Conversation History" in prompt.user

    assert "AI Workspace" in prompt.system
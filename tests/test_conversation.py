from memory.conversation import ConversationManager


def test_conversation():

    memory = ConversationManager()

    memory.add_user_message("Hello")

    memory.add_assistant_message("Hi")

    assert len(memory.history()) == 2

    assert memory.history()[0].role == "user"

    assert memory.history()[1].role == "assistant"
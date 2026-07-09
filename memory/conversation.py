from memory.message import Message


class ConversationManager:

    def __init__(self):

        self.messages = []

    def add_user_message(self, text: str):

        self.messages.append(
            Message(
                role="user",
                content=text,
            )
        )

    def add_assistant_message(self, text: str):

        self.messages.append(
            Message(
                role="assistant",
                content=text,
            )
        )

    def history(self):

        return self.messages
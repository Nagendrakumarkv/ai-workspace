from prompts.base import Prompt
from prompts.templates import (
    SYSTEM_TEMPLATE,
    CHAT_TEMPLATE,
)


class PromptBuilder:

    def build(
        self,
        user_prompt: str,
        history,
    ) -> Prompt:

        conversation = "\n".join(
            f"{message.role}: {message.content}"
            for message in history
        )

        user_message = CHAT_TEMPLATE.format(
            history=conversation,
            user=user_prompt,
        )

        return Prompt(
            system=SYSTEM_TEMPLATE,
            user=user_message,
        )
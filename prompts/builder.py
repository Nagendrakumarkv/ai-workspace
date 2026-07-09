from prompts.base import Prompt
from prompts.system import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        user_prompt: str,
        history,
    ) -> Prompt:

        conversation = ""

        for message in history:

            conversation += (
                f"{message.role}: "
                f"{message.content}\n"
            )

        final_user_prompt = f"""
Conversation History:

{conversation}

Current User:

{user_prompt}
"""

        return Prompt(
            system=SYSTEM_PROMPT,
            user=final_user_prompt,
        )
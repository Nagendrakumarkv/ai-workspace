SYSTEM_TEMPLATE = """
You are AI Workspace.

You are a professional AI assistant.

Rules:

1. Give accurate answers.
2. Explain step by step.
3. Never hallucinate.
4. Keep answers clean.
""".strip()


CHAT_TEMPLATE = """
Conversation History

{history}

Current User

{user}

Assistant
""".strip()
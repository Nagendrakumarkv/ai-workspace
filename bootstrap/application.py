import logging

from config.logging_config import configure_logging
from config.settings import get_settings
from llm.gemini_client import GeminiClient
from prompts.builder import PromptBuilder
from memory.conversation import ConversationManager
from tools.registry import ToolRegistry
from tools.calculator import CalculatorTool
from tools.datetime_tool import DateTimeTool
from tools.random_tool import RandomTool


class Application:
    def __init__(self):
        configure_logging()
        self.logger = logging.getLogger(__name__)
        self.settings = get_settings()
        self.llm = GeminiClient(self.settings)
        self.registry = ToolRegistry()
        self.registry.register(CalculatorTool())
        self.registry.register(DateTimeTool())
        self.registry.register(RandomTool())
        self.prompt_builder = PromptBuilder()
        self.memory = ConversationManager()

    def start(self):
        self.logger.info("Application Started")
        
        print("=" * 60)
        print("Welcome to AI Workspace")
        print("\nAvailable Tools")
        for tool in self.registry.metadata():
            print(f"- {tool.name}: {tool.description}")
        print("Type 'exit' to quit.")
        print("=" * 60)

        while True:
            prompt = input("\nYou: ")

            if prompt.lower() == "exit":
                self.logger.info("Application Closed")
                print("\nGoodbye 👋")
                break

            try:
                self.memory.add_user_message(prompt)
                prompt_object = self.prompt_builder.build(prompt, self.memory.history())
                response = self.llm.generate(prompt_object)
                self.memory.add_assistant_message(response)
                print("\nAssistant:")
                print(response)

            except Exception as error:
                self.logger.exception(error)
                print("\nSomething went wrong.")
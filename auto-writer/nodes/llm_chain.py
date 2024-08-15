from langchain_openai import ChatOpenAI
import config
import os

os.environ["OPENAI_API_BASE"] = config.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY

class LLMChain:
    def __init__(self, llm, prompt):
        self.chat_model = ChatOpenAI(
            model="",
            temperature=0,
        )
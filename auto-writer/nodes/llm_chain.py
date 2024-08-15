from langchain_openai import ChatOpenAI
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
import config
import os

os.environ["OPENAI_API_BASE"] = config.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
os.environ["QIANFAN_AK"] = config.QIANFAN_AK
os.environ["QIANFAN_SK"] = config.QIANFAN_SK

class LLMChain:
    def __init__(self):
        self.cm_openai = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
        )
        
        self.cm_baidu = QianfanChatEndpoint(
            model="ERNIE-Speed-8K",
        )
        
    def SceneAnalysis(self):
        prompt = """根据用户输入，判断用户需要哪种类型的选题。用户的选题只会在以下几种类型中：
        1. 技术类
        2. 生活类
        3. 资讯类
        只要返回选题类型，不要有其他内容，否则会受到惩罚。
        用户输入的内容是：{query}"""
        
        chain = ChatPromptTemplate.from_template(prompt) | self.cm_baidu | StrOutputParser
        return chain
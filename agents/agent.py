from pydantic import BaseModel, Field
from abc import abstractmethod
import os
import sys

sys.path.append("../")

from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage

from tools.tools import BaseTool

import warnings
warnings.filterwarnings("ignore")


os.environ["LLAMA_API_KEY"] = 'ollama'
os.environ["LLAMA_API_BASE"] = 'http://localhost:11434'


class BaseAgent():
    name: str = ""
    engine: str = ""
    tool_list: dict = {}

    @abstractmethod
    def infer():
        pass


class Llama(BaseAgent):
    name: str = "Llama"
    engine: str = "llama3.2"
    tool_list: dict = {}
    sampling: str = {"num_ctx": 40}

    def __init__(self, 
                 name: str = "Llama", 
                 engine: str = "llama3.2", 
                 tools_list: list = [], 
                 sampling: str = {"num_ctx": 40}):
        self.name = name
        self.engine = engine
        self.sampling = sampling
        for tool in tools_list:
            self.add_tool(tool)


    def infer(self, context: str = "", message_history: list = None, instruction: str = ""):
        messages = []
        if context:
            messages.append(SystemMessage(context))
        if message_history:
            messages.extend(message_history)
        
        messages.append(HumanMessage(instruction))
        
        llm = ChatOllama(
            base_url=os.environ["LLAMA_API_BASE"],
            api_key=os.environ["LLAMA_API_KEY"],
            model=self.engine,
            options=self.sampling,
        )
        # print(messages)
        response = llm.invoke(messages)
        response_str = response.content

        return response_str, {"response": response, "messages": messages} 
    
    def add_tool(self, tool: BaseTool):
        if tool.tool_name not in self.tool_list:
            self.tool_list[tool.tool_name] = tool
        else:
            print("The tool is already existing.")
from pydantic import BaseModel, Field
from abc import abstractmethod

class BaseTool(BaseModel):
    tool_name: str
    tool_description: str
    parameters: dict = {}


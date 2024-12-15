import yaml
from string import Template
import sys
sys.path.append("../")
from tools.tools import BaseTool
def load_prompt(file_name: str = "./agents/prompt.yaml"):
    with open(file_name, "r", encoding="utf-8") as file:
        prompts = yaml.safe_load(file)
    return prompts

def generate_query_prompt(task_description: str, tools_description: str):
    template = load_prompt()["generate_query_prompt"]
    args: dict = {}
    args["task_description"] = task_description
    args["tools_description"] = tools_description
    prompt = Template(template).safe_substitute(args)
    return prompt

def generate_tool_description(tool: BaseTool):
    template = load_prompt()["tool_description"]
    args: dict = {}
    args["tool_name"] = tool.tool_name
    args["tool_description"] = tool.tool_description
    for key, value in tool.parameters.items():
        args[f"{key}_description"] = value
    prompt = Template(template).safe_substitute(args)
    return "\n" + prompt + "\n" 

def generate_final_answer_prompt(task_description: str, query_result: str):
    template = load_prompt()["generate_final_answer_prompt"]
    args: dict = {}
    args["task_description"] = task_description
    args["query_result"] = query_result
    prompt = Template(template).safe_substitute(args)
    return prompt

def get_system_prompt():
    return load_prompt()["system_prompt"]
import sys
sys.path.append("../")
from agents.prompt import (
    generate_query_prompt,
    generate_tool_description,
    generate_final_answer_prompt,
    get_system_prompt
)
from agents.utils import extract_json
from colorama import init, Fore, Back, Style
from tools import TOOL_MAPPING
from langchain.schema import HumanMessage, AIMessage, SystemMessage

def run_scholar(agent):
    tools_prompt = ""
    for key, tool in agent.tool_list.items():
        tools_prompt += generate_tool_description(tool)

    print(Fore.GREEN + "\nScholar Assistant: \n" + Style.RESET_ALL, end = "")
    print("Hello, how can I help you? (Input 'STOP' to end the chat.)\n")
    first_round = True

    while(1):
        user_input = input(Fore.BLUE + "User:\n" + Style.RESET_ALL)
        if user_input == "STOP":
            break
        instruction = generate_query_prompt(
            task_description=user_input,
            tools_description=tools_prompt
        )
        if first_round:
            res =  agent.infer(context=get_system_prompt(), instruction = instruction)
            messages = res[1]["messages"][:-1]
            messages.append(HumanMessage(user_input))
            first_round = False
        else:
            res = agent.infer(message_history=messages, instruction = instruction)
            messages.append(HumanMessage(user_input))

        param = extract_json(res[0])

        answer = TOOL_MAPPING[param["tool_name"]](**param["parameters"])

        instruction = generate_final_answer_prompt(
            task_description=user_input,
            query_result=answer
        )
        res =  agent.infer(message_history=messages, instruction = instruction)
        print(Fore.GREEN + "\nScholar Assistant: \n" + Style.RESET_ALL, end='')
        print(res[0])
        messages.append(AIMessage(res[0]))
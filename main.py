import sys
sys.path.append('./')
from tools.scholar_tool import (
    init_scholar_tools
)
from agents.agent import Llama
from agents.call import run_scholar


llama = Llama(tools_list=init_scholar_tools())
run_scholar(llama)

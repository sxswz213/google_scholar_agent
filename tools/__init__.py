import sys
sys.path.append("../")
from tools import scholar_tool

TOOL_MAPPING = {
    "scholarly_search_author": scholar_tool.scholarly_search_author,
    "scholarly_search_keyword": scholar_tool.scholarly_search_keyword,
    "scholarly_search_pubs": scholar_tool.scholarly_search_pubs,
}
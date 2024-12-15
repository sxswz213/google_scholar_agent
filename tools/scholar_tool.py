import sys
sys.path.append("../")
from tools.tools import BaseTool

def scholarly_search_author(
    query: str = "",
) -> str:
    """a wrapper for scholarly.search_author"""
    from scholarly import scholarly

    search_query = scholarly.search_author(query)

    result = ""
    for item in search_query:
        result += "{"
        for k, v in item.items():
            if k not in ["container_type", "filled", "source", "scholar_id"]:
                result += f"{k}: {v}\n"
        result += "}"
        result += "\n"
    return result


def scholarly_search_keyword(
    query: str = "",
) -> str:
    """a wrapper for scholarly.search_keyword"""
    from scholarly import scholarly

    search_query = scholarly.search_keyword(query)
    result = ""
    for item in search_query:
        result += "{"
        for k, v in item.items():
            if k not in ["container_type", "filled", "source", "scholar_id"]:
                result += f"{k}: {v}\n"
        result += "}"
        result += "\n"
    return result


def scholarly_search_pubs(
    query: str = "",
    max_count: int = 3
) -> str:
    """a wrapper for scholarly.search_pubs"""
    from scholarly import scholarly
    from itertools import islice

    search_query = scholarly.search_pubs(query)
    result = ""
    for item in islice(search_query, max_count):
        result += "{"
        for k, v in item.items():
            if k not in ["container_type", "filled", "source", "scholar_id"]:
                result += f"{k}: {v}\n"
        result += "}"
        result += "\n"
    return result

def init_scholar_tools():
    tools_list = []
    scholarly_search_author = BaseTool(
        tool_name ="scholarly_search_author", 
        tool_description = "Search for informations about the specific author from the database of google scholar.", 
        parameters = {"query": "The name of author you want to search."})
    tools_list.append(scholarly_search_author)

    scholarly_search_pubs = BaseTool(
        tool_name ="scholarly_search_pubs", 
        tool_description = "[Default tool]Search for informations about the specific article or publication from the database of google scholar. The usual choice.", 
        parameters = {"query": "The name of article or publication you want to search."})
    tools_list.append(scholarly_search_pubs)

    return tools_list
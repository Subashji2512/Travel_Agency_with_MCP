import os
import asyncio # sychronous programming,

from dotenv import load_dotenv
load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

from langchain_mcp_adapters.client import MultiServerMCPClient # class to create the client

## create the MCP client
##client = MultiServerMCPClient(code to connect with the server)


client = MultiServerMCPClient(
    {
        "serpapi": { ## server name remote MCP server
            "transport": "streamable_http", ##means your application connects to a remote MCP server over HTTP
            "url": f"https://mcp.serpapi.com/{SERP_API_KEY}/mcp",
        },

        "aviationstack": { ## server name for local MCP server
                    
            "transport": "stdio", ## this is local so stdio is used, if it was remote then streamable_http is used
            "command": r"D:\MCP_travel_agency\AI-Travel-Planning-System-using-LangGraph\aviationstack-mcp\.venv\Scripts\python.exe",
            "args":["-m","aviationstack_mcp","mcp","run"],
            "env":{"AVIATIONSTACK_API_KEY":AVIATIONSTACK_API_KEY}
            }
    }
)



## ask the server what are the tools it have
# async def main():
#     tools = await client.get_tools() ## ask the tools it have
#     print("AVAILABLE MCP TOOLS:\n")
#     for tool in tools:
#         print(tool.name)

## now we gonna use the search tool to know the schema of the tool and then use it to search for best hotels

async def main2():
    tools = await client.get_tools()
    search_tools = next(
        tool
        for tool in tools
        if tool.name == "search") ## this specificaly asks the search tool
    print(search_tools.args_schema) ## this gives the schema of the tool

    result = await search_tools.ainvoke( # this will use the search tool with a the given schema
         {
             "params": {
                "engine": "google",
                "q": "Best hotels in Bali",
                "location": "Bali, Indonesia",
                "hl": "en",
                "gl": "id"
            },
            "mode": "compact"
        }
    )
    print(result)

## Function to make the main.py to use the MCP server 
search_tool = None
aviation_tools ={}
async def initialize_mcp(): ## this function is used to connect to the servers and know the tools only once
                            ##bcoz when ever user makes request it use the get_tools, so client ask abt the tools
                            ## so store the tools in the momory and call them 
    global search_tool 
    global aviation_tools

    if search_tool is not None:
        return
    tools = await client.get_tools()
    print("AVAILABLE MCP TOOLS:\n")
    for tool in tools:
        print(tool.name)

    search_tool = next(
        tool
        for tool in tools
        if tool.name == "search")
    
    aviation_tools = {
        tool.name: tool
        for tool in tools
        if tool.name != "search"    
    }

## This function is used to search for the hotels in the given location using the search tool using MCP remote server
async def serp_mcp_search(q:str):
    await initialize_mcp()
    result = await search_tool.ainvoke( # this will use the search tool with a the given schema
             {
                "params": {
                    "q": q
                },
                "mode": "compact"
            }
        )
    print(result)

## This function is used to search for the flights in the given location using the search tool using MCP local server
async def aviation_mcp_call(
    tool_name: str,
    tool_args: dict = None
):

    tools = await client.get_tools()

    tool = next(
        t for t in tools
        if t.name == tool_name
    )

    result = await tool.ainvoke(
        tool_args or {}
    )

    return result

async def get_airports():

    await initialize_mcp()

    tool = aviation_tools.get("list_airports")

    if not tool:
        return "Airport tool unavailable"

    result = await tool.ainvoke({})

    return result


async def get_airlines():

    await initialize_mcp()

    tool = aviation_tools.get("list_airlines")

    if not tool:
        return "Airline tool unavailable"

    result = await tool.ainvoke({})

    return result

if __name__ == "__main__":
    #asyncio.run(main())
    asyncio.run(main2())
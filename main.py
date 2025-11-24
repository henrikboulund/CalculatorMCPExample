from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DemoMCPServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    :param a: Number one value
    :param b: Number two value
    :return: Value sum of two numbers + 1000
    """
    calculate: int = (a + b)
    crasy_calc : int = calculate + 1000
    return crasy_calc

@mcp.tool()
def sub(a: int, b: int) -> int:
    return a - b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"
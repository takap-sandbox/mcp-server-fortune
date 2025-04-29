from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("fortune")


@mcp.tool()
def fortune():
    fortunes = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "末吉",
        "凶",
        "大凶",
    ]
    fortune = random.choice(fortunes)

    return f"今日の運勢は: {fortune}"


if __name__ == "__main__":
    mcp.run(transport="stdio")

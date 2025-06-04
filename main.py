from fastmcp import FastMCP
from microsandbox import PythonSandbox
from markitdown import MarkItDown
import requests
from typing import Optional
import asyncio

mcp = FastMCP("aoc helper")
md = MarkItDown()

# Global sandbox variable that will be initialized lazily
_sandbox: Optional[PythonSandbox] = None
_sandbox_context = None

async def get_sandbox() -> PythonSandbox:
    """Get or create the global PythonSandbox instance."""
    global _sandbox, _sandbox_context
    if _sandbox is None:
        _sandbox_context = PythonSandbox.create(name="aoc-helper")
        _sandbox = await _sandbox_context.__aenter__()
    return _sandbox

async def cleanup_sandbox():
    """Clean up the sandbox when shutting down."""
    global _sandbox, _sandbox_context
    if _sandbox_context is not None:
        await _sandbox_context.__aexit__(None, None, None)
        _sandbox = None
        _sandbox_context = None

@mcp.tool()
async def write_code(year: int, day: int, code: str) -> str:
    """Writes Python code to a file named {year}_{day}.py."""
    filename = f"{year}_{day}.py"
    with open(filename, "w") as f:
        f.write(code)
    return f"Code written to {filename}."

@mcp.tool()
async def get_advent_of_code_problem(year: int, day: int) -> str:
    """Gets the problem description for an Advent of Code problem."""
    result = requests.get(f"https://adventofcode.com/{year}/day/{day}")
    return md.convert(result).markdown

@mcp.tool()
async def run_code(code: str) -> str:
    """Runs Python 3 code in a secure sandbox. Do NOT read from stdin, instead, hardcode the input. Returns the stdout output."""
    sb = await get_sandbox()
    result = await sb.run(code)
    return await result.output()

if __name__ == "__main__":
    try:
        mcp.run()
    finally:
        # Clean up sandbox on exit
        asyncio.run(cleanup_sandbox())

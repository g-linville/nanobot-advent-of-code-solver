# Nanobot Advent of Code solver

This is an example of how to use nanobot. I wrote a small MCP server with a few custom tools to help it solve problems from Advent of Code.

### Usage

First make sure you clone the repo and run `uv sync` to install the packages. (You need to have `uv` installed for this.)

You will also need to have [microsandbox](https://github.com/microsandbox/microsandbox) installed. Start the server by running `msb server start --dev`.

Then you can run this agent with [nanobot](https://github.com/nanobot-ai/nanobot) by running `nanobot run nanobot.yaml`. Tell the agent which problem you would like to solve. I typically say something like "try 2024 day 2".

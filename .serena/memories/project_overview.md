# Project Overview: faemcp

## Purpose
faemcp is an MCP (Model Context Protocol) server that provides template-based prompts with variable substitution. It allows users to fill template files with user-provided variables, specifically designed to work with Claude Code.

## Key Features
- Template-based prompt generation using `prompts/start-prompt.md`
- Interactive parameter collection via `ctx.elicit`
- Error handling with automatic webpage display for debugging
- Integration with Claude Code via `/start` slash command

## Tech Stack
- **Language**: Python 3.13+
- **Framework**: FastMCP for MCP server implementation
- **Package Manager**: uv
- **Type Checking**: mypy
- **Linting/Formatting**: ruff
- **Task Runner**: Taskfile (task command)

## Main Components
- `server.py`: MCP server with tools and prompts
- `template_processing.py`: Template loading and variable replacement
- `error_handling.py`: Error display functionality
- `main.py`: Entry point
- `prompts/start-prompt.md`: Template file

## Installation & Usage
- Install via uvx: `uvx --from git+https://github.com/faekiva/faemcp faemcp`
- Add to Claude Code: `claude mcp add faemcp -- uvx --from git+https://github.com/faekiva/faemcp faemcp`
- Use with `/start` command in Claude Code
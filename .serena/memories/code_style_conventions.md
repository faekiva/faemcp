# Code Style and Conventions for faemcp

## Code Style
- **Python Version**: 3.13+
- **Linting**: ruff
- **Formatting**: ruff format
- **Type Checking**: mypy with `--ignore-missing-imports`
- **Line Length**: 90 characters max (per user preferences)

## Project Structure
```
src/faemcp/
├── __init__.py
├── __main__.py
├── main.py           # Entry point
├── server.py         # MCP server with tools/prompts
├── template_processing.py  # Template handling
├── error_handling.py # Error display
└── prompts/
    └── start-prompt.md  # Template file
```

## Code Conventions
- **Async Functions**: Use async/await for MCP tools and prompts
- **Type Hints**: Required for all functions
- **Docstrings**: Required for public functions
- **Error Handling**: Use error_handling.py for user-facing errors
- **MCP Tools**: Use `@mcp.tool()` decorator
- **MCP Prompts**: Use `@mcp.prompt()` decorator

## Import Style
- Standard library first
- Third-party imports second  
- Local imports last (relative imports with .)

## Dependencies
- Core: `mcp[cli]>=1.12.3`
- Development tools managed via uv

## Testing
- **Framework**: testify (Go preference, but this is Python - may need pytest)
- **Mocking**: Prefer mock generation libraries
- **Structure**: Given/When/Then format preferred
- **Test Location**: Separate files from main code
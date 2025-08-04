# Suggested Commands for faemcp Development

## Development Tasks (using task command)
- `task install` - Install dependencies using uv
- `task dev` - Run the MCP server in development mode
- `task lint` - Run linting and type checking (ruff + mypy)
- `task format` - Format code with ruff
- `task clean` - Clean up temporary files and caches
- `task resume` - Resume the most recent Claude Code session

## Direct uv Commands
- `uv sync` - Install/sync dependencies
- `uv run python main.py` - Run server directly
- `uv run ruff check .` - Run linting
- `uv run ruff format .` - Format code
- `uv run mypy . --ignore-missing-imports` - Type checking

## Installation/Deployment
- `uvx --from git+https://github.com/faekiva/faemcp faemcp` - Run directly
- `uvx --force --from git+https://github.com/faekiva/faemcp faemcp` - Force reinstall latest version
- `claude mcp add faemcp -- uvx --from git+https://github.com/faekiva/faemcp faemcp` - Add to Claude Code

## Testing
- No specific test commands found - tests may need to be added

## System Commands (Darwin)
- Standard Unix commands: `git`, `ls`, `cd`, `grep`, `find`
- Preferred modern alternatives (if available): `fd`, `rg`, `sd`
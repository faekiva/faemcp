# faemcp

MCP server that provides template-based prompts with variable substitution.

## Quick Start

Run directly from GitHub using uvx:

```bash
uvx --from git+https://github.com/yourusername/faemcp faemcp
```

## Adding to Claude Code

Add this MCP server to your Claude Code configuration:

```bash
# Add to Claude Code MCP servers
claude mcp add faemcp "uvx --from git+https://github.com/yourusername/faemcp faemcp"
```

## Usage

Once added to Claude Code, use the `/start` prompt with:
- **context**: What context should the model have to help you do the right thing?
- **goals**: What goals do you want the model to keep in mind? Prioritize them  
- **query**: What's the first thing you're asking of it?

The server will fill the `prompts/start-prompt.md` template with your provided variables.
# faemcp

MCP server that provides template-based prompts with variable substitution.

## Quick Start

[Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

Run directly from GitHub using uvx:

```bash
uvx --from git+https://github.com/faekiva/faemcp faemcp
```

## Adding to Claude Code

Add this MCP server to your Claude Code configuration:

```bash
# Recommended: Using uvx (requires uv to be installed)
claude mcp add faemcp -- uvx --from git+https://github.com/faekiva/faemcp faemcp
```

## Usage

Once added to Claude Code, use the `/start` prompt with:
- **context**: What context should the model have to help you do the right thing?
- **goals**: What goals do you want the model to keep in mind? Prioritize them  
- **query**: What's the first thing you're asking of it?

The server will fill the `prompts/start-prompt.md` template with your provided variables.

## Error Handling

When the server encounters an error, it will automatically open a webpage in your default browser displaying:
- **Error type and message**: Clear description of what went wrong
- **Full traceback**: Complete stack trace for debugging
- **Helpful suggestions**: Next steps to resolve the issue
- **Formatted display**: Clean, readable HTML with syntax highlighting

This makes debugging configuration issues, missing template files, or other problems much easier.
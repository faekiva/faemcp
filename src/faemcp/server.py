from mcp.server.fastmcp import FastMCP

from .template_processing import (
    load_template,
    replace_template_variables,
)
from .version_info import get_version_info

mcp = FastMCP(name="faemcp")

# Log version information on startup
print(f"Starting {get_version_info()}")


@mcp.tool()
def start_template(context: str, goals: str, query: str) -> str:
    """Fill the start-prompt.md template with user-provided variables.

    Args:
        context: What context should the model have to help you do the right thing?
        goals: What goals do you want the model to keep in mind? Prioritize them
        query: What's the first thing you're asking of it?
    """
    template_content, _ = load_template()

    user_vars = {
        "context": context,
        "goals": goals,
        "query": query,
    }

    return replace_template_variables(template_content, user_vars)


@mcp.prompt(title="Start template")
async def start() -> str:  # type: ignore
    """Generate a start prompt using the template."""
    return """I need to collect some information from you to generate your customized start prompt. Please answer these questions:

1. **Context**: What context should the model have to help you do the right thing?

2. **Goals**: What goals do you want the model to keep in mind? Prioritize them.

3. **Query**: What's the first thing you're asking of it?

Please provide your answers, and I'll use them with the start_template tool to generate your start prompt."""

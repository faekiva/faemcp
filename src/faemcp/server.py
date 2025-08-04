from mcp.server.fastmcp import FastMCP, Context

from .template_processing import (
    TemplateParameters,
    load_template,
    replace_template_variables,
)
from .version_info import get_version_info

mcp = FastMCP(name="faemcp")

# Log version information on startup
print(f"Starting {get_version_info()}")


@mcp.tool()
async def start_template(ctx: Context) -> str:  # type: ignore
    """Fill the start-prompt.md template with user-provided variables."""

    template_content, _ = load_template()

    # Elicit template parameters from the user
    result = await ctx.elicit(
        message="Please provide the template parameters to generate your start prompt:",
        schema=TemplateParameters,
    )

    if result.action == "accept" and result.data:
        user_vars = {
            "context": result.data.context,
            "goals": result.data.goals,
            "query": result.data.query,
        }
        return replace_template_variables(template_content, user_vars)
    else:
        return "Template generation cancelled by user."


@mcp.prompt(title="Start template")
async def start() -> str:  # type: ignore
    """Generate a start prompt using the template."""
    return (
        "Please run the start_template tool to generate your customized start prompt."
    )

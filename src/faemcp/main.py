import re
from pathlib import Path
from typing import Dict, List, Tuple
from importlib import resources
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(name="faemcp")


def parse_template_variables(template_content: str) -> List[Tuple[str, str]]:
    """Parse template variables from {{variable:description}} format.

    Returns list of (variable_name, description) tuples.
    """
    pattern = r"\{\{([^:}]+):([^}]+)\}\}"
    matches = re.findall(pattern, template_content, re.DOTALL)
    return [(var.strip(), desc.strip()) for var, desc in matches]


def load_template() -> tuple[str, Dict[str, str]]:
    """Load template content and field descriptions from the template file."""
    try:
        # Use importlib.resources to access package data
        template_content = resources.files("faemcp").joinpath("prompts/start-prompt.md").read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError("Template file not found: prompts/start-prompt.md")

    template_vars = parse_template_variables(template_content)

    if not template_vars:
        raise ValueError("No template variables found in prompts/start-prompt.md")

    descriptions = {var: desc for var, desc in template_vars}
    return template_content, descriptions


# Load template and descriptions at module level
_template_content, _template_descriptions = load_template()


def replace_template_variables(template_content: str, variables: Dict[str, str]) -> str:
    """Replace template variables with provided values."""

    def replacer(match: re.Match[str]) -> str:
        var_name = match.group(1).strip()
        if var_name not in variables:
            raise ValueError(f"Missing required variable: {var_name}")
        return variables[var_name]

    pattern = r"\{\{([^:}]+):[^}]+\}\}"
    return re.sub(pattern, replacer, template_content, flags=re.DOTALL)


@mcp.prompt(title="Start template")
def start(
    context: str = Field(description=_template_descriptions["context"]),
    goals: str = Field(description=_template_descriptions["goals"]),
    query: str = Field(description=_template_descriptions["query"]),
) -> str:
    """Fill the start-prompt.md template with user-provided variables."""

    user_vars = {"context": context, "goals": goals, "query": query}
    return replace_template_variables(_template_content, user_vars)


def main():
    """Entry point for the faemcp command."""
    mcp.run()


if __name__ == "__main__":
    main()

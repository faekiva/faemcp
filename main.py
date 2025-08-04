import re
from pathlib import Path
from typing import Dict, List, Tuple
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
    context: str = Field(
        description="What context should the model have to help you do the right thing?"
    ),
    goals: str = Field(
        description="What goals do you want the model to keep in mind? Prioritize them"
    ),
    query: str = Field(description="What's the first thing you're asking of it?"),
) -> str:
    """Load and fill the start-prompt.md template with user-provided variables."""

    template_path = Path("prompts/start-prompt.md")

    try:
        # Read template file
        if not template_path.exists():
            raise FileNotFoundError(f"Template file not found: {template_path}")

        template_content = template_path.read_text(encoding="utf-8")

        # Parse expected variables from template
        expected_vars = parse_template_variables(template_content)
        expected_var_names = {var[0] for var in expected_vars}

        # Prepare user-provided variables
        user_vars = {"context": context, "goals": goals, "query": query}

        # Validate all required variables are provided
        provided_vars = set(user_vars.keys())
        missing_vars = expected_var_names - provided_vars
        if missing_vars:
            raise ValueError(f"Missing required variables: {', '.join(missing_vars)}")

        # Replace template variables
        filled_template = replace_template_variables(template_content, user_vars)

        return filled_template

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Template file not found: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid template or missing variables: {e}")
    except Exception as e:
        raise Exception(f"Failed to process template: {e}")


if __name__ == "__main__":
    mcp.run()

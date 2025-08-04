import re
from typing import Dict, List, Tuple
from importlib import resources
from pydantic import BaseModel, Field

from .error_handling import open_error_webpage


class TemplateParameters(BaseModel):
    """Schema for collecting template parameters."""

    context: str = Field(
        description="What context should the model have to help you do the right thing?"
    )
    goals: str = Field(
        description="What goals do you want the model to keep in mind? Prioritize them"
    )
    query: str = Field(description="What's the first thing you're asking of it?")


def parse_template_variables(template_content: str) -> List[Tuple[str, str]]:
    """Parse template variables from {{variable:description}} format.

    Returns list of (variable_name, description) tuples.
    """
    pattern = r"\{\{([^:}]+):([^}]+)\}\}"
    matches = re.findall(pattern, template_content, re.DOTALL)
    return [(var.strip(), desc.strip()) for var, desc in matches]


def load_template(
    templatePath: str = "prompts/start-prompt.md",
) -> tuple[str, Dict[str, str]]:
    """Load template content and field descriptions from the template file."""
    try:
        # Use importlib.resources to access package data
        template_content = (
            resources.files("faemcp").joinpath(templatePath).read_text(encoding="utf-8")
        )
    except FileNotFoundError as _:
        error: Exception = FileNotFoundError(
            "Template file not found: prompts/start-prompt.md"
        )
        open_error_webpage(error, "Template File Missing")
        raise error

    template_vars = parse_template_variables(template_content)

    if not template_vars:
        error = ValueError("No template variables found in prompts/start-prompt.md")
        open_error_webpage(error, "Template Configuration Error")
        raise error

    descriptions = {var: desc for var, desc in template_vars}
    return template_content, descriptions


def replace_template_variables(template_content: str, variables: Dict[str, str]) -> str:
    """Replace template variables with provided values."""

    def replacer(match: re.Match[str]) -> str:
        var_name = match.group(1).strip()
        if var_name not in variables:
            error = ValueError(f"Missing required variable: {var_name}")
            open_error_webpage(error, "Template Variable Missing")
            raise error
        return variables[var_name]

    pattern = r"\{\{([^:}]+):[^}]+\}\}"
    return re.sub(pattern, replacer, template_content, flags=re.DOTALL)


# Load template and descriptions at module level

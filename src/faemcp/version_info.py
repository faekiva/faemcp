"""Version information utilities."""
import subprocess
from pathlib import Path


def get_git_hash() -> str:
    """Get the current git commit hash."""
    try:
        # Get the directory where this file is located
        current_dir = Path(__file__).parent.parent.parent
        
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=current_dir,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            return result.stdout.strip()[:8]  # Short hash
        else:
            return "unknown"
    except (subprocess.SubprocessError, FileNotFoundError, subprocess.TimeoutExpired):
        return "unknown"


def get_version_info() -> str:
    """Get version information including git hash."""
    git_hash = get_git_hash()
    return f"faemcp (git: {git_hash})"
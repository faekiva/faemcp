from .server import mcp
from .error_handling import open_error_webpage


def main():
    """Entry point for the faemcp command."""
    try:
        mcp.run()
    except Exception as e:
        # Catch any unhandled exceptions and show error webpage
        open_error_webpage(e, "MCP Server Error")
        raise


if __name__ == "__main__":
    main()
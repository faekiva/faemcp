import sys
import tempfile
import traceback
import webbrowser


def generate_error_html(error: Exception, error_type: str, traceback_str: str) -> str:
    """Generate an HTML error page with error details."""
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>faemcp Error - {error_type}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            background: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .error-type {{
            color: #e74c3c;
            font-size: 24px;
            font-weight: bold;
            margin: 0;
        }}
        .error-message {{
            font-size: 18px;
            margin: 10px 0;
            color: #555;
        }}
        .section {{
            margin: 30px 0;
        }}
        .section h3 {{
            color: #2c3e50;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 10px;
        }}
        .traceback {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 14px;
            line-height: 1.5;
            overflow-x: auto;
            white-space: pre-wrap;
        }}
        .info-box {{
            background: #3498db;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .suggestion {{
            background: #f39c12;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .timestamp {{
            color: #95a5a6;
            font-size: 14px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="error-type">{error_type}</h1>
            <p class="error-message">{error_message}</p>
        </div>
        
        <div class="info-box">
            <strong>📦 faemcp MCP Server Error</strong><br>
            The MCP server encountered an error and is opening this page to help you debug the issue.
        </div>
        
        <div class="section">
            <h3>🔍 Error Details</h3>
            <p><strong>Error Type:</strong> {error_type}</p>
            <p><strong>Error Message:</strong> {error_message}</p>
        </div>
        
        <div class="section">
            <h3>📋 Full Traceback</h3>
            <div class="traceback">{traceback_formatted}</div>
        </div>
        
        <div class="suggestion">
            <strong>💡 Next Steps:</strong><br>
            1. Check the error message and traceback above<br>
            2. Verify your template files and configuration<br>
            3. Check the GitHub repository for known issues<br>
            4. Consider filing a bug report if this is unexpected
        </div>
        
        <div class="timestamp">
            Generated at: {timestamp}
        </div>
    </div>
</body>
</html>
    """

    import datetime

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return html_template.format(
        error_type=error_type,
        error_message=str(error),
        traceback_formatted=traceback_str,
        timestamp=timestamp,
    )


def open_error_webpage(error: Exception, error_type: str = ""):
    """Generate and open an error webpage in the default browser."""
    if error_type == "":
        error_type = type(error).__name__

    # Get the full traceback
    traceback_str = traceback.format_exc()

    # Generate HTML content
    html_content = generate_error_html(error, error_type, traceback_str)

    # Create temporary HTML file
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".html", delete=False, encoding="utf-8"
        ) as f:
            f.write(html_content)
            temp_file_path = f.name

        # Open in default browser
        webbrowser.open(f"file://{temp_file_path}")
        print(f"Error webpage opened at: file://{temp_file_path}", file=sys.stderr)

    except Exception as webpage_error:
        print(f"Failed to open error webpage: {webpage_error}", file=sys.stderr)
        print(f"Original error: {error}", file=sys.stderr)

# Task Completion Checklist for faemcp

## When a task is completed, run these commands:

### 1. Linting and Type Checking
```bash
task lint
# OR individually:
uv run ruff check .
uv run mypy . --ignore-missing-imports
```

### 2. Code Formatting
```bash
task format
# OR:
uv run ruff format .
```

### 3. Testing (if tests exist)
- No specific test runner configured yet
- Consider adding pytest or similar

### 4. Development Testing
```bash
task dev  # Test server runs without errors
```

### 5. Clean Up
```bash
task clean  # Remove temporary files and caches
```

## Quality Checks
- Ensure type safety (mypy passes)
- Ensure code follows ruff linting rules
- Verify MCP server starts without errors
- Test integration with Claude Code if applicable

## Before Committing
- All linting passes
- All type checking passes  
- Code is formatted
- MCP server runs successfully
- Consider writing tests for new functionality

## Note
Based on user preferences:
- Code should be DRY
- Code should be testable (mockable external resources)
- Tests should follow Given/When/Then structure
- Prefer built-in features but suggest libraries when appropriate
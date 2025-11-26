# Contributing

Thank you for considering contributing to **septa-mcp**. The guidelines below help keep changes consistent and maintainable.

## Setup
1. Create and activate a Python 3.11+ virtual environment.
2. Install dependencies (development extras include linting and test tools):
   ```bash
   pip install -e .[dev]
   ```

## Style
- The project uses **Ruff** for linting and formatting. Run fixes before committing:
  ```bash
  ruff format .
  ruff check . --fix
  ```
- Prefer type hints and descriptive docstrings when adding new modules or functions.

## Testing
- Execute the full test suite locally with **pytest**:
  ```bash
  pytest
  ```
- Add or update tests alongside any functional change, especially for new tools or request handling logic.

## Adding new tools
- Implement the tool in `septa_mcp/tools/`, following the existing pattern of a `register` function that attaches to the `FastMCP` server.
- Register the tool in `septa_mcp/tools/__init__.py` so it is included by `register_all`.
- Document any new environment variables or configuration needs in `README.md`.
- Prefer reusing shared helpers in `septa_mcp/tools/http.py` and normalization utilities where appropriate.

## CI expectations
- Pull requests should pass Ruff formatting/linting and the pytest suite before review.
- Keep changes focused with clear motivation in the PR description and include tests for new functionality.
- Ensure default configuration and caching behaviors continue to work for existing tools when adding features.

# CLAUDE.md

This file provides guidance to Claude Code when working with Python code in this repository.

## Core Development Philosophy

### KISS (Keep It Simple, Stupid)

Simplicity should be a key goal in design. Choose straightforward solutions over complex ones whenever possible. Simple solutions are easier to understand, maintain, and debug.

### YAGNI (You Aren't Gonna Need It)

Avoid building functionality on speculation. Implement features only when they are needed, not when you anticipate they might be useful in the future.

## Run the Agent

UV run agent

Always validate with ruff
"uv run ruff check --fix"
"uv run ruff check"

Always validate with pytest
"uv run pytest -v"

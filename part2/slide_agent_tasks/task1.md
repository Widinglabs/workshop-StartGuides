name: "Slide Agent Foundation - UV Script Setup"
description: |

## Context References

```yaml
REFERENCE FILE: PRPs/ai_docs/single_file_agent_example.md
  why: UV script header patterns and inline dependency management

REFERENCE FILE: PRPs/ai_docs/anthropic_api/authentication.md
  why: Environment variable security with python-dotenv patterns
```

## Goal

CREATE slide_agent.py foundation with UV script structure, dotenv environment loading, and essential imports for intelligent slide creation agent.

## What

Single-file agent with:

- UV script header with inline dependencies
- Dotenv environment loading from .env
- Rich console for delightful output
- Foundation imports for agent loop

### Success Criteria

- [ ] UV script header with correct dependencies
- [ ] Secure ANTHROPIC_API_KEY loading with load_dotenv()
- [ ] Rich console initialization
- [ ] Clean import organization
- [ ] Ready for agent loop implementation

## Implementation Blueprint

### UV Script Structure

```python
# /// script
# dependencies = [
#     "anthropic>=0.60.0",
#     "rich>=13.7.0",
#     "python-dotenv>=1.1.1",
# ]
# ///
```

### Core Imports

```python
import os
import sys
import json
import argparse
import anthropic
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

load_dotenv()
console = Console()
```

## Tasks to Complete

```yaml
Task 1 - CREATE slide_agent.py:
  - IMPLEMENT: UV script header with inline dependencies
  - IMPLEMENT: Import organization following single-file agent patterns
  - IMPLEMENT: load_dotenv() call for environment setup
  - IMPLEMENT: Rich console initialization
  - VALIDATE: uv run slide_agent.py (should show missing arguments error)

Task 2 - IMPLEMENT argparse foundation:
  - IMPLEMENT: ArgumentParser with slide creation description
  - IMPLEMENT: --prompt/-p required argument for slide request
  - IMPLEMENT: --output/-o optional argument for output directory (default: ".")
  - VALIDATE: uv run slide_agent.py --help (shows usage)
```

## Validation Gates

### Level 1: File Structure

```bash
uv run slide_agent.py --help
# Expected: Shows argparse help with --prompt and --output options
```

## Anti-Patterns to Avoid

- ❌ Don't hardcode API keys - use environment variables only
- ❌ Don't skip load_dotenv() - .env files are essential for development
- ❌ Don't use print() - Rich console for all output

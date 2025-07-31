# Coding Standards

_Workshop goal: Define the essential rules agents must follow. Keep it simple - focus on what breaks builds or causes confusion._

## File & Folder Naming

_How should files and directories be named?_

- **Files**: [snake_case / kebab-case / camelCase]
- **Directories**: [convention]
- **Test files**: [naming pattern]
- **Config files**: [naming pattern]

## Code Style Basics

_The non-negotiables for consistent code_

- **Indentation**: [spaces/tabs, how many]
- **Line length**: [max characters]
- **Quotes**: [single/double]
- **Trailing commas**: [yes/no]

## Naming Conventions

_How to name things so agents and humans understand_

- **Variables**: [convention] - Example: `user_data` or `userData`
- **Functions**: [convention] - Example: `get_user()` or `getUser()`
- **Classes**: [convention] - Example: `UserManager`
- **Constants**: [convention] - Example: `MAX_USERS`

## Function/Method Standards

_Rules for writing functions_

- **Max parameters**: [number]
- **Return types**: [always explicit / when needed]
- **Documentation**: [docstring format]

```python
# Example function format:
def example_function(param1: str, param2: int) -> bool:
    """[Required documentation format]"""
    pass
```

## Import Organization

_How to organize imports - agents get this wrong often_

```python
# Order:
# 1. [Standard library]
# 2. [Third-party]
# 3. [Local imports]
```

## Error Handling

_Standard approach to errors_

- **Exceptions**: [when to catch vs raise]
- **Error messages**: [format/style]
- **Logging**: [what to log, how]

## Comments & Documentation

_When and how to document_

- **Inline comments**: [when needed]
- **Docstrings**: [required for what]
- **TODOs**: [format: TODO: description]

## Code Organization

_How to structure code within files_

- **Class order**: [properties, methods, etc.]
- **Function order**: [public first, private last]
- **Grouping**: [related functions together]

## What NOT to Do

_Common mistakes that break things_

- L
- L
- L

## Tools & Automation

_What tools enforce these standards_

- **Linter**: [tool name + config location]
- **Formatter**: [tool name + config location]
- **Pre-commit**: [yes/no + what it checks]

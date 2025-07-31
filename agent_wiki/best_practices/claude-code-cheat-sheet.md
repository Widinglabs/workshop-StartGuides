# Claude Code Cheat Sheet

## Quick Start

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Start in any project
cd your-project
claude

# Initialize project memory
/init
```

## Essential Commands

| Command              | Description               |
| -------------------- | ------------------------- |
| `claude`             | Start interactive session |
| `claude -p "prompt"` | Headless mode (scripting) |
| `claude --help`      | Show help                 |
| `claude config list` | Show configuration        |

## Keyboard Shortcuts

### Interactive Mode

| Shortcut        | Action                                     |
| --------------- | ------------------------------------------ |
| `Ctrl+C`        | Cancel input/generation                    |
| `Ctrl+D`        | Exit session                               |
| `Ctrl+L`        | Clear terminal screen                      |
| `Escape`        | Interrupt Claude mid-action                |
| `Double Escape` | Jump back in history, edit previous prompt |
| `Shift+Tab`     | Toggle auto-accept mode                    |
| `↑/↓`           | Navigate command history                   |

### Input Methods

| Shortcut       | Action                                    |
| -------------- | ----------------------------------------- |
| `#`            | Quick add to memory (CLAUDE.md)           |
| `/`            | Invoke slash commands                     |
| `@`            | Reference files/directories               |
| `\` + `Enter`  | Multiline input (universal)               |
| `Option+Enter` | Multiline input (macOS)                   |
| `Shift+Enter`  | Multiline input (after `/terminal-setup`) |

## Memory Management (CLAUDE.md)

### File Locations (Priority Order)

1. `./CLAUDE.md` - Project root (team shared)
2. `./subdir/CLAUDE.md` - Subdirectory specific
3. `~/.claude/CLAUDE.md` - User global

### Quick Memory Commands

```bash
# Add to memory
# Start input with # and follow prompts

# Edit memory directly
/memory

# Initialize project memory
/init
```

### Memory File Imports

```markdown
<!-- In CLAUDE.md -->

@path/to/other/memory.md

<!-- Recursive imports supported (max 5 hops) -->
```

## Slash Commands

### Built-in Commands

| Command        | Description               |
| -------------- | ------------------------- |
| `/help`        | Show help                 |
| `/clear`       | Clear context window      |
| `/memory`      | Edit memory files         |
| `/init`        | Initialize project memory |
| `/permissions` | Manage tool permissions   |
| `/model`       | Switch model              |
| `/vim`         | Enable vim mode           |
| `/review`      | Review a PR               |

### Custom Commands

```bash
# Create custom command
echo "Your command template with $ARGUMENTS" > .claude/commands/mycmd.md

# Use custom command
/project:mycmd argument1 argument2
```

## Common Workflow Patterns

### 1. Prime the model with context

```
1. create a /command guiding the model through exploring the codebase and understanding its structure.

Example:
/project:explore-codebase

"Read README.md, THEN run git ls-files | grep -v -f (sed 's|^|^|; s|$|/|' .cursorignore | psub) to understand the context of the project"
```

### 2. Explore → Plan → Code → Commit

```
1. "Read the codebase and understand how [feature] works"
2. "Think hard and make a plan for implementing [feature]"
3. "Implement the plan step by step"
4. "Run tests and commit the changes"
```

### 3. Test-Driven Development

```
1. "Write tests first for [functionality] - don't implement yet"
2. "Commit the failing tests"
3. "Now implement code to make tests pass"
4. "Commit the implementation"
```

### 4. Visual Iteration (playwright mcp for validation)

```
1. Provide screenshot/mockup
2. "Implement this design and take a screenshot"
3. "Iterate until it matches the mockup"
4. "Commit when satisfied"
```

## Permission Management

### Quick Permission Commands

````bash
# Allow specific tools
/permissions add Edit
/permissions add Bash(git commit:*)

# Allow MCP server
/permissions add mcp__server__tool_name

# View current permissions
/permissions list

# CLI override (session only)
claude --allowedTools Edit,Bash


### Permission Levels

1. Enterprise policies (highest)
2. Command line arguments
3. Local project settings
4. Shared project settings
5. User settings (lowest)

## MCP Integration

### Add MCP Server

```bash
claude mcp add server-name --transport stdio --command "path/to/server"
````

For teams commit a .mcp.json file to version control to share MCP servers with the team.

### Reference MCP Resources

```
@server-name://resource-path
```

### MCP Configuration Scopes

- **Local**: `.mcp.json` (project, checked in)
- **Project**: Project-specific servers
- **User**: Personal servers across all projects

## Context Optimization

### Best Practices

- Use `/clear` frequently between tasks
- Be specific in instructions
- Provide visual context when possible
- Use `@file.py` to reference specific files
- Leverage tab-completion for file paths

### Thinking Modes

| Command        | Thinking Budget |
| -------------- | --------------- |
| "think"        | Basic           |
| "think hard"   | Medium          |
| "think harder" | High            |
| "ultrathink"   | Maximum         |

## Multi-Claude Patterns

### Parallel Development

```bash
# Terminal 1: Main development
claude

# Terminal 2: Testing/review
claude

# Terminal 3: Documentation
claude
```

### Git Worktrees

```bash
# Create worktree
git worktree add ../project-feature-a feature-a

# Start Claude in worktree
cd ../project-feature-a && claude

# Clean up
git worktree remove ../project-feature-a
```

## Data Input Methods

| Method         | Example                    |
| -------------- | -------------------------- |
| Copy/paste     | Paste directly into prompt |
| Pipe input     | `cat file.txt \| claude`   |
| File reference | `@path/to/file.py`         |
| URL fetch      | Paste URL in prompt        |
| Image input    | Paste image                |

### Debug Flags

```bash
claude --verbose          # Verbose output
claude --mcp-debug       # MCP debugging
claude --dangerously-skip-permissions  # Skip all permissions
```

## Configuration Files

### Locations

- `~/.claude/settings.json` - User settings
- `.claude/settings.json` - Project settings (local)
- `settings.json` - Project settings (shared)

## Quick Tips

- **Start simple**: Begin with codebase Q&A, then add complexity
- **Be specific**: "Add error handling for null user inputs" vs "add error handling"
- **Use images and mermaid diagrams**: Screenshots, and mermaid diagrams dramatically improve results
- **Iterate and validate**: Let Claude see its output and improve (2-3 iterations optimal) let claude close its own feedback loop
- **Trust the model**: Don't over-engineer; Claude handles complexity well
- **Course correct early**: Use Escape to interrupt and redirect
- **Multi-agent patterns**: One writes, one reviews, one tests

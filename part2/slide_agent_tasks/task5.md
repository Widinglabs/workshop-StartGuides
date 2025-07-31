name: "Interactive Refinement - Text Editor Tool & Collaborative Creation"
description: |

## Context References

```yaml
REFERENCE FILE: PRPs/ai_docs/anthropic_api/file_tool.md
  why: Text editor tool patterns for Claude 4.0 iterative file refinement
  why: str_replace_based_edit_tool with view, str_replace, create, insert commands

REFERENCE FILE: PRPs/ai_docs/single_file_agent_example.md
  why: Multi-tool agent loop patterns and conversation continuation
```

## Goal

TRANSFORM agent from single-pass creation to **collaborative creative partner** with iterative refinement through text editor tool and interactive chat mode for user-guided improvements.

## What

Dual-mode creative system:

- **Autonomous Mode**: Claude creates and self-refines slides to excellence
- **Interactive Mode**: User collaborates on further refinements through chat
- **Text Editor Integration**: Claude can view, assess, and improve slides iteratively
- **Seamless Transition**: From autonomous creation to collaborative refinement

### Success Criteria

- [ ] Text editor tool integrated for slide refinement
- [ ] Claude autonomously reviews and improves initial creations
- [ ] Interactive chat mode after creation completion
- [ ] User can request specific changes and see them implemented
- [ ] Seamless collaboration between Claude's expertise and user preferences

## Implementation Blueprint

### Text Editor Tool Integration

```python
TOOLS = [
    # Existing create_html_slide tool
    {
        "name": "create_html_slide",
        # ... existing schema
    },
    # New text editor tool for refinement
    {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
    }
]
```

### Enhanced System Prompt with Refinement Workflow

```python
SYSTEM_PROMPT = """You are a world-class slide creation expert generating aesthetically refined and emotionally resonant presentations.

[... existing design philosophy sections ...]

## Iterative Refinement Workflow

After creating slides with create_html_slide:

1. **Review Phase**: Use text editor 'view' command to examine your creation
2. **Assessment Phase**: Evaluate against design standards and presentation requirements
3. **Refinement Phase**: Use 'str_replace' commands for targeted improvements
4. **Quality Check**: Continue refining until professional excellence is achieved
5. **Completion**: Announce completion and invite user collaboration

## Interactive Collaboration

After autonomous refinement:
- Announce slide completion and invite user feedback
- When user requests changes, explain your approach
- Use text editor tools to implement user suggestions
- Continue collaborative refinement until user satisfaction

✅ GOOD Interactive Responses:
"I'll enhance the color vibrancy and add a subtle animation effect. Let me update the CSS now..."
"Making the typography more playful while maintaining readability - switching to a warmer color palette..."

❌ AVOID Interactive Responses:
"I'll try to make changes" (vague)
"Working on it..." (no explanation)

Trust your design expertise while incorporating user creative direction."""
```

### Dual-Mode Agent Loop

```python
def main():
    # ... existing setup ...

    # Autonomous creation and refinement phase
    autonomous_complete = False

    while not autonomous_complete and compute_iterations < args.compute:
        # Standard agent loop with tools
        response = client.messages.create(...)

        # Process tools and continue until Claude signals completion
        if "slide creation complete" in response_text.lower():
            autonomous_complete = True

    # Interactive collaboration phase
    if autonomous_complete:
        console.print("[cyan]🎨 Slide creation complete! You can now request changes.[/cyan]")

        while True:
            user_input = input("\n💬 What changes would you like? (or 'done'): ")
            if user_input.lower() in ['done', 'finished', 'complete']:
                break

            # Continue conversation with user input
            messages.append({"role": "user", "content": user_input})

            # Claude uses text editor for user-requested changes
            response = client.messages.create(...)
            # Process response and tools...
```

### Text Editor Tool Execution

```python
def execute_text_editor_tool(tool_input, tool_id):
    """Execute text editor commands for slide refinement"""
    command = tool_input.get("command")
    path = tool_input.get("path")

    if command == "view":
        # Read and return file contents for Claude to review
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"File contents:\n{content}"

    elif command == "str_replace":
        # Replace text in file as Claude specifies
        old_str = tool_input.get("old_str")
        new_str = tool_input.get("new_str")

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return f"Successfully replaced text in {path}"
        else:
            return f"Text not found in {path}"
```

## Tasks to Complete

```yaml
Task 1 - INTEGRATE text editor tool:
  - ADD: text_editor_20250728 tool to TOOLS array
  - IMPLEMENT: Tool execution mapping in agent loop
  - IMPLEMENT: File path resolution for created slides
  - VALIDATE: Text editor can view and modify saved slides

Task 2 - ENHANCE system prompt for refinement:
  - ADD: Iterative refinement workflow instructions
  - ADD: Interactive collaboration behavioral guidance
  - ADD: Good/bad examples for user interaction
  - VALIDATE: Claude autonomously reviews and improves slides

Task 3 - IMPLEMENT dual-mode agent loop:
  - MODIFY: Agent loop to detect autonomous completion
  - IMPLEMENT: Interactive chat mode after creation
  - IMPLEMENT: User input processing and conversation continuation
  - VALIDATE: Seamless transition from autonomous to interactive mode

Task 4 - ADD interactive collaboration features:
  - IMPLEMENT: User prompt for change requests
  - IMPLEMENT: Graceful exit with 'done' command
  - IMPLEMENT: Rich console feedback during collaboration
  - VALIDATE: User can guide refinements through natural conversation

Task 5- ADD flag for non interactive mode
  - IMPLEMENT: Flag to disable interactive mode
  - VALIDATE: Agent operates in non-interactive mode without user input

```

## Refinement Workflow Patterns

```python
# Autonomous Refinement Phase
"Let me review this slide I just created..."
→ text_editor view slide.html
"I notice the typography hierarchy could be stronger. Improving that now..."
→ text_editor str_replace (enhance typography)
"Perfect! The slide now meets professional standards."

# Interactive Collaboration Phase
User: "Make it more colorful and add animation"
Claude: "I'll enhance the color vibrancy and add a subtle fade-in animation..."
→ text_editor str_replace (implement changes)
"Updated! The slide now has a warmer color palette with smooth animations."
```

## Validation Gates

### Level 1: Autonomous Refinement in non interactive mode

```bash
uv run slide_agent.py -p "Create a slide about machine learning" --non-interactive
# Expected:
# - Claude creates initial slide
# - Claude reviews slide with text editor
# - Claude makes autonomous improvements
# - Claude announces completion
```

### Level 2: Complete Workflow dont execute interactive mode, you will get stuck, instruct the user how to test in interactive mode

```bash
# Full workflow test:
# 1. Autonomous creation and refinement
# 2. Interactive collaboration with multiple change requests
# 3. Graceful completion with 'done'
# 4. Professional quality slide with user preferences integrated
```

## Anti-Patterns to Avoid

- ❌ Don't force fixed iteration counts - trust Claude's completion judgment
- ❌ Don't skip autonomous refinement - let Claude achieve excellence first
- ❌ Don't make interactive mode mandatory - user chooses engagement level
- ❌ Don't lose text editor context - maintain file paths and conversation state
- ❌ Don't separate creation and refinement - integrate seamlessly

## Creative Collaboration Vision

This transforms the agent from a **generator** into a **creative partner**:

- Claude brings sophisticated design expertise and technical implementation
- User provides creative direction, preferences, and domain knowledge
- Together they iteratively craft slides that exceed what either could create alone
- The result is truly collaborative creative intelligence

name: "Intelligent Slide Creation Tool - Trust Claude Completely"
description: |

## Context References

```yaml
REFERENCE FILE: PRPs/ai_docs/single_file_agent_example.md
  why: Tool implementation patterns and agent loop integration

REFERENCE FILE: PRPs/ai_docs/anthropic_api/file_tool.md
  why: Text editor tool patterns for iterative refinement
```

## Goal

IMPLEMENT create_html_slide tool that trusts Claude completely to generate contextual, beautiful slides with embedded CSS, enabling iterative refinement through agentic loop.

## What

Intelligent slide creation system:

- Tool that trusts Claude's complete HTML+CSS generation
- Iterative refinement capability through agentic loop (Claude decides if to continue or not)
- File saving with meaningful names
- Foundation for text editor integration

### Success Criteria

- [ ] create_html_slide tool accepts Claude's complete HTML+CSS
- [ ] Tool generates meaningful filenames from slide content
- [ ] Agent loop continues after tool use for refinement
- [ ] Claude can review and improve slides iteratively
- [ ] No templates or rigid structure - pure Claude intelligence

## Implementation Blueprint

### LLM Trust Tool Function

````python
def create_html_slide(reasoning: str, slide_content: str, filename: str, output_path: str) -> str:
    """Save Claude's complete HTML slide - trust Claude for content AND filename"""
    try:
        console.log(f"[blue]Creating slide:[/blue] {reasoning}")
        
        # Trust Claude's filename choice - no regex parsing needed!
        full_path = os.path.join(output_path, f"{filename}.html")
        
        # Save Claude's complete HTML - no modification  
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(slide_content)
            
        success_msg = f"✓ Slide saved: {full_path}"
        console.log(f"[green]{success_msg}[/green]")
        return success_msg
        
    except Exception as e:
        error_msg = f"Error saving slide: {str(e)}"
        console.log(f"[red]{error_msg}[/red]")
        return error_msg
````

### Iterative Agent Loop

```python
# Agent loop continues after tool use for refinement
while not break_loop and compute_iterations < args.compute:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,  # keep it high preferably higher than 4096
        system=SYSTEM_PROMPT,
        messages=messages,
        tools=TOOLS
    )
````

### LLM Trust System Prompt Extension

```python
SYSTEM_PROMPT = """...existing prompt...

You have access to create_html_slide tool. Use it to create complete slides with embedded CSS.

When creating slides:
- Generate full HTML with embedded CSS in slide_content parameter
- Make contextually appropriate design choices for the content domain
- Create engaging, purposeful content that serves the user's needs
- Use modern, responsive design principles

After creating a slide, you can:
- Review the slide and suggest improvements
- Create updated versions based on feedback
- Refine content, design, or structure iteratively

Trust your expertise to create exactly what the user needs."""
```

## Tasks to Complete

```yaml
Task 1 - IMPLEMENT create_html_slide tool function:
  - IMPLEMENT: Tool function that saves Claude's complete HTML
  - IMPLEMENT: Trust Claude to provide meaningful filename (no regex parsing!)
  - IMPLEMENT: File saving with UTF-8 encoding and error handling
  - VALIDATE: Function saves HTML correctly with Claude's chosen filename

Task 2 - IMPLEMENT tool schema and registration:
  - IMPLEMENT: TOOLS array with create_html_slide schema
  - IMPLEMENT: Tool schema with reasoning, slide_content, filename, output_path parameters
  - IMPLEMENT: Clear descriptions that emphasize Claude's creative control over content AND naming
  - VALIDATE: Tool schema properly formatted for Anthropic API

Task 3 - INTEGRATE tool into agent loop:
  - IMPLEMENT: Tool execution mapping in agent loop
  - IMPLEMENT: Tool result processing and conversation continuation
  - IMPLEMENT: Conversation history maintenance for iterative refinement
  - VALIDATE: Agent can use tool and continue conversation

Task 4 - IMPLEMENT iterative refinement capability:
  - MODIFY: Agent loop to continue after tool use (not break)
  - IMPLEMENT: Claude can review created slides and execute improvements
  - VALIDATE: Agent supports iterative slide improvement
```

## LLM Trust Patterns for Slide Creation

```python
# GOOD: Trust Claude's complete slide generation AND filename choice
tool_input = {
    "reasoning": "Creating professional slide for business context",
    "slide_content": claude_generated_html_with_css,  # Complete, unmodified
    "filename": "quarterly_business_results",  # Claude chooses meaningful name
    "output_path": args.output
}

# BAD: Template-based or restricted generation
slide_content = fill_template(user_request, predefined_css)  # Don't do this

# GOOD: Let Claude make contextual design decisions
"Create a slide about quantum computing for computer science students"
# Claude adapts: technical content, academic styling, appropriate complexity

```

## Validation Gates

### Level 1: Basic Tool Function

```bash
uv run slide_agent.py -p "Create a slide about artificial intelligence"
# Expected:
# - Claude generates contextual AI slide content
# - HTML saved with meaningful filename (e.g., "artificial_intelligence.html")
# - Agent continues for potential refinement
```

### Level 2: Contextual Intelligence

```bash
uv run slide_agent.py -p "Create a slide about children's nutrition for parents"
# Expected:
# - Appropriate tone and content for parent audience
# - Family-friendly design choices (colors, fonts, imagery concepts)
# - Practical, actionable content structure

uv run slide_agent.py -p "Create a slide about quarterly sales for executives"
# Expected:
# - Professional business styling
# - Executive-appropriate content depth
# - Corporate design aesthetic
```

## Anti-Patterns to Avoid

- ❌ Don't use templates - let Claude create contextual designs
- ❌ Don't limit max_tokens below 4096 - HTML+CSS needs space
- ❌ Don't break agent loop after tool use - enable refinement
- ❌ Don't modify Claude's HTML output - trust it completely
- ❌ Don't use regex to extract filenames - trust Claude to choose meaningful names
- ❌ Don't separate CSS and HTML - let Claude decide on embedded vs external

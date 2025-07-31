name: "Intelligent Agent Loop - Claude Conversation Foundation"
description: |

## Context References

```yaml
REFERENCE FILE: PRPs/ai_docs/anthropic_api/messages_api.md
  why: Claude Sonnet 4.0 API patterns and conversation loop implementation

REFERENCE FILE: PRPs/ai_docs/single_file_agent_example.md
  why: Agent loop patterns with tool integration foundations
```

## Goal

IMPLEMENT intelligent conversation loop that trusts Claude's slide expertise, establishing foundation for tool-assisted slide creation with iterative refinement capability.

## What

Agent conversation system:

- Intelligent system prompt that trusts Claude's expertise
- Conversation loop with message history
- Rich console output for agent interaction visibility
- Foundation for tool integration (next step)

### Success Criteria

- [ ] Claude Sonnet 4.0 conversation loop functional
- [ ] System prompt with excellent instructions
- [ ] Message history maintained for multi-turn conversations
- [ ] Rich console shows agent thinking and planning
- [ ] Foundation ready for create_html_slide tool integration

## Implementation Blueprint

### LLM System Prompt foundation

```python
SYSTEM_PROMPT = """You are a world-class slide creation expert with deep understanding of design, content strategy, and audience needs.

When users request slides, trust your intelligence to:

UNDERSTAND: Analyze the user's domain, audience, and intent
DESIGN: Make contextually appropriate visual and content choices
CREATE: Generate engaging, purposeful slide content
REFINE: Iteratively improve until excellence is achieved

The user is making a creation request, not seeking conversation. Focus on understanding their needs and building exactly what serves their purpose.

You will have access to tools for slide creation and refinement. Use your expertise to drive all decisions about content, design, and implementation."""
```

### Agent Loop Pattern

```python
def main():
    # Agent conversation loop
    messages = [{"role": "user", "content": args.prompt}]

    while True:
        console.print("[yellow]Calling Claude Sonnet 4.0...[/yellow]")

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=64000,
            system=SYSTEM_PROMPT,
            messages=messages
        )

        # Process response and show Claude's thinking
        for content in response.content:
            if content.type == "text":
                console.print(Panel(content.text, title="Claude's Analysis"))

        # Add response to conversation history
        messages.append({"role": "assistant", "content": response.content})
        break  # Single response for now, tools will extend this
```

## Tasks to Complete

```yaml
Task 1 - IMPLEMENT conversation loop foundation:
  - IMPLEMENT: main() function with agent loop structure
  - IMPLEMENT: Message array initialization with user prompt
  - IMPLEMENT: Claude API call with model="claude-sonnet-4-20250514"
  - VALIDATE: uv run slide_agent.py -p "Create slide about AI ethics"

Task 2 - IMPLEMENT intelligent system prompt:
  - IMPLEMENT: System prompt that trusts Claude's slide expertise
  - IMPLEMENT: Emphasis on understanding user intent and context
  - IMPLEMENT: Clear instruction that user wants creation, not chat
  - VALIDATE: Response shows contextual understanding (AI ethics = serious tone)

Task 3 - IMPLEMENT rich console output:
  - IMPLEMENT: Panel display for Claude's response
  - IMPLEMENT: User prompt display with styling
  - IMPLEMENT: Agent loop iteration indicators
  - VALIDATE: Beautiful console output with clear conversation flow

Task 4 - IMPLEMENT conversation history:
  - IMPLEMENT: Message history array maintenance
  - IMPLEMENT: Response appending for multi-turn capability
  - IMPLEMENT: Foundation for tool integration in task 3
  - VALIDATE: Conversation state ready for tool extension
```

## LLM Trust Patterns

```python
# GOOD: Trust Claude's intelligence and expertise
system_prompt = "You are a slide expert. Use your intelligence to..."

# GOOD: Let Claude understand context and make decisions
messages = [{"role": "user", "content": user_request}]  # Full request

# BAD: Pre-processing or limiting Claude's input
messages = [{"role": "user", "content": f"Create template for: {category}"}]
```

## Validation Gates

### Level 1: Basic Conversation

```bash
uv run slide_agent.py -p "Create a slide about sustainable energy"
# Expected: Claude shows understanding of sustainability context, suggests appropriate content/design approach
```

### Level 2: Contextual Intelligence

```bash
uv run slide_agent.py -p "Create a slide about quarterly financial results [results]"
# Expected: Claude adapts to business context, suggests professional design approach

uv run slide_agent.py -p "Create a slide about dinosaurs for kids"
# Expected: Claude adapts to educational/child context, suggests engaging visual approach
```

### Level 3: Rich Console Output

```bash
# Expected: Beautiful formatted output with:
# - User prompt display
# - Claude's analysis in styled panel
# - Clear conversation flow indicators
```

## Anti-Patterns to Avoid

- ❌ Don't create rigid templates - trust Claude's contextual intelligence
- ❌ Don't pre-process user requests - send full context to Claude
- ❌ Don't skip message history - foundation for tool integration needed

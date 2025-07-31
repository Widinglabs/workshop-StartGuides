## Intent

Build a single-file UV script agent that creates slides using gamma.app patterns. The agent should loop until it successfully creates a single slide based on user request, using Claude Sonnet 4.0 for reasoning and tool orchestration.

## Context References

REFERENCE FILE: PRPs/ai_docs/single_file_agent_example.md
- UV script header pattern with inline dependencies
- Tool-based architecture with reasoning parameters
- Agent loop structure with compute limits and conversation state
- Thinking integration pattern with Claude

REFERENCE FILE: PRPs/ai_docs/anthropic_api/messages_api.md
- Claude Sonnet 4.0 model: "claude-sonnet-4-20250514"
- Messages API request structure with tools parameter
- Multi-turn conversation handling with message history
- Tool use capabilities for function calling

REFERENCE FILE: PRPs/ai_docs/anthropic_api/authentication.md
- ANTHROPIC_API_KEY environment variable for secure key storage
- Avoid hardcoding API keys in source code
- Use python-dotenv for environment variable loading

REFERENCE FILE: PRPs/ai_docs/anthropic_api/quickstart.md
- client = anthropic.Anthropic(api_key=api_key) initialization pattern
- messages.create() with model, max_tokens, messages parameters
- Process response.content for tool_use and text blocks

## Tasks

CREATE gamma_slide_agent.py:

- ADD: UV script header with dependencies:
  - anthropic>=0.60.0
  - rich>=13.7.0
  - pydantic>=2.11.7
  - python-dotenv>=1.1.1
- ADD: Import statements: os, sys, json, argparse, time
- ADD: Import anthropic, Rich Console, Panel
- ADD: Import python-dotenv load_dotenv
- VALIDATE: uv run --help | grep "script"

CREATE research_topic tool:

- IMPLEMENT: research_topic(reasoning: str, topic: str) -> str function
- IMPLEMENT: Synthesize comprehensive knowledge about the slide topic
- IMPLEMENT: Return structured research content with key points, audience considerations, and main messages
- ADD: Rich console logging with reasoning display
- ADD: Error handling with graceful fallback to basic topic summary
- VALIDATE: python -c "from gamma_slide_agent import research_topic; print(research_topic('Understanding topic', 'Python basics'))"

CREATE create_slide_outline tool:

- IMPLEMENT: create_slide_outline(reasoning: str, topic: str, content: str) -> dict function
- IMPLEMENT: Structure slide with title, subtitle, main points (3-5 bullet points), layout suggestions
- IMPLEMENT: Return dict with keys: title, subtitle, main_points, layout_type, visual_suggestions
- ADD: Rich console logging with reasoning display
- ADD: Error handling with basic outline fallback
- VALIDATE: python -c "from gamma_slide_agent import create_slide_outline; result = create_slide_outline('Creating structure', 'Python', 'content'); print('title' in result)"

CREATE generate_slide_content tool:

- IMPLEMENT: generate_slide_content(reasoning: str, outline: dict) -> dict function
- IMPLEMENT: Transform outline into final slide content with formatted text, visual descriptions, color scheme
- IMPLEMENT: Return dict with keys: final_title, final_content, visuals, formatting, gamma_style_notes
- ADD: Rich console logging with reasoning display
- ADD: Error handling with basic content generation fallback
- VALIDATE: python -c "from gamma_slide_agent import generate_slide_content; result = generate_slide_content('Finalizing content', {'title': 'Test'}); print('final_title' in result)"

CREATE finalize_slide tool:

- IMPLEMENT: finalize_slide(reasoning: str, slide_content: dict) -> str function
- IMPLEMENT: Output complete slide as formatted string with title, content, visual directions
- IMPLEMENT: Display slide preview using Rich Panel
- IMPLEMENT: Set break_loop=True to terminate agent loop
- ADD: Rich console logging with completion message
- VALIDATE: python -c "from gamma_slide_agent import finalize_slide; result = finalize_slide('Completing slide', {'final_title': 'Test'}); print(len(result) > 0)"

CREATE TOOLS schema array:

- IMPLEMENT: TOOLS list with 4 tool definitions matching Anthropic tool schema format
- ADD: research_topic schema with reasoning and topic parameters
- ADD: create_slide_outline schema with reasoning, topic, content parameters  
- ADD: generate_slide_content schema with reasoning and outline parameters
- ADD: finalize_slide schema with reasoning and slide_content parameters
- VALIDATE: python -c "from gamma_slide_agent import TOOLS; print(len(TOOLS) == 4)"

CREATE agent main loop:

- IMPLEMENT: argparse with --prompt/-p (required) and --compute/-c (default: 10)
- IMPLEMENT: Load ANTHROPIC_API_KEY from environment using load_dotenv()
- IMPLEMENT: Initialize Rich console for logging
- IMPLEMENT: Anthropic client initialization with error handling for missing API key
- IMPLEMENT: System prompt with slide creation expert persona and tool workflow
- IMPLEMENT: Message history initialization with user prompt
- VALIDATE: python -c "from gamma_slide_agent import main; print('OK')"

CREATE agent execution loop:

- IMPLEMENT: While loop with compute_iterations counter and break_loop control
- IMPLEMENT: client.messages.create() call with:
  - model="claude-sonnet-4-20250514"
  - max_tokens=4096
  - tools=TOOLS
  - messages=conversation_history
- IMPLEMENT: Response content processing for thinking, tool_use, text blocks
- IMPLEMENT: Dynamic tool execution mapping (if tool_name == "research_topic": result = research_topic(...))
- IMPLEMENT: Conversation state management - append assistant and user messages
- ADD: Error handling for tool failures with error message passed back to agent
- ADD: Rich console output for each iteration with tool call details
- VALIDATE: uv run gamma_slide_agent.py --prompt "test slide" (should not error on basic execution)

CREATE system prompt template:

- ADD: Expert slide creation persona: "You are a world-class slide creation expert"
- ADD: Gamma.app style guidance for clean, modern presentation design
- ADD: Tool workflow instructions: research -> outline -> content -> finalize sequence
- ADD: Template variable {{user_prompt}} for dynamic user request insertion
- ADD: Clear success criteria: create exactly one slide and call finalize_slide to complete
- VALIDATE: Check system prompt contains all 4 tool names and workflow sequence

## Validation

VALIDATE: uv run gamma_slide_agent.py --prompt "Create a slide about Python data science tools"
- Script executes without errors
- Agent loops through research -> outline -> content -> finalize sequence
- Each tool displays reasoning and results via Rich console
- Outputs complete formatted slide content
- Terminates successfully with completed slide

VALIDATE: uv run gamma_slide_agent.py -p "Make a slide explaining API design principles" -c 5
- Accepts short flags and compute limit parameter
- Respects maximum iteration limit
- Shows rich console feedback throughout process
- Handles tool errors gracefully with agent self-correction
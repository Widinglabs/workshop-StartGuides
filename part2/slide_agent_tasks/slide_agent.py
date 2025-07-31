# /// script
# dependencies = [
#     "anthropic>=0.60.0",
#     "rich>=13.7.0",
#     "python-dotenv>=1.1.1",
# ]
# ///

import argparse
import json
import os
import sys

import anthropic
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()


def execute_text_editor_tool(tool_input, tool_id, last_created_file):
    """Execute text editor commands for slide refinement"""
    command = tool_input.get("command")
    path = tool_input.get("path", last_created_file)  # Use last created file as default

    try:
        if command == "view":
            # Read and return file contents for Claude to review
            if not os.path.exists(path):
                return f"File not found: {path}"

            with open(path, encoding="utf-8") as f:
                content = f.read()

            console.print(f"[blue]📖 Viewing file: {path}[/blue]")
            return f"File contents of {path}:\n{content}"

        elif command == "str_replace":
            # Replace text in file as Claude specifies
            old_str = tool_input.get("old_str", "")
            new_str = tool_input.get("new_str", "")

            if not os.path.exists(path):
                return f"File not found: {path}"

            with open(path, encoding="utf-8") as f:
                content = f.read()

            if old_str in content:
                new_content = content.replace(old_str, new_str, 1)  # Replace only first occurrence
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                console.print(f"[green]✏️ Updated file: {path}[/green]")
                return f"Successfully replaced text in {path}"
            else:
                return f"Text not found in {path}. Cannot perform replacement."

        elif command == "create":
            # Create new file
            file_text = tool_input.get("file_text", "")

            # Ensure directory exists
            os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)

            with open(path, "w", encoding="utf-8") as f:
                f.write(file_text)

            console.print(f"[green]📄 Created file: {path}[/green]")
            return f"Successfully created file: {path}"

        else:
            return f"Unknown text editor command: {command}"

    except Exception as e:
        error_msg = f"Error executing text editor command '{command}': {str(e)}"
        console.print(f"[red]❌ {error_msg}[/red]")
        return error_msg


def create_html_slide(reasoning: str, slide_content: str, filename: str, output_path: str) -> str:
    """Save Claude's complete HTML slide - trust Claude for content AND filename"""
    try:
        console.print(f"[blue]Creating slide:[/blue] {reasoning}")

        # Trust Claude's filename choice - no regex parsing needed!
        # Ensure filename doesn't already have .html extension
        if not filename.endswith(".html"):
            full_path = os.path.join(output_path, f"{filename}.html")
        else:
            full_path = os.path.join(output_path, filename)

        # Ensure output directory exists
        os.makedirs(output_path, exist_ok=True)

        # Save Claude's complete HTML - no modification
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(slide_content)

        success_msg = f"✓ Slide saved: {full_path}"
        console.print(f"[green]{success_msg}[/green]")
        return success_msg

    except Exception as e:
        error_msg = f"Error saving slide: {str(e)}"
        console.print(f"[red]{error_msg}[/red]")
        return error_msg


TOOLS = [
    {
        "name": "create_html_slide",
        "description": "Create aesthetically refined and emotionally resonant HTML slides with embedded CSS. Apply sophisticated design principles and contextual intelligence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "reasoning": {
                    "type": "string",
                    "description": "Your design reasoning including typography, color, and aesthetic choices",
                },
                "slide_content": {
                    "type": "string",
                    "description": "Complete HTML with embedded CSS demonstrating design excellence",
                },
                "filename": {
                    "type": "string",
                    "description": "Meaningful filename reflecting the slide's purpose and content",
                },
                "output_path": {"type": "string", "description": "Directory path for slide output"},
            },
            "required": ["reasoning", "slide_content", "filename", "output_path"],
        },
    },
    {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
]

SYSTEM_PROMPT = """You are a world-class slide creation expert generating aesthetically refined and emotionally resonant presentations.

## Design Philosophy

### Foundational Principles
- **Content-First Design**: Every design decision should serve and enhance the content's message
- **Intentional Simplicity**: Embrace elegant restraint - every element should have a clear purpose
- **Emotional Resonance**: Create slides that connect with the audience beyond mere information transfer
- **Professional Excellence**: Maintain standards that reflect expertise and attention to detail

### Typographic Excellence
- **Purposeful Typography**: Typography is a core design element, not an afterthought
- **Typographic Hierarchy**: Create clear visual distinction between information levels
- **Limited Font Selection**: Use 2-3 maximum typefaces that emphasize legibility
- **Type Scale Harmony**: Establish mathematical relationships between text sizes (golden ratio, major third)
- **Breathing Room**: Allow generous spacing - line height 1.5x font size minimum

### Aesthetic Refinement
- **Visual Hierarchy**: Guide viewer attention through purposeful contrast and spacing
- **Color Psychology**: Choose colors that enhance the content's emotional tone
- **Spatial Awareness**: Use whitespace as a design element, not empty space
- **Micro-Interactions**: Add subtle details that reward attention

### Presentation Frame Standards
- **Slide Dimensions**: Use standard 16:9 aspect ratio (1920x1080px or 1366x768px)
- **Safe Areas**: Maintain 80-120px margins on all sides for projection safety
- **Consistent Layout**: Establish header, content, and footer zones across all slides
- **Responsive Scaling**: Design for both large displays and laptop screens
- **Grid System**: Use consistent spacing units (8px, 16px, 24px, 32px grid)

## Behavioral Excellence

✅ GOOD Examples:
"Creating a professional slide for quantum computing - using technical blues and precise typography"
"Building engaging children's nutrition content - bright, friendly colors with playful but readable fonts"
"Designing executive summary - clean corporate aesthetic with data-focused layout"

❌ AVOID:
"I'll create a basic slide template for you"
"Let me make a simple layout with some text"
"I'll add some colors and fonts"

You have access to create_html_slide and str_replace_based_edit_tool. Generate complete HTML with embedded CSS that demonstrates:
- Standard 16:9 presentation frame (1920x1080px or 1366x768px with safe margins)
- Contextually appropriate design choices for the content domain
- Professional typography and color theory application
- Modern, responsive design principles with consistent grid system
- Purposeful visual hierarchy and spacing within presentation constraints

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

CRITICAL: Always create slides with presentation-ready dimensions and consistent layout framework that works across different display sizes.

Trust your design expertise while incorporating user creative direction."""


def main():
    parser = argparse.ArgumentParser(description="Intelligent slide creation agent using Claude")
    parser.add_argument("--prompt", "-p", required=True, help="Slide creation request prompt")
    parser.add_argument(
        "--output",
        "-o",
        default=".",
        help="Output directory for generated slides (default: current directory)",
    )
    parser.add_argument(
        "--compute",
        "-c",
        type=int,
        default=10,
        help="Maximum number of agent iterations (default: 10)",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Disable interactive mode after autonomous creation",
    )

    args = parser.parse_args()

    console.print(
        Panel(
            f"[bold green]Slide Agent Initialized[/bold green]\n"
            f"Prompt: {args.prompt}\n"
            f"Output: {args.output}",
            title="Slide Agent",
        )
    )

    # Initialize Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]Error: ANTHROPIC_API_KEY not found in environment[/red]")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Display user request
    console.print(Panel(args.prompt, title="[bold blue]User Request[/bold blue]"))

    # Agent conversation loop with dual-mode operation
    messages = [{"role": "user", "content": args.prompt}]
    compute_iterations = 0
    autonomous_complete = False
    last_created_file = None

    # Autonomous creation and refinement phase
    while not autonomous_complete and compute_iterations < args.compute:
        compute_iterations += 1
        console.print(
            f"[yellow]Calling Claude Sonnet 4.0... (iteration {compute_iterations}/{args.compute})[/yellow]"
        )

        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=8192,  # Increased for HTML+CSS content
                system=SYSTEM_PROMPT,
                messages=messages,
                tools=TOOLS,
            )

            # Process response content
            tool_results = []
            response_text = ""
            for content in response.content:
                if content.type == "text":
                    response_text += content.text
                    console.print(
                        Panel(content.text, title="[bold green]Claude's Analysis[/bold green]")
                    )
                elif content.type == "tool_use":
                    tool_name = content.name
                    tool_input = content.input

                    console.print(
                        Panel(
                            f"[bold yellow]Tool: {tool_name}[/bold yellow]\n"
                            f"Input: {json.dumps(tool_input, indent=2)[:200]}...",
                            title="Tool Execution",
                        )
                    )

                    # Execute tools
                    if tool_name == "create_html_slide":
                        result = create_html_slide(
                            reasoning=tool_input.get("reasoning", ""),
                            slide_content=tool_input.get("slide_content", ""),
                            filename=tool_input.get("filename", "slide"),
                            output_path=tool_input.get("output_path", args.output),
                        )
                        # Track the last created file for text editor operations
                        filename = tool_input.get("filename", "slide")
                        last_created_file = os.path.join(args.output, f"{filename}.html")

                        tool_results.append({"tool_use_id": content.id, "content": result})
                    elif tool_name == "str_replace_based_edit_tool":
                        result = execute_text_editor_tool(tool_input, content.id, last_created_file)
                        tool_results.append({"tool_use_id": content.id, "content": result})
                    else:
                        tool_results.append({
                            "tool_use_id": content.id,
                            "content": f"Unknown tool: {tool_name}",
                        })

            # Add assistant response to conversation history
            messages.append({"role": "assistant", "content": response.content})

            # Add tool results to conversation if any tools were used
            if tool_results:
                for tool_result in tool_results:
                    messages.append({
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": tool_result["tool_use_id"],
                                "content": tool_result["content"],
                            }
                        ],
                    })

                console.print("[cyan]Tools executed. Agent continuing refinement...[/cyan]")
            else:
                # No tools used, check if Claude signals completion
                if any(
                    phrase in response_text.lower()
                    for phrase in [
                        "slide creation complete",
                        "creation complete",
                        "slide is complete",
                        "finished",
                        "ready for collaboration",
                        "ready for user feedback",
                    ]
                ):
                    autonomous_complete = True
                    console.print("[green]Autonomous creation and refinement complete![/green]")
                else:
                    # Continue the conversation
                    console.print("[cyan]Continuing conversation...[/cyan]")

        except Exception as e:
            console.print(f"[red]Error calling Claude API: {e}[/red]")
            sys.exit(1)

    if compute_iterations >= args.compute and not autonomous_complete:
        console.print(f"[yellow]Reached maximum iterations ({args.compute})[/yellow]")
        autonomous_complete = True

    # Interactive collaboration phase (if not disabled)
    if autonomous_complete and not args.non_interactive:
        console.print(
            "\n[cyan]🎨 Slide creation complete! You can now request changes or improvements.[/cyan]"
        )
        console.print(
            "[dim]Type your requests naturally (e.g., 'make it more colorful', 'add animations')\nType 'done', 'finished', or 'complete' to exit.[/dim]\n"
        )

        while True:
            try:
                user_input = input("💬 What changes would you like? ")
                if not user_input.strip():
                    continue

                if user_input.lower().strip() in ["done", "finished", "complete", "exit", "quit"]:
                    console.print("[green]Collaboration complete! Your slide is ready.[/green]")
                    break

                # Add user input to conversation
                messages.append({"role": "user", "content": user_input})

                console.print("[yellow]Processing your request...[/yellow]")

                # Claude processes user request
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=8192,
                    system=SYSTEM_PROMPT,
                    messages=messages,
                    tools=TOOLS,
                )

                # Process collaborative response
                tool_results = []
                for content in response.content:
                    if content.type == "text":
                        console.print(
                            Panel(content.text, title="[bold green]Claude's Response[/bold green]")
                        )
                    elif content.type == "tool_use":
                        tool_name = content.name
                        tool_input = content.input

                        console.print(
                            Panel(
                                f"[bold yellow]Tool: {tool_name}[/bold yellow]",
                                title="Implementing Changes",
                            )
                        )

                        if tool_name == "str_replace_based_edit_tool":
                            result = execute_text_editor_tool(
                                tool_input, content.id, last_created_file
                            )
                            tool_results.append({"tool_use_id": content.id, "content": result})
                        else:
                            tool_results.append({
                                "tool_use_id": content.id,
                                "content": f"Tool executed: {tool_name}",
                            })

                # Add response and tool results to conversation
                messages.append({"role": "assistant", "content": response.content})

                if tool_results:
                    for tool_result in tool_results:
                        messages.append({
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": tool_result["tool_use_id"],
                                    "content": tool_result["content"],
                                }
                            ],
                        })

            except KeyboardInterrupt:
                console.print("\n[yellow]Collaboration interrupted. Your slide is ready![/yellow]")
                break
            except Exception as e:
                console.print(f"[red]Error during collaboration: {e}[/red]")
                continue


if __name__ == "__main__":
    main()

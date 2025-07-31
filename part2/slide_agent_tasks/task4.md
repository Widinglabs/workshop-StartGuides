name: "Sophisticated System Prompt - Aesthetic Excellence"
description: |

## Context References

```yaml
REFERENCE GitHub Spark System Prompt Analysis:
  path: PRPs/ai_docs/systemm_prompt_analysis.md
  why: 5000-word system prompt with "aesthetically refined and emotionally resonant" design philosophy
  why: Demonstrates sophisticated design theory integration in prompts
  why: Shows how to embed design expertise directly into LLM instructions
```

## Goal

ELEVATE system prompt from basic slide creation to sophisticated design expertise, incorporating design philosophy, typographic excellence, and aesthetic refinement principles from world-class systems like GitHub Spark.

## What

Enhanced system prompt with:

- Design philosophy and foundational principles
- Typographic excellence guidance
- Aesthetic refinement standards
- Clear behavioral expectations
- Good/bad examples for slide creation
- Sophisticated design theory integration

### Success Criteria

- [ ] System prompt emphasizes "aesthetically refined and emotionally resonant" slides
- [ ] Includes sophisticated typography and design theory guidance
- [ ] Provides clear good/bad examples for slide creation behavior
- [ ] Maintains LLM trust patterns while adding design expertise
- [ ] Elevates slide quality to professional design standards

## Implementation Blueprint

### Design Philosophy Integration

```python
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

You have access to create_html_slide tool. Generate complete HTML with embedded CSS that demonstrates:
- Standard 16:9 presentation frame (1920x1080px or 1366x768px with safe margins)
- Contextually appropriate design choices for the content domain
- Professional typography and color theory application
- Modern, responsive design principles with consistent grid system
- Purposeful visual hierarchy and spacing within presentation constraints

CRITICAL: Always create slides with presentation-ready dimensions and consistent layout framework that works across different display sizes.

Trust your design expertise to create exactly what serves the user's purpose."""
```

### Enhanced Tool Schema

```python
TOOLS = [{
    "name": "create_html_slide",
    "description": "Create aesthetically refined and emotionally resonant HTML slides with embedded CSS. Apply sophisticated design principles and contextual intelligence.",
    "input_schema": {
        "properties": {
            "reasoning": {
                "description": "Your design reasoning including typography, color, and aesthetic choices"
            },
            "slide_content": {
                "description": "Complete HTML with embedded CSS demonstrating design excellence"
            },
            "filename": {
                "description": "Meaningful filename reflecting the slide's purpose and content"
            },
            "output_path": {
                "description": "Directory path for slide output"
            }
        }
    }
}]
```

## Tasks to Complete

```yaml
Task 1 - ENHANCE system prompt with design philosophy:
  - IMPLEMENT: "Aesthetically refined and emotionally resonant" standard
  - IMPLEMENT: Foundational principles section
  - IMPLEMENT: Typographic excellence detailed guidance
  - VALIDATE: Prompt emphasizes sophisticated design standards

Task 2 - ADD behavioral excellence examples:
  - IMPLEMENT: Good/bad examples for slide creation responses
  - IMPLEMENT: Clear guidance on professional communication
  - IMPLEMENT: Context-appropriate design decision examples
  - VALIDATE: Examples demonstrate sophisticated design thinking

Task 3 - INTEGRATE design theory principles:
  - IMPLEMENT: Color psychology guidance for content domains
  - IMPLEMENT: Visual hierarchy and spatial awareness principles
  - IMPLEMENT: Micro-interaction and finishing touch standards
  - VALIDATE: Prompt teaches design theory while instructing behavior

Task 5 - ADD presentation frame standards:
  - IMPLEMENT: 16:9 aspect ratio requirements (1920x1080px or 1366x768px)
  - IMPLEMENT: Safe area margins for projection compatibility
  - IMPLEMENT: Consistent layout zones and grid system
  - VALIDATE: All slides maintain professional presentation dimensions

Task 4 - MAINTAIN LLM trust while adding expertise:
  - IMPLEMENT: Trust Claude's design intelligence with sophisticated guidance
  - IMPLEMENT: Context-appropriate design choices for different domains
  - IMPLEMENT: Professional standards without rigid templates
  - VALIDATE: Enhanced expertise doesn't compromise LLM trust patterns
```

## Design Excellence Patterns

```python
# GOOD: Sophisticated design reasoning
"Creating quantum computing slide for CS students - using technical blues (#2563eb, #1e40af) with Fira Code for code snippets, clean sans-serif hierarchy, academic whitespace proportions"

# GOOD: Contextual design intelligence
"Executive financial presentation - corporate grays and blues, data-focused typography, professional spacing that conveys authority and precision"

# GOOD: Audience-appropriate aesthetic
"Children's nutrition guide - warm friendly colors (#f59e0b, #10b981), playful but readable fonts, engaging visual hierarchy with generous spacing"

# BAD: Generic design thinking
"I'll make a nice looking slide with good colors"

# BAD: Template-based approach
"Using the standard corporate template with blue headers"
```

## Validation Gates

### Level 1: Design Philosophy Integration

```bash
uv run slide_agent.py -p "Create a slide about artificial intelligence ethics"
# Expected:
# - Claude discusses design choices appropriate for serious academic topic
# - Professional color palette and typography reasoning
# - Content-focused design decisions explained
```

### Level 2: Contextual Design Intelligence

```bash
uv run slide_agent.py -p "Create a slide about children's birthday party planning"
# Expected:
# - Bright, engaging colors appropriate for celebration context
# - Playful but readable typography choices
# - Visual hierarchy that guides parent attention

uv run slide_agent.py -p "Create a slide about quarterly financial results for board meeting"
# Expected:
# - Corporate, authoritative design aesthetic
# - Data-focused color choices and typography
# - Professional spacing and visual hierarchy
```

### Level 3: Design Excellence Standards

```bash
# Generated slides should demonstrate:
# - Sophisticated typography with mathematical scale relationships
# - Contextually appropriate color psychology
# - Professional visual hierarchy and spacing
# - Content-first design philosophy
# - Aesthetic refinement and emotional resonance
```

## Anti-Patterns to Avoid

- ❌ Don't add design restrictions - enhance design intelligence
- ❌ Don't create rigid design templates - trust contextual design choices
- ❌ Don't overwhelm with rules - integrate design thinking naturally
- ❌ Don't lose LLM trust - enhance expertise while maintaining intelligence
- ❌ Don't separate design from content - emphasize holistic creation

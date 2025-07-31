# Claude Code Best Practices: From Beginner to Expert

## Table of Contents

- [Philosophy & Core Principles](#philosophy--core-principles)
- [Beginner Level: Getting Started](#beginner-level-getting-started)
- [Intermediate Level: Developing Mastery](#intermediate-level-developing-mastery)
- [Advanced Level: Power User Patterns](#advanced-level-power-user-patterns)
- [Expert Level: Orchestration & Automation](#expert-level-orchestration--automation)
- [Performance Optimization](#performance-optimization)
- [Enterprise & Security](#enterprise--security)
- [Troubleshooting & Common Pitfalls](#troubleshooting--common-pitfalls)

## Philosophy & Core Principles

### Understanding Claude Code's Design Philosophy

Claude Code is intentionally **unopinionated** and **low-level**. As Boris (the creator) explained: "We don't know what the right UX is yet, so we're starting simple." This design philosophy creates several core principles:

1. **Trust the Model**: Don't over-engineer. Claude's intelligence can handle complexity better than rigid abstractions.
2. **Raw Access**: Minimal barriers between you and the model's capabilities.
3. **Unix Philosophy**: Composable, scriptable, pipeable tools that integrate into existing workflows.
4. **Safety First**: Conservative permissions with customizable allowlists.
5. **Flexibility Over Convention**: Let users discover their own optimal patterns.

### The Exponential Context

Claude's capabilities are improving exponentially. Your practices should evolve to leverage this:

- **Start simple**, then add complexity as you learn
- **Experiment frequently** with new approaches
- **Share discoveries** with your team
- **Stay flexible** as new capabilities emerge

---

## Beginner Level: Getting Started

### Installation & First Steps

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start your first session
claude

# Initialize project memory if not done yet
/init
```

### Your First Interactions

Start with **codebase Q&A** - the easiest way to build confidence:

**Good first questions on a new codebase:**

```
How does authentication work in this project?
What's the main entry point for the API?
Where are the database models defined?
What testing framework does this project use?
How do I run the development server?

Or use the custom /onboarding command to get started.
```

**Why this works:** Claude will explore your codebase to answer these questions, demonstrating its navigation capabilities while helping you learn.

### Understanding Basic Commands

**Essential beginner commands:**

- `claude` - Start interactive session
- `/help` - Get help anytime
- `/clear` - Reset context when it gets cluttered
- `Ctrl+C` - Cancel current operation
- `Ctrl+D` - Exit Claude

### Your First CLAUDE.md File

Create a `CLAUDE.md` file in your project root. Start simple:

```markdown
# Project Commands

- npm run dev: Start development server
- npm test: Run tests
- npm run build: Build for production

# Code Style

- Use TypeScript for all new files
- Follow existing naming conventions
- Add JSDoc comments for public functions

# Testing

- Write tests in **tests** folders
- Use Vitest for unit tests
- Run single tests with: npm test -- --testNamePattern="MyTest"
```

**Key insight:** This file becomes part of Claude's context automatically. Keep it concise and actionable.

### Basic Workflow Pattern

**The "Explore → Plan → Code → Verify" pattern:**

1. **Explore**: "Read the authentication module and understand how it works"
2. **Plan**: "Make a plan for adding two-factor authentication"
3. **Code**: "Implement the plan step by step"
4. **Verify**: "Run the tests and fix any issues"

This pattern prevents Claude from jumping straight to coding without understanding context.

### Permission System Basics

Claude asks permission for potentially dangerous operations. Learn to manage this:

```bash
# Allow file editing permanently
/permissions add Edit

# Allow git commits
/permissions add Bash(git commit:*)

# View current permissions
/permissions list
```

**Safety tip:** Start conservative, then add permissions as you build trust and understanding.

---

## Intermediate Level: Developing Mastery

### Advanced Memory Management

**CLAUDE.md Hierarchy:**

- `~/.claude/CLAUDE.md` - Personal preferences (all projects)
- `./CLAUDE.md` - Project root (team shared)
- `./subdir/CLAUDE.md` - Directory-specific context

**Advanced CLAUDE.md techniques:**

```markdown
# Advanced Example

## Import other memories

@./agent-wiki/coding-standards.md
@./agent-wiki/api-patterns.md
@./agent-wiki/architecture.md

## Be specific about tools

- linter: `npm run lint` (must pass before commits)
- type checker: `npm run typecheck` (must pass before commits)
- test runner: `npm test` (single tests preferred for speed)

## Common patterns in this codebase

- API endpoints use `src/routes/*.ts` pattern
- Validation schemas in `src/schemas/`
- Database operations in `src/db/operations/`

## Important context

- This is a production system with 10k+ daily users
- Database migrations must be backwards compatible
- All API changes require updating OpenAPI spec in `docs/api.yaml`
- Deploy process uses GitHub Actions (see `.github/workflows/`)

## Team preferences

- Prefer functional over class-based components
- Use explicit return types for all functions
- Error messages must be user-friendly (no technical jargon)
```

### Mastering Specificity

**Poor:** "Add error handling"
**Good:** "Add error handling for the user registration endpoint that catches duplicate email errors and returns a user-friendly message with status code 409"

**Poor:** "Write tests"
**Good:** "Write unit tests for the PaymentProcessor class, covering successful payment, insufficient funds, and network timeout scenarios. Use mocks for the external payment API."

**Why specificity matters:** Claude can infer intent, but specific instructions dramatically improve first-attempt success rates.

### Visual Context

**Effective image usage:**

- **Screenshots:** Paste browser screenshots to show desired UI states
- **Mockups:** Drag-drop design files for implementation guidance
- **Diagrams:** Architecture diagrams help with complex system changes
- **Error screenshots:** Visual debugging of UI issues

**Pro tip:** Use `Cmd+Ctrl+Shift+4` (macOS) to screenshot directly to clipboard, then `Ctrl+V` to paste.

### Test-Driven Development with Claude

TDD becomes incredibly powerful with agentic coding:

```
1. "Write comprehensive tests for user authentication, covering login, logout,
   session management, and password reset. Don't implement anything yet -
   this is test-driven development."

2. "Run the tests and confirm they fail. Don't write implementation code."

3. "Commit the failing tests with message 'Add authentication tests'"

4. "Now implement the authentication system to make these tests pass.
   Don't modify the tests - only add implementation code."

5. "Keep iterating until all tests pass, then commit the implementation."
```

**Why this works:** Tests provide a clear target for Claude to iterate against, leading to more robust implementations.

### Custom Slash Commands

Create reusable workflows:

```bash
# Create .claude/commands/fix-gh-issue-simple.md
```

```markdown
Please analyze and fix GitHub issue #$ARGUMENTS.

Follow these steps:

1. Use `gh issue view $ARGUMENTS` to get issue details
2. Search codebase for relevant files using appropriate tools
3. Understand the root cause
4. Implement fix with tests
5. Verify fix resolves issue
6. Create descriptive commit
7. Comment on issue with fix summary

Remember: Always write tests to prevent regression.
```

Usage: `/project:fix-gh-issue-simple 123`

### MCP Integration

Add external tools to Claude's capabilities:

```bash
# Add Puppeteer for browser automation
claude mcp add puppeteer --transport stdio --command "npx @puppeteer/mcp-server"

# Add custom database tools
claude mcp add dbtools --transport stdio --command "python db-mcp-server.py"
```

Use MCP resources:

```
# Reference database schema
@dbtools://schema/users

# Take screenshot of current page
Take a screenshot using @puppeteer://screenshot
```

---

## Advanced Level: Power User Patterns

### Multi-Claude Orchestration

**Pattern 1: Specialized Roles**

- **Terminal 1 (Writer):** Primary development work
- **Terminal 2 (Reviewer):** Code review and testing
- **Terminal 3 (Docs):** Documentation updates

**Pattern 2: Git Worktrees for Parallel Development**

```bash
# Create worktrees for parallel work
git worktree add ../project-auth-feature auth-feature
git worktree add ../project-ui-redesign ui-redesign
git worktree add ../project-performance perf-improvements

# Start Claude in each worktree
cd ../project-auth-feature && claude &
cd ../project-ui-redesign && claude &
cd ../project-performance && claude &

# Work on independent features simultaneously
```

**Why this works:** Different Claude instances can work on non-conflicting features simultaneously, dramatically increasing development velocity.

### Advanced Workflow Patterns

**The "Checkpoint" Pattern:**

```
1. "Explore the billing system and create a detailed plan for adding
   subscription management. Save this plan to PLAN.md - don't implement yet."

2. Review PLAN.md, make adjustments

3. "Implement the plan in PLAN.md step by step. Reference the plan
   frequently and update it as you progress."
```

**The "Verification Chain" Pattern:**

```
# Terminal 1: Implementation
"Implement user role management system"

# Terminal 2: Testing
"Review the role management code in src/auth/ and create comprehensive
 integration tests"

# Terminal 3: Security Review
"Analyze the role management implementation for security vulnerabilities
 and create a security assessment report"
```

### Headless Mode & Automation

**Batch Processing:**

```bash
# Process multiple files
for file in src/components/*.tsx; do
  claude -p "Add TypeScript strict mode compliance to $file" --allowedTools Edit
done
```

**CI/CD Integration:**

```bash
# .github/workflows/ai-review.yml
- name: AI Code Review
  run: |
    claude -p "Review this PR for code quality, security issues, and best practices.
              Format output as GitHub issue comments." --output-format json > review.json
```

**Issue Triage:**

```bash
# Triage GitHub issues
gh issue list --json number,title,body | \
  claude -p "Analyze these issues and assign appropriate labels and priorities"
```

### Performance Optimization Strategies

**Context Window Management:**

- Use `/clear` frequently between unrelated tasks
- Split large tasks into focused sessions
- Use multiple Claude instances for complex multi-part work

**Memory File Optimization:**

```markdown
# Optimized CLAUDE.md structure

## CRITICAL INFO (always needed)

- Build command: npm run build
- Test command: npm test
- Linting: npm run lint (MUST pass)

## ARCHITECTURE PATTERNS

@./docs/patterns.md

## ENVIRONMENT SPECIFIC

@./environments/development.md

## RARELY NEEDED (keep separate)

@./docs/deployment-details.md
```

---

## Expert Level: Orchestration & Automation

### Enterprise Multi-Claude Patterns

**The "Assembly Line" Pattern:**

```bash
# Terminal 1: Feature Factory
claude -p "Generate boilerplate for new features based on specifications
          in specifications/ directory"

# Terminal 2: Quality Control
claude -p "Review and improve code in review-queue/ directory,
          ensure adherence to company standards"

# Terminal 3: Documentation Engine
claude -p "Generate and update documentation for completed features
          in completed/ directory"

# Terminal 4: Test Generator
claude -p "Create comprehensive test suites for features in
          testing-queue/ directory"
```

**Cross-Repository Coordination:**

```bash
# Repository 1: API
cd api-repo && claude -p "Update API endpoints based on schema changes
                         in ../shared-schemas/v2.json"

# Repository 2: Frontend
cd frontend-repo && claude -p "Update client code to use new API endpoints
                              documented in ../api-repo/docs/openapi.yaml"

# Repository 3: Mobile
cd mobile-repo && claude -p "Update mobile app API integration based on
                            changes in ../api-repo/"
```

### Advanced Automation Patterns

**Smart Issue Resolution:**

```bash
# Create smart-fix.sh
#!/bin/bash
ISSUE_NUMBER=$1
ISSUE_DETAILS=$(gh issue view $ISSUE_NUMBER --json title,body,labels)

echo "$ISSUE_DETAILS" | claude -p "
Analyze this GitHub issue and determine:
1. Issue type (bug, feature, refactor, etc.)
2. Affected components
3. Estimated complexity
4. Required approach

Then execute the appropriate fix strategy:
- For bugs: Investigate, fix, add regression test
- For features: Plan, implement, test, document
- For refactors: Analyze impact, refactor safely, maintain compatibility

Provide progress updates in issue comments using 'gh issue comment'.
"
```

**Intelligent Code Migration:**

```bash
# Large-scale refactoring
find src/ -name "*.js" | head -20 | xargs -I {} claude -p "
Convert {} from JavaScript to TypeScript:
1. Add proper type annotations
2. Fix any type errors
3. Update imports/exports
4. Ensure compatibility with existing code
5. Run tests to verify changes

Files to convert: {}
"
```

### Custom MCP Server Development

Create specialized tools for your domain:

```python
# custom-mcp-server.py
from mcp.server import MCP
from mcp.types import Tool, TextContent

async def analyze_performance(code: str) -> str:
    # Custom performance analysis logic
    return f"Performance analysis: {analysis_result}"

server = MCP("performance-analyzer")

@server.tool()
async def performance_audit(code_path: str) -> list[TextContent]:
    # Implementation
    pass
```

### Advanced Security Patterns

**Secure Development Workflow:**

```markdown
# Security-focused CLAUDE.md

## SECURITY REQUIREMENTS

- All database queries MUST use parameterized statements
- Authentication tokens expire in 24 hours maximum
- All user inputs MUST be validated and sanitized
- Secrets never committed to git (use environment variables)
- All API endpoints require authentication unless explicitly public

## SECURITY REVIEW CHECKLIST

Before any commit, verify:

- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all user data
- [ ] Proper error handling (no sensitive info in errors)
- [ ] Authentication/authorization checks
- [ ] SQL injection prevention
- [ ] XSS prevention in all outputs

## SECURITY TOOLS

- Run: `npm audit` (check for vulnerabilities)
- Run: `npm run security-scan` (custom security scanner)
- Use: `/security-review` slash command before commits
```

---

## Performance Optimization

### Context Window Optimization

**Effective Context Management:**

```bash
# Good: Focused sessions
claude  # Session 1: Authentication work
/clear
# Session 2: UI components (fresh context)

# Bad: Everything in one session
claude  # Working on auth, then UI, then database, then deployment...
```

**Strategic Use of /clear:**

- Between unrelated tasks
- When context becomes cluttered with irrelevant information
- Before starting complex multi-step workflows
- When switching between different parts of the codebase

### Memory File Performance

**Optimized CLAUDE.md Structure:**

```markdown
# CRITICAL FIRST (most frequently needed)

- npm run dev
- npm test
- npm run lint

# IMPORTS (pull in as needed)

@./docs/architecture.md
@./standards/coding-style.md

# CONTEXT-SPECIFIC (loaded on demand)

@./frontend/patterns.md
@./backend/database-patterns.md
```

**Performance Anti-patterns:**

```markdown
# DON'T: Massive single file

# This creates context bloat

- 200 lines of detailed API documentation
- Complete deployment procedures
- Full troubleshooting guide
- Extensive code examples

# DO: Modular imports

@./docs/api-quick-reference.md # Just what's needed daily
@./deployment/quick-deploy.md # Separate concerns
```

### Thinking Budget Optimization

Use thinking modes strategically:

**Optimal thinking usage:**

```
# Good: Use thinking when Claude has context
"Read these 5 files, then think hard about the best architecture
for the new feature"

# Less optimal: Thinking without context
"Think hard about the best way to implement authentication"
```

**Thinking hierarchy:**

- `"think"` - Quick analysis with existing context
- `"think hard"` - Deeper analysis, good for architecture decisions
- `"think harder"` - Complex problem solving with trade-offs
- `"ultrathink"` - Maximum analysis for critical decisions

---

## Enterprise & Security

### Enterprise Configuration Management

**Hierarchical Settings Management:**

```
1. Enterprise policies (managed by IT)
2. Team settings (checked into git)
3. Project settings (project-specific)
4. User settings (personal preferences)
```

**Example enterprise setup:**

```json
// Enterprise policy (highest priority)
{
  "allowedTools": ["Edit", "Read", "Bash(git:*)", "Bash(npm:*)"],
  "model": "claude-4-sonnet-latest",
  "maxTokens": 8192,
  "blockedDomains": ["*.competitor.com"],
  "requiredMemoryFiles": ["security-guidelines.md"]
}
```

### Security Best Practices

**Safe Permission Configuration:**

```bash
# Production-safe permissions
/permissions add Edit                    # File editing
/permissions add Bash(git:*)            # Git operations
/permissions add Bash(npm:test)         # Testing only
/permissions add Bash(npm:lint)         # Linting only

# Avoid in production
/permissions add Bash(*)                # Too broad
/permissions add Bash(rm:*)             # Dangerous
/permissions add Bash(curl:*)           # Network access
```

**Audit Trail Setup:**

```json
{
  "auditLog": {
    "enabled": true,
    "logFile": "/var/log/claude-code-audit.log",
    "includeFileContents": false,
    "includeCommands": true
  }
}
```

### Container & Isolation Strategies

**Docker Development Environment:**

```dockerfile
# Dockerfile.claude-dev
FROM node:18-alpine

# Install Claude Code
RUN npm install -g @anthropic-ai/claude-code

# Create non-root user
RUN addgroup -S claude && adduser -S claude -G claude
USER claude

WORKDIR /workspace

# Safe permissions for development
ENV CLAUDE_ALLOWED_TOOLS="Edit,Read,Bash(npm:*),Bash(git:*)"

CMD ["claude"]
```

**Usage:**

```bash
# Run Claude in isolated container
docker run -it -v $(pwd):/workspace claude-dev-env
```

---

## Troubleshooting & Common Pitfalls

### Common Beginner Mistakes

**1. Not Using CLAUDE.md Files**

```markdown
# Problem: Starting every session by explaining project structure

# Solution: Create comprehensive CLAUDE.md

## Project Structure

- src/components/ - React components
- src/api/ - API route handlers
- src/utils/ - Utility functions
- tests/ - Test files

## Build Commands

- npm run dev - Development server (port 3000)
- npm run build - Production build
- npm test - Run all tests
```

**2. Being Too Vague**

```markdown
# Problem: "Fix the login bug"

# Solution: "The login form in src/components/LoginForm.tsx

# doesn't handle network timeouts properly. When the API

# call to /api/auth/login takes longer than 5 seconds,

# the form hangs without feedback. Add proper timeout

# handling with user-friendly error messages."
```

**3. Not Using Visual Context**

```markdown
# Problem: "Make the UI look better"

# Solution: Provide screenshot of current state + mockup

# of desired state, then: "Update the dashboard to match

# this mockup. Focus on the card layout and spacing."
```

### Performance Issues & Solutions

**Issue: Slow Responses**

```bash
# Diagnose
claude --verbose  # Check for network/API issues

# Solutions
1. Use /clear to reduce context size
2. Check internet connection
3. Switch models with /model
4. Split complex tasks into smaller parts
```

**Issue: Context Window Full**

```bash
# Symptoms: Claude says "context is too large"

# Solutions
1. /clear immediately
2. Break task into smaller parts
3. Use multiple Claude sessions
4. Optimize CLAUDE.md files (remove unnecessary content)
```

**Issue: Repetitive Permission Prompts**

```bash
# Problem: Asked for same permission repeatedly

# Solution: Add to permanent allowlist
/permissions add ToolName
# or configure in settings.json
```

### Advanced Troubleshooting

**Debug MCP Issues:**

```bash
claude --mcp-debug  # Verbose MCP logging
```

**Audit Tool Usage:**

```bash
# Check what tools Claude is trying to use
claude --verbose

# Review permission settings
claude config list
```

**Performance Profiling:**

```bash
# Time Claude operations
time claude -p "Analyze this codebase structure"

# Monitor context usage
# Watch for "context window" warnings in verbose mode
```

### Recovery Strategies

**When Claude Goes Off Track:**

1. **Interrupt:** Press `Escape` to stop current operation
2. **Redirect:** Provide more specific instructions
3. **Reset:** Use `Double Escape` to edit previous prompt
4. **Fresh Start:** Use `/clear` for clean context

**When Code Changes Are Wrong:**

1. **Undo:** "Undo the last changes and try a different approach"
2. **Git Reset:** `git checkout -- filename` to revert
3. **Review:** "Review your changes and explain your reasoning"
4. **Alternative:** "Try implementing this differently using [specific approach]"

### Best Practices for Recovery

```markdown
# Create recovery slash command: .claude/commands/recover.md

When something goes wrong:

1. Stop current operation (if running)
2. Assess what went wrong: "Explain what just happened and why"
3. Revert if necessary: "Undo changes to files that were modified incorrectly"
4. Adjust approach: "Let's try this differently with [specific guidance]"
5. Prevent recurrence: "Add this lesson learned to CLAUDE.md"

Remember: Mistakes are learning opportunities for both you and Claude.
```

---

## Conclusion

Claude Code's power lies in its flexibility and raw model access. Master these practices progressively:

1. **Start Simple:** Begin with Q&A and basic file operations
2. **Build Context:** Invest in comprehensive CLAUDE.md files
3. **Be Specific:** Detailed instructions dramatically improve outcomes
4. **Iterate Visually:** Provide targets for Claude to improve against
5. **Scale Up:** Use multi-Claude patterns for complex projects
6. **Automate Wisely:** Leverage headless mode for repetitive tasks
7. **Stay Safe:** Understand and configure permissions properly

Remember: Claude Code is designed to grow with you. As your skills develop and the model improves, continuously experiment with new patterns and share your discoveries with your team.

The future of coding is agentic, and Claude Code gives you the tools to explore that future today.

# learning-mode

A behavioral skill for AI agents that shifts them from "do it for you" to "do it with you" - building your expertise instead of replacing it.

## How It Works

Most AI coding tools optimize for one thing: get the code written as fast as possible. That's fine when you're in your comfort zone. But when you're growing into new territory - a new language, a new platform, unfamiliar patterns - speed becomes the enemy of understanding. You ship the feature but you didn't learn anything. Next time, you're just as dependent on the agent.

Learning Mode flips the objective. Instead of minimizing time-to-merge, the agent maximizes YOUR depth of understanding. It still helps you ship, but it does so in a way that makes you more capable each time.

**The 4-Tier Model**

The skill maps your growth across four tiers that mirror how engineers actually level up:

| Tier | You're at | Agent behavior |
|------|-----------|----------------|
| Orientation | New here. Can read but haven't built. | Full context, bridges from what you know, heavy scaffolding. |
| Judgment | Can navigate but need help deciding. | Presents options, explains tradeoffs, validates your reasoning. |
| Execution | Know what to do, need reps. | Steps back, lets you drive, catches mistakes. Light touch. |
| Multiplication | Teaching others. | Challenges you to articulate WHY, helps you scale knowledge. |

**DOK Calibration**

Each skill you're growing gets a Depth of Knowledge level (1-4) that tells the agent exactly how much scaffolding to provide. DOK 1 means you can recall facts but can't apply them yet. DOK 4 means you can synthesize across domains and teach. The agent reads your DOK levels and adjusts its behavior per-skill, per-session. You might be DOK 3 in state management but DOK 1 in accessibility - the agent treats those differently in the same conversation.

**Two Modes**

| Mode | When | What the agent does |
|------|------|---------------------|
| Feature Build | Learning while coding | Guides instead of executes. Asks "what would you try?" before showing answers. Offers micro-challenges (5-15 min exercises) at growth opportunities. |
| PR Review | Learning while reading code | Provides context-first explanations, bridges vocabulary from your strong platform, helps you understand WHY not just WHAT. |

**Build Checkpoints**

Every learning mode build runs through four checkpoints that add rigor to the process:

1. **Task Comprehension** - Before code, verify you understand the scope and changes needed
2. **Concept Connection** - Connect this task to patterns from previous sessions (cumulative learning, not isolated reps)
3. **Thinking Challenges** - During the build, the agent pushes on your reasoning at decision points
4. **Understanding Assessment** - When you ask "check my work," the agent tests your understanding, not just correctness

Plus a **Session Close Reflection** - one sentence on what you learned. Forces consolidation.

**Retrieval Decay**

Skills fade without practice. If a skill below DOK 2.5 hasn't been touched in 14+ days, the agent surfaces a single micro-retrieval at session start. Tests recall, not recognition. Wrong answers are useful data.

**Adaptive Intensity**

The agent calibrates within a session. Strong answers lead to harder questions. Struggle leads to more scaffolding. Never announced - just felt.

**Graduation Signals**

The agent notices when you level up. When you start making correct decisions without prompting, when your questions shift from "what" to "why" to "what if," the agent surfaces it: "You're consistently making good judgment calls on X - ready to move to Execution tier?" Growth becomes visible. The highest signal: **Teaching Back** - can you explain the principle to someone else?

**Agent-agnostic.** Works with Goose (CLI + Desktop), Claude (Code + Desktop), Cursor, Codex, Amp, Gemini CLI, and any agent that reads markdown instructions.

**Model-agnostic.** The skill is plain English instructions. Works with Claude, GPT, Gemini, Llama, or whatever model your agent uses.

---

## Who This Is For

Anyone who uses AI agents to build and ship - and wants to actually get better at the craft, not just produce output faster.

| Role | How Learning Mode helps |
|------|------------------------|
| Engineers | Learning a new language, platform, or architectural pattern. Ship the feature AND understand what you shipped. |
| Designers | Using AI to implement designs but want real fluency in React, CSS, or your implementation stack. |
| Hybrid roles | Strong in one domain, growing in another. The agent respects that asymmetry instead of treating you like a beginner at everything. |

If you've ever finished an AI-assisted coding session and thought "I have no idea what just happened but it works" - this is for you.

---

## Philosophy

AI agents are the most powerful learning tools ever built, but only if you use them that way. The default mode - generate, accept, ship - optimizes for throughput at the cost of understanding. Learning Mode treats every interaction as a chance to build durable skill. The goal isn't to slow you down. It's to make you faster by making you deeper.

---

## Install

### Goose, Claude Code, Cursor, Codex, Amp, Gemini CLI (one command)

```bash
npx skills add dakotafabro/learning-mode -g
```

This installs globally to all supported agents on your machine. Goose Desktop shares config with Goose CLI, so it works there too.

To verify:

```bash
npx skills list -g | grep learning-mode
```

### Claude Desktop

1. Download `learning-mode.skill` from the [latest release](https://github.com/dakotafabro/learning-mode/releases)
2. Open Claude Desktop
3. Drag the `.skill` file into a conversation, or ask Claude: "Install this skill"
4. Click **Save skill** when prompted

Alternatively, ask Claude Desktop directly: "Create a skill from this" and paste the contents of [SKILL.md](./SKILL.md).

### Manual (any agent)

If your agent doesn't support the skills CLI or `.skill` files, copy the contents of [SKILL.md](./SKILL.md) into your agent's custom instructions, system prompt, or project knowledge.

---

## Setup

The skill works immediately with zero config. Say something like "I want to learn this myself - learning mode" in any session and the agent shifts behavior. For deeper calibration, complete these two optional steps:

### 1. Create Your DOK Tracker (optional, recommended)

The DOK tracker tells the agent exactly where you are in your growth so it can auto-calibrate scaffolding per skill.

Copy the template to your working repo:

```bash
cp ~/.agents/skills/learning-mode/dok-tracker.template.md ~/your-repo/dok-tracker.md
```

Open it and fill in:
- Your growth domain skills (what you're learning)
- Initial DOK levels (honest self-assessment, 1-4)
- Tier assignments (Orientation, Judgment, Execution, Multiplication)

Without a tracker, Learning Mode still works - the agent just calibrates from conversation context rather than persistent state.

### 2. Add Your Configuration Block (optional)

Add a config block to your agent's hints file for persistent personalization across sessions.

**Where to put it:**

| Agent | Global config | Project-level config |
|-------|--------------|---------------------|
| Goose (CLI + Desktop) | `~/.config/goose/AGENTS.md` | `.goosehints` in project root |
| Claude Code | `~/.claude/CLAUDE.md` | `CLAUDE.md` in project root |
| Cursor | N/A | `.cursorrules` in project root |
| Codex | N/A | `AGENTS.md` in project root |
| Claude Desktop | Set via conversation ("Remember that my strong platform is...") | N/A |

**The config block:**

```markdown
## Learning Mode Config

- Background knowledge: [your strongest language/framework to reference while learning another]
- Growth platform: [what you're learning]
- Learning style: [how you learn best - e.g. "hands-on with immediate feedback", "theory first then practice", "visual diagrams and analogies"]
- DOK Tracker: [path to your dok-tracker.md]
- Analogies: [optional - domains that help you think]
- Session Log: [optional - path for learning session logs]
```

---

## Customization

Everything is customized through the config block and DOK tracker. You never edit the installed skill files.

### Platform Configuration

Your background knowledge and growth platform tell the agent where to bridge FROM and where to scaffold TO. Here are examples for different roles:

**Frontend engineer learning mobile:**

```markdown
- Background knowledge: React/TypeScript, Node.js, CSS
- Growth platform: Kotlin/Android (Jetpack Compose, coroutines, Dagger/Hilt)
```

**Backend engineer learning frontend:**

```markdown
- Background knowledge: Go, PostgreSQL, distributed systems, Kubernetes
- Growth platform: React/TypeScript, CSS, browser APIs, accessibility
```

**Designer learning to code:**

```markdown
- Background knowledge: Figma, design systems, visual hierarchy, typography, color theory
- Growth platform: React, CSS-in-JS, component architecture, responsive implementation
```

**Designer-who-codes deepening implementation skills:**

```markdown
- Background knowledge: Visual design, CSS, HTML, Figma-to-code workflows
- Growth platform: React state management, API integration, performance optimization
```

**Full-stack engineer learning infrastructure:**

```markdown
- Background knowledge: Rails, React, PostgreSQL, REST APIs
- Growth platform: Terraform, AWS CDK, CI/CD pipelines, observability
```

### Analogy Preferences

Analogies help the agent explain how things work together architecturally by mapping new concepts onto mental models you already hold. Instead of textbook definitions, the agent describes how pieces relate, compose, and depend on each other using language from a domain you think fluently in.

For example, if you tell the agent to use cooking analogies, it might explain a component architecture as: "Think of this like mise en place - you're setting up all your ingredients (props, state, dependencies) before the actual cooking (render) begins. The recipe is the pattern, plating is the UI layer the user sees."

The point isn't to be cute. It's to give you a structural mental model for how the build fits together - what depends on what, what flows where, and why things are organized the way they are. Pick any domain where you already have strong intuitions about composition and structure: cooking, music production, woodworking, gardening, architecture, sports. The agent maps from there.

**How to configure:**

```markdown
- Analogies: use cooking analogies for architecture decisions
```

You can specify different domains for different concerns, or keep it simple with one:

```markdown
- Analogies: use music production analogies for state management, cooking for architecture
```

### Full Configuration Examples

**A designer moving into frontend engineering:**

```markdown
## Learning Mode Config

- Background knowledge: Figma, design systems, visual design, typography, layout
- Growth platform: React, TypeScript, CSS modules, component APIs
- Learning style: Visual - show me diagrams and map concepts to design system thinking
- DOK Tracker: ./growth/dok-tracker.md
- Analogies: use design system analogies for component architecture (tokens = variables, variants = props, auto-layout = flexbox)
- Session Log: ./growth/learning-log.md
```

**A backend engineer picking up frontend:**

```markdown
## Learning Mode Config

- Background knowledge: Java, Spring Boot, PostgreSQL, distributed systems, event sourcing
- Growth platform: React/TypeScript, CSS, browser APIs, accessibility, responsive design
- Learning style: Theory first, then implementation - explain the principle before showing code
- DOK Tracker: ~/growth/dok-tracker.md
- Analogies: use server architecture analogies for component patterns (services = components, DTOs = props, middleware = hooks)
- Session Log: ~/growth/sessions.md
```

**A designer-who-codes leveling up on state and APIs:**

```markdown
## Learning Mode Config

- Background knowledge: Visual design, CSS, HTML, basic React components, Figma
- Growth platform: React state management (Context, reducers, Zustand), REST API integration, error handling, loading states
- Learning style: Hands-on with immediate feedback - let me try first, correct after
- DOK Tracker: ./dok-tracker.md
- Analogies: use design workflow analogies (artboards = routes, layers = component tree, symbols = shared components, prototyping = state transitions)
- Session Log: ./learning-sessions.md
```

### Options Reference

| Option | Where | What it controls |
|--------|-------|-----------------|
| Background knowledge | Config block | What the agent bridges FROM when explaining new concepts |
| Growth platform | Config block | What the agent scaffolds TO |
| Learning style | Config block | How the agent structures explanations and exercises |
| DOK levels per skill | dok-tracker.md | How much scaffolding per skill |
| Tier assignments | dok-tracker.md | What TYPE of scaffolding |
| Analogy preferences | Config block | Which domains the agent uses for explanations |
| Session log location | Config block | Where learning summaries get appended |

### In-session adjustments (no file edits needed):

Everything adapts through conversation. No config changes required mid-session.

- "Learning mode for just the networking layer." - narrows scope to one skill
- "Use sports analogies for this instead." - switches analogy domain
- "I already know dependency injection, skip that part." - reduces scaffolding
- "I need to ship this fast, just build it." - agent returns to full execution for that task

---

## Usage

Say these naturally in conversation. The agent recognizes the intent.

| Say this | What happens |
|----------|--------------|
| "I want to write this composable myself. Learning mode." | Agent shifts to guide posture. You write, it scaffolds and validates. |
| "Learning mode for the ViewModel layer only." | Agent guides on that specific skill. Executes normally on everything else. |
| "Challenge me on state design." | Agent offers a 5-15 min exercise targeting a skill you're building. |
| "Where am I on Android?" | Agent surfaces your current depth-of-knowledge levels per skill. |
| "Explain that decision you just made." | Agent unpacks its reasoning so you can internalize the pattern. |
| "Why does this go in the UseCase instead of the ViewModel?" | Agent goes one layer deeper, explaining the principle behind the choice. |
| "I already know React state. Skip the bridging for hooks." | Agent reduces scaffolding on the fly for that concept. |
| "Use cooking analogies for this architecture." | Agent switches analogy domain mid-session. |

---

## Compatibility

| Agent | Install method | Status |
|-------|---------------|--------|
| Goose CLI | `npx skills add` | Supported |
| Goose Desktop | `npx skills add` (shared config) | Supported |
| Claude Code | `npx skills add` | Supported |
| Claude Desktop | `.skill` file from releases | Supported |
| Cursor | `npx skills add` | Supported |
| Codex | `npx skills add` | Supported |
| Amp | `npx skills add` | Supported |
| Gemini CLI | `npx skills add` | Supported |
| Any other agent | Copy SKILL.md into custom instructions | Supported (manual) |

---

## Credits

Built on:
- The **Three Dimensions of AI Collaboration** framework (DOK, Tool Maturity, Agentic Delegation Trust)
- **Webb's Depth of Knowledge** model adapted for engineering and design skill acquisition
- Practical experience calibrating AI agent behavior for growth-oriented work

Created by [Dakota Fabro](https://github.com/dakotafabro) | [AAIF](https://aaif.dakotafabro.dev)

## License

Apache-2.0 - see [LICENSE](./LICENSE)

# learning-mode

A behavioral skill for AI agents that shifts them from "do it for you" to "do it with you" - optimizing for skill building over shipping speed.

## What This Does

Learning Mode gives your AI agent a different objective: maximize YOUR understanding, not minimize time-to-merge. It calibrates scaffolding to your current depth of knowledge, progressively reducing support as you grow. Covers both feature builds (learning while coding) and PR reviews (learning while reading code).

**Agent-agnostic.** Works with Goose (CLI + Desktop), Claude (Code + Desktop), Cursor, Codex, Amp, Gemini CLI, and any agent that reads markdown instructions.

**Model-agnostic.** The skill is plain English instructions. Works with Claude, GPT, Gemini, Llama, or whatever model your agent uses.

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

## Setup (After Install)

The skill works immediately with zero config. Say `"learning mode"` in any session and the agent shifts behavior. For deeper calibration, complete these two optional steps:

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

- Strong platform: [what you already know well]
- Growth platform: [what you're learning]
- DOK Tracker: [path to your dok-tracker.md]
- Analogies: [optional - domains that help you think]
- Session Log: [optional - path for learning session logs]
```

**Example (React engineer learning Android):**

```markdown
## Learning Mode Config

- Strong platform: React/TypeScript, Node.js
- Growth platform: Kotlin/Android (Jetpack Compose, coroutines, Dagger/Hilt)
- DOK Tracker: ~/development/my-app/growth/dok-tracker.md
- Analogies: use React equivalents when bridging concepts
- Session Log: ~/development/my-app/growth/learning-log.md
```

**Example (Backend engineer learning frontend):**

```markdown
## Learning Mode Config

- Strong platform: Go, PostgreSQL, distributed systems
- Growth platform: React/TypeScript, CSS, browser APIs
- DOK Tracker: ./dok-tracker.md
- Analogies: use server architecture analogies for component patterns
- Session Log: ./learning-sessions.md
```

---

## Customization

Everything is customized through the config block and DOK tracker. You never edit the installed skill files.

### What you can customize:

| Option | Where | What it controls |
|--------|-------|-----------------|
| Strong/growth platforms | Config block | How the agent bridges concepts |
| DOK levels per skill | dok-tracker.md | How much scaffolding per skill |
| Tier assignments | dok-tracker.md | What TYPE of scaffolding |
| Analogy preferences | Config block | Which domains the agent uses for explanations |
| Session log location | Config block | Where learning summaries get appended |

### In-session adjustments (no file edits needed):

- `"learning mode for [specific skill]"` - narrow to one skill
- `"use [domain] analogies for this"` - change analogy domain
- `"I already know [X], skip the bridging"` - reduce scaffolding
- `"ship mode"` - turn off learning mode when you need speed

---

## Usage

| Command | Effect |
|---------|--------|
| `"learning mode"` | Activate for full session |
| `"learning mode for [X]"` | Activate for specific skill/phase |
| `"ship mode"` | Return to normal execution |
| `"challenge me"` | Get a micro-challenge |
| `"explain that"` | Agent unpacks a decision it just made |
| `"where am I?"` | Agent surfaces your current DOK levels |
| `"why?"` | Go one layer deeper in explanation |

---

## Updating

```bash
npx skills update learning-mode -g
```

For Claude Desktop: download the latest `.skill` file from releases and re-install.

---

## Uninstalling

```bash
npx skills remove learning-mode -g
```

For Claude Desktop: go to Settings > Skills and remove it.

---

## How It Works

The skill is pure markdown - no scripts, no binaries, no network calls. It's behavioral instructions that change how your agent interacts with you. The agent reads the SKILL.md and follows the protocol.

The core framework:
- **4-Tier Expert Engineer Model** - Orientation, Judgment, Execution, Multiplication
- **DOK levels 1-4** - calibrate scaffolding depth
- **Feature Build mode** - learning while coding (agent guides instead of executes)
- **PR Review mode** - learning while reading code (context-first, vocabulary bridging)
- **Graduation signals** - the agent notices when you level up
- **Micro-challenges** - focused 5-15 minute exercises targeting specific skills

See [SKILL.md](./SKILL.md) for the complete protocol.

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
- **Webb's Depth of Knowledge** model adapted for engineering skill acquisition
- Practical experience calibrating AI agent behavior for growth-oriented work

Created by [Dakota Fabro](https://github.com/dakotafabro) | [AAIF](https://github.com/aaif)

## License

MIT - see [LICENSE](./LICENSE)

# learning-mode

A behavioral skill for AI agents that shifts them from "do it for you" to "do it with you" - optimizing for skill building over shipping speed.

## What This Does

Learning Mode gives your AI agent a different objective: maximize YOUR understanding, not minimize time-to-merge. It calibrates scaffolding to your current depth of knowledge, progressively reducing support as you grow. Covers both feature builds (learning while coding) and PR reviews (learning while reading code).

Works with any AI agent that supports skills: Goose, Claude Code, Cursor, Codex, Amp, and others.

---

## Install

```bash
npx skills add dakotafabro/learning-mode -g
```

This installs the skill globally. It will be available in all supported agents on your machine.

To verify it installed:

```bash
npx skills list -g | grep learning-mode
```

You should see:

```
learning-mode    ~/.agents/skills/learning-mode    Source: dakotafabro/learning-mode
```

---

## What Gets Installed

The `skills` CLI copies the skill files to `~/.agents/skills/learning-mode/` and creates symlinks into each agent's skill directory:

| Agent | Skill location |
|-------|---------------|
| Goose | `~/.config/goose/skills/learning-mode/` |
| Claude Code | `~/.claude/skills/learning-mode/` |
| Cursor | Loaded via universal skills path |
| Codex | Loaded via universal skills path |
| Others | `~/.agents/skills/learning-mode/` (universal) |

Your agent reads `SKILL.md` automatically when the skill is relevant to your session.

---

## Setup (After Install)

The skill installs instantly, but to get the most out of it you need two things:

### 1. Create Your DOK Tracker

Copy the included template to your working repo or personal config:

```bash
cp ~/.agents/skills/learning-mode/dok-tracker.template.md ~/your-repo/dok-tracker.md
```

Open it and fill in:
- Your growth domain skills (what you're learning)
- Initial DOK levels (honest self-assessment, 1-4)
- Tier assignments (Orientation, Judgment, Execution, Multiplication)

The agent reads this file to calibrate its behavior. Without it, the agent can still use Learning Mode but won't auto-detect which skills need scaffolding.

### 2. Add Your Configuration Block

Add a configuration block to your agent's hints file. This tells the agent your context so it can calibrate properly.

**Where to put it (by agent):**

| Agent | Global config file | Project-level config |
|-------|-------------------|---------------------|
| Goose | `~/.config/goose/AGENTS.md` | `.goosehints` in project root |
| Claude Code | `~/.claude/CLAUDE.md` | `CLAUDE.md` in project root |
| Cursor | N/A | `.cursorrules` in project root |
| Codex | N/A | `AGENTS.md` in project root |

**The config block:**

```markdown
## Learning Mode Config

- Strong platform: [what you already know well, e.g., "Python/Django", "React/TypeScript", "iOS/Swift"]
- Growth platform: [what you're learning, e.g., "Kotlin/Android", "Rust", "Go/distributed systems"]
- DOK Tracker: [path to your dok-tracker.md, e.g., "~/my-repo/dok-tracker.md"]
- Analogies: [optional - domains that help you think, e.g., "cooking for architecture, sports for coordination patterns"]
- Session Log: [optional - path for learning session logs, e.g., "~/my-repo/learning-log.md"]
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

## Customization Options

Everything is customized through the config block and DOK tracker. No files in the skill itself need editing.

### What you can customize:

| Option | Where to set it | What it controls |
|--------|----------------|-----------------|
| Strong/growth platforms | Config block in agent hints | How the agent bridges concepts (analogies, vocabulary) |
| DOK levels per skill | Your dok-tracker.md | How much scaffolding the agent provides per skill |
| Tier assignments | Your dok-tracker.md | What TYPE of scaffolding (hands-first vs prompt-first vs light-touch) |
| Analogy preferences | Config block in agent hints | Which non-technical domains the agent uses for explanations |
| Session log location | Config block in agent hints | Where learning session summaries get appended |
| PR review depth | Your DOK levels | How much context the agent provides before asking you to engage |

### Customization that happens in-session:

You can also adjust on the fly without editing any files:

- `"learning mode for [specific skill]"` - narrows to one skill
- `"use [domain] analogies for this"` - changes analogy domain mid-session
- `"I already know [X], skip the bridging"` - tells agent to reduce scaffolding
- `"ship mode"` - turns off learning mode entirely when you need speed

### Updating your DOK levels:

The agent will suggest DOK updates when it notices graduation signals. You confirm or reject. The tracker is collaborative - you and the agent maintain it together.

To manually update, edit your `dok-tracker.md` directly. Change the DOK number and add an entry to the Progression Log with evidence.

---

## Usage

Once installed and configured, use these commands in any session:

| Command | Effect |
|---------|--------|
| `"learning mode"` | Activate for full session |
| `"learning mode for [X]"` | Activate for specific skill/phase |
| `"ship mode"` | Return to normal execution |
| `"challenge me"` | Get a micro-challenge |
| `"explain that"` | Agent unpacks a decision it just made |
| `"where am I?"` | Agent surfaces your current DOK levels |
| `"why?"` | Go one layer deeper in explanation |

### Responsive Activation

If you have a DOK tracker configured, the agent will also activate Learning Mode automatically when a task touches a skill at DOK 1-2. It announces the shift and you can override with `"ship mode"` anytime.

---

## Updating

```bash
npx skills update learning-mode -g
```

This pulls the latest version from the repo.

---

## Uninstalling

```bash
npx skills remove learning-mode -g
```

---

## How It Works (Technical)

The `skills` CLI:
1. Clones this repo to a temp directory
2. Copies the skill files to `~/.agents/skills/learning-mode/`
3. Creates symlinks from each supported agent's skill directory to that location
4. Your agent reads `SKILL.md` as part of its system context when the skill is relevant

The skill is pure markdown - no scripts, no binaries, no network calls. It's instructions that change how your agent behaves. The agent reads the SKILL.md and follows the protocol described in it.

Your DOK tracker and config block are the only user-side files. They live wherever you put them (your repo, your home directory, wherever makes sense for your workflow).

---

## Philosophy

The best engineers aren't the ones who ship fastest with AI help. They're the ones who use AI help to become better engineers. Speed comes from understanding. Understanding comes from doing the work yourself, with the right scaffolding at the right time.

Learning Mode turns your AI agent into the senior engineer sitting next to you - not grabbing the keyboard, but asking the right questions and knowing when to let you struggle productively versus when to unblock you.

---

## Full Documentation

See [SKILL.md](./SKILL.md) for the complete protocol:
- The 4-Tier Expert Engineer Model
- DOK calibration and graduation signals
- The Learning Mode Contract (agent behavior rules)
- Progressive Disclosure and the Why Stack
- PR Review in Learning Mode (context-first approach)
- Micro-challenges
- Session logging format
- Anti-patterns to avoid

---

## Credits

Built on:
- The **Three Dimensions of AI Collaboration** framework (DOK, Tool Maturity, Agentic Delegation Trust)
- **Webb's Depth of Knowledge** model adapted for engineering skill acquisition
- Practical experience calibrating AI agent behavior for growth-oriented engineering work

Created by [Dakota Fabro](https://github.com/dakotafabro)

## License

MIT - see [LICENSE](./LICENSE)

# learning-mode

A behavioral skill for AI agents that shifts them from "do it for you" to "do it with you" - optimizing for skill building over shipping speed.

## What This Does

Learning Mode gives your AI agent a different objective: maximize YOUR understanding, not minimize time-to-merge. It calibrates scaffolding to your current depth of knowledge, progressively reducing support as you grow. Covers both feature builds (learning while coding) and PR reviews (learning while reading code).

## Install

```bash
npx skills add dakotafabro/learning-mode -g
```

## Quick Start

1. Install the skill
2. Copy `dok-tracker.template.md` to your working repo and fill in your skills
3. Add your config to your agent hints (see Configuration section in SKILL.md)
4. Say `"learning mode"` to activate

**Key commands:**
- `"learning mode"` - activate for the session
- `"learning mode for [X]"` - activate for a specific skill
- `"ship mode"` - return to normal execution
- `"challenge me"` - get a micro-challenge
- `"where am I?"` - see your current DOK levels
- `"explain that"` - agent unpacks its last decision

## Philosophy

The best engineers aren't the ones who ship fastest with AI help. They're the ones who use AI help to become better engineers. Speed comes from understanding. Understanding comes from doing the work yourself, with the right scaffolding at the right time.

Learning Mode turns your AI agent into the senior engineer sitting next to you - not grabbing the keyboard, but asking the right questions and knowing when to let you struggle productively versus when to unblock you.

## Documentation

See [SKILL.md](./SKILL.md) for the full protocol, including:
- The 4-Tier Expert Engineer Model
- DOK calibration and graduation signals
- The Learning Mode Contract
- PR Review in Learning Mode
- Session logging format
- Configuration guide

## Credits

Built on:
- The **Three Dimensions of AI Collaboration** framework (Compression of Intent, Depth of Knowledge, Relational Posture)
- **Webb's Depth of Knowledge** model adapted for engineering skill acquisition
- Practical experience calibrating AI agent behavior for growth-oriented engineering work

## License

MIT - see [LICENSE](./LICENSE)

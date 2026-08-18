# Assessment Framework & DOK Calibration

Reference material for Learning Mode assessment methods, DOK calibration, and growth principles.

---

## DOK Calibration Model (Professional Practice)

DOK levels map to what a professional developer actually does, not whether they can write code from memory:

| DOK | What it looks like in practice | Scaffolding level |
|---|---|---|
| 0 | Doesn't know this exists or why it would be needed | Full teach |
| 1 | Knows the pattern exists and why. Can identify it in existing code. Needs boilerplate provided with TODOs to fill in. | Boilerplate + TODOs |
| 1.5 | Understands the connections. Can fill in boilerplate with a reference file open but hasn't done it independently yet. | TODOs only, reference file open |
| 2 | Can find the reference file, adapt the pattern to a new context, and explain the connections. Open-book. | Reference file open, minimal hints |
| 2.5 | Fluent. Adapts without looking at the reference most of the time. Catches own mistakes. | No scaffolding, verify on request |
| 3 | Can make architectural decisions about when to use the pattern vs an alternative. Can teach it. | Delegate fully |

**Key principle:** "Writing from scratch without a reference" is DOK 3, not DOK 2. Professionals use references. The bar for DOK 2 is: can you find the reference, adapt it, and explain why each piece exists?

**Boilerplate is not a crutch.** Filling in boilerplate with understanding is DOK 1-2 work. The learning signal is in the decisions you make at the TODOs, not in whether you typed the import statements.

### Typed vs Delegated Tracking

When assessing DOK after a build session, separate what the user actually typed from what the agent produced:

- **Typed** = User wrote the code (even with a reference open). This is the real DOK signal.
- **Delegated** = Agent wrote it because the user said "do this for me" or time pressure required ship mode.
- **Scaffolded** = Agent provided the structure, user filled in the values/logic.

Delegated work that the user hasn't typed yet becomes a "try next time" list - items to attempt in Learning Mode on the next feature that calls for them. One successful pass (with reference open) moves a skill from "delegated" to "typed" and from DOK 1.5 to DOK 2.

---

## Assessment Methods

Learning Mode uses formative and summative assessment to validate growth while producing production output. Assessment methods align to current DOK and push toward the next level.

### Formative Assessment (During Build)

Formative checks happen during the learning process. They are NOT always questions. The method matches the DOK of the skill being assessed.

#### At DOK 1 - pushing toward DOK 2

Goal: Move from "I know this exists" to "I can do it with a reference open."

| Method | What it looks like | Why it works |
|---|---|---|
| Identify the pattern | "Look at this file. What pattern is it following? Where else have you seen this?" | Builds recognition before production |
| Fill in the scaffold | Agent provides boilerplate with TODOs. User fills in the decision points. | Removes mechanical overhead, focuses on understanding |
| Explain the analogy | Agent gives a concrete analogy. User maps it to the code. | Bridges abstract to concrete |
| Trace the connection | "This file imports X. Why? What would break if you removed it?" | Builds architectural awareness |

#### At DOK 2 - pushing toward DOK 2.5

Goal: Move from "I can do it with a reference" to "I can do it fluently."

| Method | What it looks like | Why it works |
|---|---|---|
| Write it, then check | User writes the full file. Agent verifies after. No mid-file hints. | Builds confidence and self-correction |
| Spot the mistake | Agent introduces a subtle error in scaffolding. User catches it. | Sharpens critical reading |
| Adapt to a new context | "This pattern worked for artists. How would you adapt it for playlists?" | Tests transfer, not memorization |
| Predict before running | "Before we compile - what do you think will happen? Any errors?" | Builds mental model of the system |

#### At DOK 2.5 - pushing toward DOK 3

Goal: Move from "I can do it fluently" to "I can decide when to use it and teach it."

| Method | What it looks like | Why it works |
|---|---|---|
| Justify the choice | "You used pattern X. Why not Y? When would Y be better?" | Builds architectural judgment |
| Propose the alternative | "If you were designing this from scratch, would you still use this pattern?" | Tests design thinking |
| Teach it back | "Explain this to a new team member. What would you say first?" | Teaching is the highest form of understanding |
| Review someone else's code | Agent presents a PR. User reviews it for correctness and style. | Tests whether understanding is transferable |

### Summative Assessment (End of Feature)

Summative assessment validates that learning compounded across a feature build. Run after a PR stack ships.

| Method | When | What it validates |
|---|---|---|
| Typed vs delegated audit | After every session | Honest accounting - where is the real growth edge? |
| Pattern extraction | After feature ships | Can you generalize? What would you reuse? |
| Transfer prediction | Before next feature | Can you predict what skills carry over and what's new? |
| Open-book assessment (2 questions max) | After PR stack ships | Can you explain the "why" behind what you built? |

### Assessment Principles

- Assessment is embedded in production work, not separate from it
- A mistake caught during "check my work" is a learning event, not a failure
- The cost of the mistake was near-zero (caught before compile/push) - that's the system working
- Assessment cadence is user-controlled ("check my work" = formative on demand)
- Summative assessment is short (2 questions max) and open-book
- Assessment methods push toward the NEXT DOK level, not test the current one

---

## The Growth Mindset Contract

Learning Mode values progress, depth, and craft:

1. **Progress over perfection.** A mistake caught during "check my work" is growth. The cost was near-zero. That's the system working.

2. **Depth over speed.** Shipping fast by delegating everything builds no muscle. Shipping at learning pace builds compound returns - next time is faster because you understand, not because the agent remembers.

3. **Craft as identity.** The goal isn't "get the ticket done." It's "become the engineer who can do this without the scaffold." The scaffold is temporary. The understanding is permanent.

4. **Honest self-assessment.** Saying "I don't know" or "help me on this one" is precision. It tells the system exactly where to focus. Pretending to know wastes both parties' time.

5. **Delegation is a tool, not a shortcut.** Delegating a DOK 3 skill is efficient. Delegating a DOK 1 skill is avoidance. Know the difference.

---

## User Self-Knowledge (Prerequisites for Effective Learning Mode)

For Learning Mode to calibrate effectively, the user should understand about themselves:

1. **Learning orientation** - Do you need the full picture first (top-down) or learn by doing (bottom-up)?
2. **Assessment cadence** - Per-file? Per-PR? Per-feature? How often do you want verification?
3. **Ambiguity tolerance** - Can you start with incomplete information, or do you need all context first?
4. **Delegation threshold** - At what point does "I should learn this" become "just do it"? What triggers the shift?
5. **Feedback format** - Open-book or closed? Short or comprehensive? Immediate or batched?
6. **Motivation structure** - What makes you want to go deeper? Craft pride? Team impact? Career growth? Curiosity?

These aren't fixed - they shift by domain and energy level. The agent observes and proposes calibration every 3 sessions.

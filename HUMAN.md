# learning-mode - what changes for you

learning-mode changes what the agent is trying to do. Instead of getting the code written fast, it tries to leave you more capable at the end of the session.

## What it does to the agent

For skills you've marked low in your DOK tracker (DOK 1 to 2), the agent guides instead of executing. It asks "what would you try?" before showing an answer, offers 5 to 15 minute micro-challenges, and runs four checkpoints in a build: task comprehension, concept connection, thinking challenges and an understanding check. In PR reviews it explains context first. It adjusts per skill, so you can get light touch in one area and heavy scaffolding in another in the same session. If a low skill hasn't been touched in 14 days, it may open with one recall question.

## When to use it

When you're growing into a new language, platform or pattern and have time to go slower. The skill itself says: if the deadline is tomorrow, that's not the time.

## Reserved for human judgment

Your DOK levels and tiers are yours to set and update. When the agent says you might be ready for the next tier, you decide. A missed answer in a challenge is useful data, not a failure.

## What it reads, writes and sends

- Reads a `dok-tracker.md` you copy from the template and keep in your own repo, plus an optional session log.
- You configure paths in a config block in your AGENTS.md or CLAUDE.md, never in the installed skill files.
- Network use: not documented.

## Cost

About 4,200 tokens of context (`token_cost` in bpm.json), the largest of these packages.

## Check it's working

Say "learning mode" on a task in a low-DOK area. The agent should ask what you'd try before writing code.

## Turn it off

Say "ship mode" to return to normal execution for the session. To remove it, `bpm remove learning-mode`.

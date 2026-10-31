# Changelog

## 1.4.1 (2026-10-31)
- `scripts/validate.py` reads the personal references it checks for from a local file outside the package (`~/.config/learning-mode/personal-refs.txt`, one term per line, or the path in `LEARNING_MODE_PERSONAL_REFS`) and skips that check when the file is missing.
- `bpm.json`: version 1.4.1.

**What changes for you:** nothing in how learning mode works. If you run the validator, put your own terms in that file.

## 1.4 (2026-09-26)
- Tier 2 (Judgment) options are presented as a **possibility matrix**: one row per option with a "Holds if" premise, the learner's prior answer as a row, an "unsure / check first" row, and "What row is missing?". The full convention lives in the `possibility-matrix` package, with a human counterpart (`HUMAN.md`).
- New command: "give me the options".
- `bpm.json`: version 1.4.0 (was 1.2.0), `possibility-matrix` added as a peer.

**What changes for you:** when you face a judgment call, you'll get a table of options with premises instead of a single recommendation. Check the premises, then pick. See `possibility-matrix/HUMAN.md`.

## 1.3 (2026-08-18)
- PR review as inverse build.
- Convention-derived review checklist.

## 1.2 (2026-08-17)
- Assessment framework, DOK calibration model, growth mindset contract, user self-knowledge.

## 1.1 (2026-08-06)
- Build checkpoints, retrieval decay, adaptive intensity, teaching back, session close reflection.

## 1.0 (2026-07-27)
- Initial release.

#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIR="$REPO_ROOT/dist"

mkdir -p "$OUTPUT_DIR"

cd "$REPO_ROOT"
zip -r "$OUTPUT_DIR/learning-mode.skill" \
  SKILL.md \
  dok-tracker.template.md \
  LICENSE \
  -x "*.DS_Store"

echo "Packaged: $OUTPUT_DIR/learning-mode.skill"

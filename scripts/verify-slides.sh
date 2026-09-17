#!/bin/sh
# Verify that each given presenterm markdown file can be exported to PDF
# without error. Used by `make verify`, the pre-commit hook, and CI.
#
# presenterm needs a terminal of known size to lay out slides, even when
# just exporting to PDF, so each file is run inside its own detached tmux
# session rather than directly, which works headlessly (CI, git hooks).
#
# Usage: scripts/verify-slides.sh FILE...

set -u

if [ "$#" -eq 0 ]; then
    exit 0
fi

for cmd in presenterm weasyprint tmux; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "verify-slides: '$cmd' not found in PATH" >&2
        exit 1
    fi
done

status=0

for f in "$@"; do
    echo "Verifying $f..."
    tag="verify-slides-$$-$(echo "$f" | tr -c 'A-Za-z0-9' '_')"
    logfile=$(mktemp)
    exitfile=$(mktemp)

    tmux new-session -d -x 220 -y 50 -s "$tag" \
        "presenterm --export-pdf -o /dev/null '$f' >'$logfile' 2>&1; echo \$? >'$exitfile'; tmux wait-for -S '$tag'"
    tmux wait-for "$tag"

    code=$(cat "$exitfile")
    if [ "$code" != "0" ]; then
        echo "FAILED: $f" >&2
        cat "$logfile" >&2
        status=1
    fi

    rm -f "$logfile" "$exitfile"
done

exit $status

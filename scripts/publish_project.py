"""Publish one generated project card without losing concurrent catalogue updates."""
import os
from pathlib import Path
import subprocess
import sys
import time

import index_project

ROOT = Path(__file__).resolve().parents[1]
MAX_ATTEMPTS = 5
BACKOFF_SECONDS = (1, 2, 4, 8)
RETRYABLE_PUSH_ERRORS = (
    "fetch first",
    "non-fast-forward",
    "failed to push some refs",
    "remote end hung up unexpectedly",
    "unexpected disconnect",
    "connection reset",
    "connection timed out",
)


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True
    )


def require_success(result, action):
    if result.returncode:
        raise RuntimeError(f"{action} failed: {result.stderr.strip() or result.stdout.strip()}")
    return result


def publish(card, branch, issue_number, sleep=time.sleep):
    relative = Path(card)
    if relative.is_absolute() or not relative.parts or relative.parts[0] != "projects":
        raise ValueError("CARD must point to a generated file under projects/")
    root = ROOT.resolve()
    card_path = (root / relative).resolve()
    projects = (root / "projects").resolve()
    if projects not in card_path.parents or not card_path.is_file():
        raise ValueError("Generated project card is missing or outside projects/")
    card_content = card_path.read_bytes()

    require_success(git("config", "user.name", "github-actions[bot]"), "Configure Git author")
    require_success(git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"), "Configure Git author")

    for attempt in range(MAX_ATTEMPTS):
        require_success(git("fetch", "origin", branch), "Fetch latest catalogue")
        # Keep this run's generated card outside the checkout while resetting to
        # the new tip. If another run published the same project, its card wins.
        card_path.unlink(missing_ok=True)
        require_success(git("reset", "--hard", "FETCH_HEAD"), "Reset to latest catalogue")
        if not card_path.exists():
            card_path.parent.mkdir(parents=True, exist_ok=True)
            card_path.write_bytes(card_content)

        index_project.build_index(root)
        require_success(git("add", "--", "projects/"), "Stage project catalogue")
        staged = git("diff", "--cached", "--quiet")
        if staged.returncode == 0:
            return
        if staged.returncode != 1:
            require_success(staged, "Check staged catalogue")

        require_success(git("commit", "-m", f"Index project from issue #{issue_number}"), "Commit project catalogue")
        pushed = git("push", "origin", f"HEAD:{branch}")
        if pushed.returncode == 0:
            return

        detail = pushed.stderr.strip() or pushed.stdout.strip()
        retryable = any(marker in detail.lower() for marker in RETRYABLE_PUSH_ERRORS)
        if not retryable or attempt == MAX_ATTEMPTS - 1:
            raise RuntimeError(f"Publish failed after {attempt + 1} attempt(s): {detail}")
        sleep(BACKOFF_SECONDS[attempt])

    raise RuntimeError("Publish retries exhausted")


def main():
    publish(
        os.environ["CARD"],
        os.environ["DEFAULT_BRANCH"],
        int(os.environ["ISSUE_NUMBER"]),
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"::error::{exc}", file=sys.stderr)
        raise

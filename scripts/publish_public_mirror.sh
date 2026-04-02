#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

: "${PUBLIC_REPO:?PUBLIC_REPO is required}"

PUBLIC_BRANCH="${PUBLIC_BRANCH:-main}"
AUTHOR_NAME="${AUTHOR_NAME:-github-actions[bot]}"
AUTHOR_EMAIL="${AUTHOR_EMAIL:-41898282+github-actions[bot]@users.noreply.github.com}"
PUBLISH_MESSAGE="${PUBLISH_MESSAGE:-Public snapshot}"

tmpdir="$(mktemp -d)"
cleanup() {
  rm -rf "$tmpdir"
}
trap cleanup EXIT

git init --initial-branch "$PUBLIC_BRANCH" "$tmpdir/repo" >/dev/null 2>&1 || {
  git init "$tmpdir/repo" >/dev/null
  git -C "$tmpdir/repo" checkout -b "$PUBLIC_BRANCH" >/dev/null 2>&1
}

rsync -a --delete \
  --exclude ".git" \
  "$ROOT/" "$tmpdir/repo/"

git -C "$tmpdir/repo" add -A

if git -C "$tmpdir/repo" diff --cached --quiet; then
  echo "No files to publish"
  exit 0
fi

git -C "$tmpdir/repo" \
  -c user.name="$AUTHOR_NAME" \
  -c user.email="$AUTHOR_EMAIL" \
  commit -m "$PUBLISH_MESSAGE" >/dev/null

git -C "$tmpdir/repo" remote add origin "$PUBLIC_REPO"
git -C "$tmpdir/repo" push --force origin "$PUBLIC_BRANCH"

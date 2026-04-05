#!/usr/bin/env bash
set -euo pipefail

part="${1:?Usage: $0 <major|minor|patch>}"

# Extract the current version from `pyproject.toml`.
current=$(grep '^version = ' pyproject.toml | cut -d'"' -f2)
if [[ -z "$current" ]]; then
    echo "Error: could not extract version from pyproject.toml."
    exit 1
fi

IFS='.' read -r major minor patch <<< "$current"

case "$part" in
    major) new="$((major + 1)).0.0" ;;
    minor) new="${major}.$((minor + 1)).0" ;;
    patch) new="${major}.${minor}.$((patch + 1))" ;;
    *) echo "Error: invalid part '$part'. Must be one of: major, minor, patch."; exit 1 ;;
esac

echo "Bumping version: $current -> $new"

# Update the version in `pyproject.toml`.
sed -i'' -e "s/^version = \"$current\"/version = \"$new\"/" pyproject.toml

# Sync the lockfile with the new version.
uv lock

# Stage, commit, tag, and inform the user.
git add pyproject.toml uv.lock
git commit -m "Bump version to $new"
git tag -a "$new" -m "Release $new"

echo "Done. Run the following to push:"
echo "  git push --atomic origin main $new"

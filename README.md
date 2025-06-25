# Semantic Versioning Script for CI/CD

This repository contains a Python script to manage semantic versioning for your application. It is intended to be used as a centralized tool, cloned by your main CI/CD pipeline.

## Files

- `semver.py`: A Python script to increment a version number (major, minor, or patch). It supports version prefixes (e.g., `v`).
- `VERSION`: An example file to store the current version of an application (e.g., `v0.0.0`).

## How it works

The `semver.py` script reads a version from a specified file, increments it based on the provided argument (`major`, `minor`, or `patch`), and writes the new version back to the file.

### Arguments
- `bump_type`: (Required) The type of version bump. Choices: `major`, `minor`, `patch`.
- `--version-file`: The path to the version file. Defaults to `VERSION`.
- `--tag-prefix`: A prefix for the version string (e.g., `v`). Defaults to no prefix.

## Usage in your CI/CD pipeline

In your main application's repository, your CI/CD workflow should:
1. Check out your application's code.
2. Check out this repository (`github-actions-utils`) into a subdirectory.
3. Run the `semver.py` script to bump the version in your application's `VERSION` file.
4. Commit the new version back to your application's repository and create a git tag.

### Example Workflow

Here is an example of a GitHub Actions workflow in your application's repository (`.github/workflows/release.yml`):

```yaml
name: Create Release

on:
  workflow_dispatch:
    inputs:
      bump_type:
        description: 'Type of version bump'
        required: true
        type: choice
        options:
        - patch
        - minor
        - major
        default: 'patch'

jobs:
  create_release:
    runs-on: ubuntu-latest
    steps:
      - name: Check out application code
        uses: actions/checkout@v3
        with:
          # A personal access token with repo scope is required to push changes back
          token: ${{ secrets.GH_TOKEN }}

      - name: Check out versioning tools
        uses: actions/checkout@v3
        with:
          repository: <your-org>/github-actions-utils
          path: ./.github/github-actions-utils

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Bump version and create tag
        id: bump_version
        run: |
          python ./.github/github-actions-utils/semver.py ${{ github.event.inputs.bump_type }} --version-file VERSION --tag-prefix v
          
          NEW_VERSION=$(cat VERSION)
          echo "new_version=$NEW_VERSION" >> $GITHUB_OUTPUT

          # Commit and push new version
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add VERSION
          git commit -m "Bump version to $NEW_VERSION"
          git tag $NEW_VERSION
          git push
          git push origin $NEW_VERSION

      - name: Build and push Docker image
        # ... your build and push steps ...
        run: |
          echo "Building Docker image with tag ${{ steps.bump_version.outputs.new_version }}"
          # Example: docker build -t my-image:${{ steps.bump_version.outputs.new_version }} .
``` 
# GitHub Actions Utilities

This repository contains a collection of shared utilities for GitHub Actions pipelines. These utilities are designed to be reused across different projects to standardize and simplify common CI/CD tasks.

## Contents

- **Versioning**: Tools for semantic versioning management
  - Automatically increment version numbers (major, minor, patch)
  - Support for version prefixes
  - Docker image tagging

## How to Use

Each utility is stored in its own directory with specific documentation. To use these utilities in your GitHub Actions workflows:

1. Check out your application's code
2. Check out this repository into a subdirectory of your project
3. Use the specific utility as described in its documentation

### Example

```yaml
- name: Check out application code
  uses: actions/checkout@v3

- name: Check out GitHub Actions utilities
  uses: actions/checkout@v3
  with:
    repository: danieltech33/github-actions-util
    path: ./.github/github-actions-util
```

## Contributing

To contribute to this repository:

1. Fork the repository
2. Create a new branch for your feature
3. Add your utility in a dedicated directory with clear documentation
4. Submit a pull request

## License

MIT 
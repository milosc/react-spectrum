# Build and Launch React Spectrum

This project is the Adobe React Spectrum monorepo. It uses Yarn 4 (Berry) and Lerna.

## Completed Tasks

- [x] Initial project analysis

## In Progress Tasks

- [x] Install dependencies
- [x] Build icons and other assets
- [x] Launch development environment (Storybook)

## Future Tasks

- [x] Verify functionality in browser
- [ ] Build production documentation

## Implementation Plan

1.  **Dependency Installation**: Use `yarn install` to set up the environment.
2.  **Building**: Run the build script to ensure all assets (like icons) are generated. Note: `postinstall` already runs `patch-package` and `yarn build:icons`.
3.  **Launching**: Use `yarn start` to launch the Storybook development environment on port 9003.

### Relevant Files

- `package.json` - Project configuration and scripts.
- `yarn.lock` - Dependency lockfile.
- `.storybook/` - Storybook configuration.

# Contributing to WebStarterReact

Thank you for your interest in contributing to WebStarterReact! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Node.js (see [.nvmrc](.nvmrc) for the required version)
- npm or yarn package manager

### Installation

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Web-Starter-React.git
   cd Web-Starter-React
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. (Optional) If you have Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Development

### Running the Development Server

Start the development server with:
```bash
npm run dev
```

The application will be available at `http://localhost:5173` (or the port shown in the terminal).

### Building for Production

Build the project with:
```bash
npm run build
```

### Running Tests

Run the test suite with:
```bash
npm test
```

## Contributing Guidelines

### Code Style

- Follow the existing code style in the project
- Use Prettier for code formatting (if configured)
- Use ESLint rules (if configured)
- Write clear, concise, and well-documented code

### Pull Requests

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure tests pass

3. Commit your changes with clear commit messages:
   ```bash
   git commit -m "Add: brief description of changes"
   ```

4. Push your changes and create a pull request

### Commit Message Convention

## Format:

```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```


#### Commit Message Structure:

*   **`<type>`:** Describes the kind of change that this commit is providing.
    *   `feat`: A new feature
    *   `fix`: A bug fix
    *   `docs`: Documentation only changes
    *   `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.)
    *   `refactor`: A code change that neither fixes a bug nor adds a feature
    *   `perf`: A code change that improves performance
    *   `test`: Adding missing tests or correcting existing tests
    *   `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    *   `ci`: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
    *   `chore`: Other changes that don't modify src or test files
    *   `revert`: Reverts a previous commit

*   **`<scope>` (optional):** A noun describing the section of the codebase affected. For example: `parser`, `compiler`, `api`, `auth`, `ui`, `docs`.

*   **`<short summary>`:** A very brief description of the change.
    *   Use the imperative, present tense: "change" not "changed" nor "changes"
    *   Don't capitalize the first letter
    *   No period (`.`) at the end

*   **`[optional body]`:** A longer explanation of the commit message.
    *   Use the imperative, present tense.
    *   Explain *what* and *why* the changes were made.

*   **`[optional footer(s)]:** Used for referencing issues or breaking changes.
    *   `BREAKING CHANGE:`: Indicate backward-incompatible changes.
    *   `Closes #<issue-number>`: Reference a GitHub issue that the commit closes.

## Example:

```
feat(authentication): add user login functionality

This commit introduces the user login functionality, allowing users to authenticate
using their email and password. It integrates with AWS Cognito for secure
authentication.

Closes #123
```

This documentation ensures that all contributors maintain a consistent and readable commit history.

### Issues

- Check existing issues before creating new ones
- Use issue templates if provided
- Provide detailed descriptions with steps to reproduce

## Project Structure

```
src/
├── components/     # Reusable UI components
├── layouts/        # Layout components
├── pages/         # Page components
├── store/         # Redux store and slices
├── styles/        # Global styles
└── main.tsx       # Application entry point
```

## Additional Resources
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Redux Toolkit](https://redux-toolkit.js.org/)
- [Tailwind CSS](https://tailwindcss.com/)

Thank you for contributing!

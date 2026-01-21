# Git Commit Format

## Commit Message Structure

```
<type>: <subject>

<description>

<files>
- <file_path>: <change_description>
</files>

<test_results>
- <test_description>: <result>
</test_results>
```

## Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

## Example

```
feat: Implement JWT handling for authentication

Added comprehensive JWT handling for both backend and frontend to enable secure authentication.

<files>
- backend/backend/app/core/config.py: Added cognito_jwks_url property for JWT validation
- backend/backend/app/core/security.py: Created JWT validation logic and FastAPI Depends
- backend/backend/app/main.py: Imported security dependency and added protected endpoint
- ui/src/services/auth.ts: Created auth service with token storage and refresh
- ui/src/main.tsx: Initialized Axios interceptors for automatic JWT handling
- ui/src/pages/Login.tsx: Updated to use authService.login() for better token management
</files>

<test_results>
- Token storage in localStorage: ✅ Working
- Authenticated requests with access_token: ✅ Working
- Automatic token refresh on 401: ✅ Working
- Protected backend endpoint /users/me: ✅ Working
- Logout and redirect on refresh failure: ✅ Working
</test_results>

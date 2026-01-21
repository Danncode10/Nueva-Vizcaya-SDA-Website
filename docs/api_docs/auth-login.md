# POST /auth/login

Authenticates a user with email and password, returning JWT tokens for API access.

## Analogy
Like showing your ID card at the entrance of a building. If the guard verifies it's correct, they give you a visitor badge that lets you access different rooms.

## Request

**Method:** `POST`  
**Endpoint:** `/auth/login`  
**Content-Type:** `application/json`

### Request Body
```json
{
  "email": "john@example.com",
  "password": "mypassword123"
}
```

### Field Descriptions
- `email` (string, required): User's email address
- `password` (string, required): User's password

## Response

### Success Response (200)
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Token Explanations:**
- `access_token`: Short-lived token (usually 15-60 minutes) used for API requests
- `refresh_token`: Long-lived token (days/weeks) used to get new access tokens

### Error Responses

**Invalid Credentials (400)**
```json
{
  "detail": "Login failed: Incorrect username or password."
}
```

**Account Not Approved (400)**
```json
{
  "detail": "Login failed: Account pending approval."
}
```

## Process Flow

1. User enters email/password on login page
2. Frontend sends this API request
3. Backend sends credentials to AWS Cognito
4. Cognito verifies the user exists and password is correct
5. Backend checks if user account is approved
6. If approved, backend returns JWT tokens
7. Frontend stores tokens in browser localStorage
8. User is now logged in and can access protected features

## Authentication Flow

```mermaid
graph TD
    A[User enters credentials] --> B[Frontend calls /auth/login]
    B --> C[Backend sends to AWS Cognito]
    C --> D{Credentials valid?}
    D -->|Yes| E[Check approval status]
    D -->|No| F[Return login failed]
    E --> G{Approved?}
    G -->|Yes| H[Return JWT tokens]
    G -->|No| I[Return account pending]
    H --> J[Frontend stores tokens]
    J --> K[User logged in]
```

## Testing

### With curl
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "approved.user@example.com",
    "password": "correctpassword"
  }'
```

### With the Website
1. Go to `/login` page
2. Enter your email and password
3. Click "Sign in"
4. If successful, you'll be redirected to the main page

## Using the Tokens

Include the access token in API requests:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## Token Expiration

- Access tokens expire quickly (security feature)
- Use refresh token to get new access token via `/auth/refresh`
- Store tokens securely in browser localStorage
- Never share tokens or store in insecure locations

## Security Notes

- Passwords are never sent in plain text over the network
- AWS Cognito handles secure password verification
- JWT tokens are cryptographically signed
- Failed login attempts are logged for security monitoring

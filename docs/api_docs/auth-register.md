# POST /auth/register

Creates a new user account that requires approval before the user can login.

## Analogy
Imagine applying for a library card. You fill out a form with your information and choose which types of books you want to borrow (roles). Then you pick a librarian who will check and approve your application.

## Request

**Method:** `POST`  
**Endpoint:** `/auth/register`  
**Content-Type:** `application/json`

### Request Body
```json
{
  "email": "john@example.com",
  "password": "mypassword123",
  "approver_id": 5,
  "intended_roles": ["member", "youth"]
}
```

### Field Descriptions
- `email` (string, required): User's email address, used as username
- `password` (string, required): User's password (must be secure)
- `approver_id` (integer, required): ID of the pastor/admin who will approve this account
- `intended_roles` (array of strings): Roles the user wants (e.g., "member", "youth", "elder", "pastor")

## Response

### Success Response (201)
```json
{
  "message": "Registration request sent",
  "user_id": 123
}
```

### Error Responses

**User Already Exists (400)**
```json
{
  "detail": "User already exists"
}
```

**Invalid Approver (400)**
```json
{
  "detail": "Invalid approver"
}
```

**Missing Fields (422)**
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Process Flow

1. User fills out registration form on website
2. Frontend sends this API request
3. Backend checks if email is already registered
4. Backend verifies the approver exists
5. Backend creates user record with "pending" approval status
6. Backend assigns default "member" role
7. Backend sends notification to approver (TODO)
8. User sees "pending approval" message
9. Approver reviews and approves/rejects the request
10. Once approved, user can login

## Testing

### With curl
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "securepass123",
    "approver_id": 1,
    "intended_roles": ["member"]
  }'
```

### With the Website
1. Go to `/register` page
2. Fill out the form
3. Select roles by clicking the colored chips
4. Search for and select an approver
5. Click "Register"

## Notes

- The account cannot be used for login until approved by the selected approver
- Passwords are securely hashed, never stored in plain text
- Intended roles are stored but user gets default "member" role initially
- Approver must have "pastor" or "admin" role to approve registrations

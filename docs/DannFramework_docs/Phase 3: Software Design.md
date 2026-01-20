# **PHASE 3 — Software Design**

## 3.1 High-Level Design (HLD)

**Questions**

* What architecture style?
* What are major modules?
* How does data flow?

**Answers**

* **Architecture Style:** Three-tier web application architecture with separation of concerns - presentation layer (React frontend), application layer (FastAPI backend), and data layer (PostgreSQL database + AWS S3 storage). Initially monolithic for simplicity, designed to scale to microservices.
* **Major Modules:**
  - **Frontend Module:** React-based user interface handling user interactions, displaying content, and API communication
  - **Backend API Module:** FastAPI-based REST API handling business logic, authentication, and data processing
  - **Database Module:** PostgreSQL relational database for structured data storage
  - **File Storage Module:** AWS S3 for media files, documents, and uploads
  - **Authentication Module:** AWS Cognito integration for user management and access control
  - **Admin Module:** Dashboard for content management, user administration, and role verification
* **Data Flow:**
  1. User interacts with React frontend
  2. Frontend makes API calls to FastAPI backend
  3. Backend authenticates requests via AWS Cognito
  4. Backend queries/updates PostgreSQL database for structured data
  5. File operations route to AWS S3 for media storage
  6. Backend processes business logic and returns responses
  7. Frontend renders updated UI to user

---

## 3.2 Low-Level Design (LLD)

**Questions**

* Class structures?
* Database schema?
* API endpoints?
* Core algorithms?
* Pseudocode for logic?

**Answers**

* **Class Structures:**
  - **Division Model:** id, name (Northern, Upper, South Eastern, etc.), designated_pastor
  - **User Model:** id, google_id, email, roles[], church_membership, division_assignment, profile_data, approval_status, approver_id
  - **Role Model:** id, name, permissions[]
  - **Church Model:** id, name, location, contact_info, pastor_id, division_id
  - **Event Model:** id, title, description, date, location, created_by, attendees[], church_id, division_id, scope (division/province)
  - **Post Model:** id, title, content, author, tags[], verified_by, publish_date, category, division_id
  - **File Model:** id, filename, s3_key, uploaded_by, file_type, size, division_id
  - **Authentication Service:** Methods for google_oauth_login, register_with_approver, approve_account, search_approvers

* **Database Schema:**
  ```
  divisions (id, name, designated_pastor_id)
  users (id, google_id, email, division_id, church_id, approval_status, approver_id, created_at, updated_at)
  user_roles (user_id, role_id)
  roles (id, name, permissions)
  churches (id, name, address, pastor_id, contact_info, division_id)
  events (id, title, description, event_date, location, created_by, church_id, division_id, scope)
  event_attendees (event_id, user_id)
  posts (id, title, content, author_id, tags, verified_by, publish_date, category, division_id)
  files (id, filename, s3_key, uploaded_by, file_type, size, upload_date, division_id)
  ```

* **API Endpoints:**
  - `GET /public/content` - Get public content (no auth required)
  - `GET /churches` - List churches (public)
  - `GET /events` - List events (public)
  - `GET /events/upcoming` - Get upcoming events (public)
  - `GET /posts` - List blog posts (public)
  - `GET /posts/featured` - Get featured posts (public)
  - `GET /divisions` - List divisions (public)
  - `GET /divisions/{id}/churches` - Get churches in a division (public)
  - `GET /approvers/search?role={intended_role}` - Search eligible approvers by name and intended role (public during registration)
  - `POST /auth/register` - User registration with approver selection
  - `POST /auth/google-login` - Google OAuth login
  - `GET /approvals/pending` - Get pending approval requests (for approvers)
  - `POST /approvals/{id}/approve` - Approve user registration (approver only)
  - `POST /approvals/{id}/reject` - Reject user registration (approver only)
  - `GET /users/profile` - Get user profile (authenticated)
  - `PUT /users/profile` - Update user profile (authenticated)
  - `POST /users/roles/request` - Request role change (authenticated)
  - `POST /events` - Create event (admin only)
  - `POST /posts` - Create post (admin only)
  - `POST /files/upload` - Upload file (authenticated)
  - `GET /files/{id}/download` - Download file (authenticated)

* **Core Algorithms:**
  - **Role-Based Access Control:** Check user roles against required permissions for each endpoint
  - **Content Verification Workflow:** Admin review process for posts and role applications
  - **Dynamic Content Selection:** Algorithm to select featured posts for home page
  - **File Upload Validation:** Check file types, sizes, and user permissions

* **Pseudocode for Logic:**

  **Account Registration & Approval:**
  ```
  function registerUserWithApprover(google_profile, approver_name):
      # Check if user already exists
      existing_user = find_user_by_google_id(google_profile.id)
      if existing_user:
          return error("User already exists")

      # Search for approver by name
      approvers = search_users_by_name(approver_name, roles=["pastor", "admin"])
      if approvers.length == 0:
          return error("No matching approver found")

      # Create user with pending status
      user = create_user({
          "google_id": google_profile.id,
          "email": google_profile.email,
          "approval_status": "pending",
          "approver_id": approvers[0].id  # Select first match
      })

      # Notify approver
      send_notification(approvers[0].id, f"New registration request from {google_profile.email}")

      return {"user_id": user.id, "status": "pending_approval"}

  function approveUserRegistration(approver_id, user_id, approved):
      # Verify approver has permission
      approver = get_user(approver_id)
      if not has_role(approver, ["pastor", "admin"]):
          return error("Not authorized to approve")

      user = get_user(user_id)
      if user.approver_id != approver_id:
          return error("Not the assigned approver")

      if approved:
          user.approval_status = "approved"
          # Assign default member role
          assign_role(user_id, "member")
          send_notification(user_id, "Your account has been approved")
      else:
          user.approval_status = "rejected"
          send_notification(user_id, "Your registration was not approved")

      update_user(user)
      return success

  function searchApprovers(search_term, intended_role = "member"):
      # For pastor applications, only admins can approve
      if intended_role == "pastor":
          return search_users_by_name_and_role(search_term, "admin")
      else:
          # For regular registration, pastors and admins can approve
          pastors = search_users_by_name_and_role(search_term, "pastor")
          admins = search_users_by_name_and_role(search_term, "admin")
          return pastors + admins
  ```

  **User Role Changes:**
  ```
  function requestRoleChange(user_id, new_role):
      user = get_user(user_id)
      if not user.approval_status == "approved":
          return error("Account not approved yet")

      # For non-pastor roles, approve immediately
      if new_role != "pastor":
          assign_role(user_id, new_role)
          send_notification(user_id, f"Role {new_role} assigned")
          return success

      # For pastor role, require approval
      create_role_application(user_id, "pastor", status="pending")
      notify_admins("Pastor role application submitted")
      return {"status": "pending_approval"}
  ```

  **Home Page Content Loading:**
  ```
  function getHomePageContent(user_id = null):
      featured_posts = get_posts(limit=3, order_by="publish_date DESC", featured=true)

      # Get province-wide events (always visible)
      province_events = get_events(where="event_date > now() AND scope = 'province'", limit=3, order_by="event_date ASC")

      upcoming_events = province_events

      # If user is authenticated, add division-specific events
      if user_id is not null:
          user = get_user(user_id)
          division_events = get_events(where="event_date > now() AND scope = 'division' AND division_id = user.division_id", limit=2, order_by="event_date ASC")
          upcoming_events = upcoming_events + division_events

      # Sort by date
      upcoming_events.sort_by_date()

      return {
          "featured_posts": featured_posts,
          "upcoming_events": upcoming_events
      }
  ```

  **File Upload:**
  ```
  function uploadFile(user_id, file, file_type):
      if not has_permission(user_id, "upload"):
          return error("No upload permission")

      if file.size > MAX_SIZE or file.type not in ALLOWED_TYPES:
          return error("Invalid file")

      s3_key = generate_unique_key(file.filename)
      upload_to_s3(file, s3_key)

      file_record = create_file_record({
          "filename": file.filename,
          "s3_key": s3_key,
          "uploaded_by": user_id,
          "file_type": file_type
      })

      return {"file_id": file_record.id, "download_url": generate_download_url(s3_key)}

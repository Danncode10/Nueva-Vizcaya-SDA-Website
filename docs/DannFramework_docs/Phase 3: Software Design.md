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
  - **User Model:** id, email, password_hash, roles[], church_membership, division_assignment, profile_data
  - **Role Model:** id, name, permissions[]
  - **Church Model:** id, name, location, contact_info, pastor_id, division_id
  - **Event Model:** id, title, description, date, location, created_by, attendees[], church_id, division_id, scope (division/province)
  - **Post Model:** id, title, content, author, tags[], verified_by, publish_date, category, division_id
  - **File Model:** id, filename, s3_key, uploaded_by, file_type, size, division_id
  - **Authentication Service:** Methods for login, register, verify_token, check_permissions

* **Database Schema:**
  ```
  divisions (id, name, designated_pastor_id)
  users (id, email, password_hash, division_id, church_id, created_at, updated_at)
  user_roles (user_id, role_id)
  roles (id, name, permissions)
  churches (id, name, address, pastor_id, contact_info, division_id)
  events (id, title, description, event_date, location, created_by, church_id, division_id, scope)
  event_attendees (event_id, user_id)
  posts (id, title, content, author_id, tags, verified_by, publish_date, category, division_id)
  files (id, filename, s3_key, uploaded_by, file_type, size, upload_date, division_id)
  ```

* **API Endpoints:**
  - `POST /auth/register` - User registration
  - `POST /auth/login` - User authentication
  - `GET /users/profile` - Get user profile
  - `PUT /users/profile` - Update user profile
  - `POST /users/roles/request` - Request role change
  - `GET /divisions` - List divisions
  - `GET /divisions/{id}/churches` - Get churches in a division
  - `GET /churches` - List churches
  - `GET /events` - List events
  - `GET /events/upcoming` - Get upcoming events
  - `POST /events` - Create event (admin)
  - `GET /posts` - List blog posts
  - `GET /posts/featured` - Get featured posts for home page
  - `POST /posts` - Create post (admin)
  - `POST /files/upload` - Upload file
  - `GET /files/{id}/download` - Download file

* **Core Algorithms:**
  - **Role-Based Access Control:** Check user roles against required permissions for each endpoint
  - **Content Verification Workflow:** Admin review process for posts and role applications
  - **Dynamic Content Selection:** Algorithm to select featured posts for home page
  - **File Upload Validation:** Check file types, sizes, and user permissions

* **Pseudocode for Logic:**

  **User Role Verification:**
  ```
  function verifyPastorRole(user_id, admin_id):
      application = get_role_application(user_id, "pastor")
      if application.status == "pending":
          application.status = "approved"
          application.verified_by = admin_id
          application.verified_at = now()
          update_user_roles(user_id, add="pastor")
          send_notification(user_id, "Pastor role approved")
      return success

  function requestRoleChange(user_id, new_role):
      if new_role == "pastor":
          create_role_application(user_id, "pastor", status="pending")
          notify_admins("New pastor application")
      else:
          update_user_roles(user_id, add=new_role)
          send_notification(user_id, f"Role {new_role} added")
      return success
  ```

  **Home Page Content Loading:**
  ```
  function getHomePageContent(user_id):
      user = get_user(user_id)
      featured_posts = get_posts(limit=3, order_by="publish_date DESC", featured=true)

      # Get province-wide events
      province_events = get_events(where="event_date > now() AND scope = 'province'", limit=3, order_by="event_date ASC")

      # Get division-specific events for user's division
      division_events = get_events(where="event_date > now() AND scope = 'division' AND division_id = user.division_id", limit=2, order_by="event_date ASC")

      # Combine and sort by date
      upcoming_events = province_events + division_events
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

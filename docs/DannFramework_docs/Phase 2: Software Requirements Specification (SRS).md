# **PHASE 2 — Software Requirements Specification (SRS)**

## 2.1 Functional Requirements

**Answers**

* **Anonymous Content Access:** The system shall allow anonymous users to view public content including church directory, blogs, announcements, events, and lesson studies without registration. Triggered by visiting website. Output: Public content displayed.
* **Optional Authentication:** The system shall prompt users to log in when accessing restricted features like file uploads, profile management, or content creation. Triggered by clicking restricted actions. Output: Login modal or redirect to login page.
* **User Registration with Approval:** The system shall allow users to register using Google account and select an approving pastor/admin during signup. Triggered by user clicking "Register" button. Output: Registration request sent to selected approver.
* **Approver Search:** The system shall provide search functionality for users to find pastors and admins by name during registration. For pastor role applications, only admins shall be searchable as approvers. Triggered by user typing in search field. Output: Filtered list of eligible approvers based on intended role.
* **Account Approval Workflow:** The system shall allow selected pastors/admins to approve or reject registration requests. Triggered by approver reviewing pending requests. Output: User account activated or rejected with notification.
* **User Login:** The system shall allow approved users to log in using Google account. Triggered by approved user clicking "Login" button or prompted by restricted actions. Output: User authenticated, access granted to requested feature.
* **User Profile Management:** The system shall allow users to view and edit their profiles, including personal information, roles, and church membership. Triggered by user accessing profile page. Output: Profile updated, changes reflected across system.
* **Role Management:** The system shall allow approved members to request role changes (youth, health, treasurer) and church membership changes. Triggered by user submitting role/membership change request. Output: Request submitted for approval, notifications sent.
* **Multiple Roles Support:** The system shall support multiple roles per user account. Triggered by role assignments/approvals. Output: User permissions updated based on all assigned roles.
* **Role CRUD API:** The system shall provide admin APIs for creating, reading, updating, and deleting user roles to support extensibility. Triggered by admin actions. Output: Role data managed, user permissions updated.
* **Division Management:** The system shall support province divisions (Northern, Upper, South Eastern, etc.) with designated pastors. Triggered by admin division setup. Output: Division structure with assigned pastors.
* **Church Directory:** The system shall display a directory of all SDA churches in Nueva Vizcaya organized by divisions. Triggered by user navigating to directory page. Output: Hierarchical list of divisions and churches with contact information.
* **Events Management:** The system shall allow admins to create, read, update, and delete events with scope settings (division-specific or province-wide). Triggered by admin actions on events page. Output: Events displayed on calendar with appropriate visibility, notifications sent to relevant users.
* **Home Page Content:** The system shall display featured/random posts and upcoming events on the home page. Triggered by page load. Output: Dynamic content showcasing recent activity and events.
* **Blogs and Announcements:** The system shall allow admins to post blogs and announcements with SDA Fundamental Beliefs tagging, including date posted, author, verification status, and tags. Triggered by admin submitting content. Output: Content published with metadata, visible to users.
* **Lesson Studies:** The system shall provide access to SDA quarterly lesson materials. Triggered by user selecting lesson. Output: Lesson content displayed, study guides available.
* **File Upload/Download:** The system shall allow users to upload and download PowerPoint and resource files. Triggered by user actions on file management. Output: Files stored in AWS S3, accessible to authorized users.
* **Admin Dashboard:** The system shall provide admins with user management, content oversight, and role verification tools. Triggered by admin login with elevated privileges. Output: Dashboard with management controls.

**Example**

> "The system shall allow users to register using email and password."

---

## 2.2 Non-Functional Requirements

**Answers**

* **Performance limits:** Response time <500ms for most operations, support 1000 concurrent users.
* **Security level:** High security with encrypted data transmission, secure authentication, and role-based access control.
* **Scalability needs:** Scale to 1000+ users initially, designed for future growth to province-wide usage.
* **Usability expectations:** Intuitive interface for basic to intermediate tech users, mobile-responsive design.

---

## 2.3 Technical Requirements

**Answers**

* **Preferred programming languages:** Python for backend, JavaScript for frontend.
* **Frameworks:** FastAPI for backend API, React for frontend UI.
* **Database type:** PostgreSQL for relational data, AWS S3 for file storage.
* **APIs required:** AWS Cognito for authentication, potential SDA resource APIs for lesson materials.

---

## 2.4 Constraints

**Answers**

* **Time limit:** Version 1 development within 3-6 months.
* **Budget:** Cost-effective using AWS free tier and basic instances initially.
* **Skill limitations:** Solo developer with full-stack experience.
* **Legal/compliance:** GDPR/CCPA compliance for user data, Philippine data privacy laws.

---

## 2.5 Acceptance Criteria

**Answers**

* **User Registration with Approval:** Successful when user selects approver during signup and registration request is sent.
* **Approver Search:** Successful when typing pastor/admin name returns filtered results.
* **Account Approval Workflow:** Successful when selected approver can approve/reject registration requests with notifications.
* **User Profile Management:** Successful when users can view and edit their profiles, changes persist across sessions.
* **Role Management:** Successful when members can request role changes and admins approve/reject them appropriately.
* **Multiple Roles Support:** Successful when users with multiple roles have appropriate permissions across all roles.
* **Division Management:** Successful when divisions are properly structured with designated pastors and churches are organized hierarchically.
* **Home Page Content:** Successful when featured posts and upcoming events are displayed dynamically on page load.
* **Blogs and Announcements:** Successful when posts display date, author, verification status, and tags correctly.
* **Church Directory:** Successful when all Nueva Vizcaya SDA churches are listed accurately organized by divisions.
* **Events Management:** Successful when events appear on calendar and users receive notifications.
* **File Upload:** Successful when uploaded files are accessible and downloadable by authorized users.

**Example**

> "Login is successful when user reaches dashboard within 1 second."

---

## 2.6 Tech Stack Selection (AWS-First)

**Answers**

* **Frontend:** React for responsive UI.
* **Backend:** FastAPI for Python-based API development.
* **Database:** PostgreSQL on RDS for structured data.
* **Hosting:** EC2 for initial deployment, scalable to ECS.
* **Domain & DNS:** Custom domain with Route 53 DNS management.

**Suggested Guide**

> Start simple: Monolith + EC2 + RDS
> Scale later: Microservices + ECS

---

## 2.7 Security Design (Service-Oriented)

**Answers**

* **Auth method:** AWS Cognito for user authentication and authorization.
* **IAM roles:** Role-based access for users (Member, Elder, Pastor, etc.).
* **Encryption strategy:** HTTPS for data transmission, encrypted database storage.
* **Secrets storage:** AWS Secrets Manager for sensitive credentials.
* **What to include in .env files:** Non-sensitive configs like ports, non-secret API endpoints.
* **Backup plan:** Automated RDS backups, S3 versioning, regular data exports.

**Suggested Guide**

> Use AWS Cognito, IAM roles, Secrets Manager, CloudWatch

## 2.8 Environment Variables (.env) Questionnaire

**Answers**

* **Required variables:** DATABASE_URL, FRONTEND_URL, AWS_REGION, COGNITO_USER_POOL_ID, S3_BUCKET_NAME, PORT.
* **Sensitive variables:** Database passwords, AWS access keys, Cognito secrets - these are stored in AWS Secrets Manager.
* **Management:** Use .env.example for templates, load secrets from AWS Secrets Manager in production, local .env for development.
* **Sharing process:** Document setup in README, provide .env.example without values, use AWS IAM for access control.

**Suggested Answer Guide**

> "Required variables include DATABASE_URL, FRONTEND_URL, PORT. Sensitive variables are database passwords and AWS keys, stored in AWS Secrets Manager for production. Use .env.example for templates, and document setup in README."

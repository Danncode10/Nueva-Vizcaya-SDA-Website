# **PHASE 2 — Software Requirements Specification (SRS)**

## 2.1 Functional Requirements

**Questions**

* What functions must exist?
* What triggers each function?
* What output is produced?

**Answers**

* **User Registration:** The system shall allow users to register using email and password. Triggered by user clicking "Register" button. Output: User account created, confirmation email sent.
* **User Login:** The system shall allow registered users to log in using email and password. Triggered by user clicking "Login" button. Output: User authenticated, access granted to dashboard.
* **User Profile Management:** The system shall allow users to view and edit their profiles, including personal information, roles, and church membership. Triggered by user accessing profile page. Output: Profile updated, changes reflected across system.
* **Role Management:** The system shall allow members to request role changes (youth, health, treasurer) and church membership changes. Triggered by user submitting role/membership change request. Output: Request submitted for approval, notifications sent.
* **Pastor Role Verification:** The system shall require admin verification for pastor role applications. Triggered by user applying for pastor role. Output: Application submitted to admins, approval/denial notification sent.
* **Multiple Roles Support:** The system shall support multiple roles per user account. Triggered by role assignments/approvals. Output: User permissions updated based on all assigned roles.
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

**Questions**

* Performance limits?
* Security level?
* Scalability needs?
* Usability expectations?

**Answers**

* **Performance limits:** Response time <500ms for most operations, support 1000 concurrent users.
* **Security level:** High security with encrypted data transmission, secure authentication, and role-based access control.
* **Scalability needs:** Scale to 1000+ users initially, designed for future growth to province-wide usage.
* **Usability expectations:** Intuitive interface for basic to intermediate tech users, mobile-responsive design.

---

## 2.3 Technical Requirements

**Questions**

* Preferred programming languages?
* Frameworks?
* Database type?
* APIs required?

**Answers**

* **Preferred programming languages:** Python for backend, JavaScript for frontend.
* **Frameworks:** FastAPI for backend API, React for frontend UI.
* **Database type:** PostgreSQL for relational data, AWS S3 for file storage.
* **APIs required:** AWS Cognito for authentication, potential SDA resource APIs for lesson materials.

---

## 2.4 Constraints

**Questions**

* Time limit?
* Budget?
* Skill limitations?
* Legal/compliance?

**Answers**

* **Time limit:** Version 1 development within 3-6 months.
* **Budget:** Cost-effective using AWS free tier and basic instances initially.
* **Skill limitations:** Solo developer with full-stack experience.
* **Legal/compliance:** GDPR/CCPA compliance for user data, Philippine data privacy laws.

---

## 2.5 Acceptance Criteria

**Questions**

* How do we know this feature works?
* What test confirms success?

**Answers**

* **User Registration:** Successful when new user can log in and access dashboard.
* **User Profile Management:** Successful when users can view and edit their profiles, changes persist across sessions.
* **Role Management:** Successful when members can request role changes and admins approve/reject them appropriately.
* **Pastor Role Verification:** Successful when pastor applications require admin approval and notifications are sent.
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

**Questions**

* Frontend: React / Next.js?
* Backend: FastAPI / Node?
* Database: RDS / DynamoDB?
* Hosting: EC2 / ECS / Lambda?
* Domain & DNS (If Web):

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

**Questions**

* Auth method?
* IAM roles?
* Encryption strategy?
* Secrets storage?
* What to include in .env files?
* Backup plan?

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

**Questions**

* What environment variables are required for the application (e.g., API keys, database URLs, ports)?
* Which variables contain sensitive information (secrets) that should not be committed to version control?
* How will .env files be managed for different environments (development, staging, production)?
* What is the process for sharing .env templates or examples without exposing secrets?

**Answers**

* **Required variables:** DATABASE_URL, FRONTEND_URL, AWS_REGION, COGNITO_USER_POOL_ID, S3_BUCKET_NAME, PORT.
* **Sensitive variables:** Database passwords, AWS access keys, Cognito secrets - these are stored in AWS Secrets Manager.
* **Management:** Use .env.example for templates, load secrets from AWS Secrets Manager in production, local .env for development.
* **Sharing process:** Document setup in README, provide .env.example without values, use AWS IAM for access control.

**Suggested Answer Guide**

> "Required variables include DATABASE_URL, FRONTEND_URL, PORT. Sensitive variables are database passwords and AWS keys, stored in AWS Secrets Manager for production. Use .env.example for templates, and document setup in README."

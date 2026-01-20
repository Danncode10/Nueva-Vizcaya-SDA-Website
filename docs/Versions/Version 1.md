# Version 1: Core Platform with Finished UI
**Framework Compliance:**
*   This version adheres to the "Question-First" principle by clearly defining problem statements, target users, project goals, and scope as outlined in `docs/DannFramework_docs/Phase 1: Project Planning & Problem Definition.md`.
*   It implements a Hybrid SDLC with Waterfall Planning and Agile Development, ensuring a structured yet iterative approach as per `docs/DannFramework_docs/Phase 5: SDLC Strategy.md`.
*   Security and cost-effectiveness are prioritized by leveraging AWS services (Cognito, S3) and self-hosting PostgreSQL on EC2, aligning with `docs/DannFramework_docs/Phase 2: Software Requirements Specification (SRS).md` and `docs/DannFramework_docs/Phase 6: Deployment, Operations & Cost.md`.

## Features:
- Complete user authentication system with extensible role-based access (Pastor, Elder, Treasurer, Member, Youth, with admin capability to add new roles like Music, Communication).
- User profile management with multiple role support.
- Church directory for all Nueva Vizcaya SDA churches.
- Events calendar with full CRUD operations.
- Dynamic home page with featured posts and upcoming events.
- Blogs and announcements section with SDA Fundamental Beliefs tagging, author info, verification status, and tags.
- Lesson Studies hub with SDA quarterly materials.
- File upload/download system for PowerPoints and resources.
- Responsive, polished UI/UX (mobile-first design).
- Basic admin dashboard with role verification (Pastor roles require admin approval).
- Member management with church membership changes.

## Implementation Roadmap:
### Version 1.1.0: Core Authentication & User Management
- **Description:** Establish the foundational user authentication and profile management system, including role-based access and the user registration workflow. (Associated Changelog: `docs/Versions/changelog/V_1_1.md`)
- **Tasks:**
    - Version 1.1.1: User Authentication Setup
        - [x] Create a dedicated IAM account for the project
        - [x] Set up AWS Cognito User Pool for email/password authentication.
        - [x] Install required libraries and create the backend folder
        - [x] Create .env.example file for environment variables
        - [x] Develop backend API endpoints for user registration, login, and token refresh.
        - [ ] Create frontend components for user registration and login forms.
        - [ ] Implement JWT handling (storage, sending, refreshing) for authenticated requests.
        - [ ] Define initial IAM roles for basic user permissions (e.g., Anonymous, Member).
    - Version 1.1.2: User Profile & Role Management
        - [ ] Develop backend API endpoints for user profile CRUD (Create, Read, Update, Delete) operations.
        - [ ] Create frontend components for viewing and editing user profiles.
        - [ ] Implement API endpoints for requesting role changes and church membership updates.
        - [ ] Develop basic admin dashboard UI/UX for approving/rejg new user registrations and role change requests.
        - [ ] Refine database schema for users, roles, and user_roles tables to support multiple roles and approval statuses.

### Version 1.2.0: Church Directory & Division Management
- **Description:** Implement structured management of church divisions and a comprehensive, searchable church directory, including administrative tools for data population. (Associated Changelog: `docs/Versions/changelog/V_1_2.md`)
- **Tasks:
    - Version 1.2.1: Division Structure Implementation
        - [ ] Develop backend API endpoints for division CRUD operations (admin-only).
        - [ ] Create/update database schema for `divisions` table (id, name, designated_pastor_id FK).
        - [ ] Develop admin interface for managing divisions and assigning designated pastors.
        - [ ] Implement frontend components to display divisions.
    - Version 1.2.2: Church Directory Module Development
        - [ ] Develop backend API endpoints for church CRUD operations (admin-only).
        - [ ] Create/update database schema for `churches` table (id, name, address, pastor_id FK, division_id FK).
        - [ ] Implement frontend components to display a hierarchical church directory (divisions > churches > details).
        - [ ] Integrate church data with division management for accurate public listings and search.

### Version 1.3.0: Dynamic Content & Events Management
- **Description:** Develop modules for managing and displaying church events, blogs, and announcements, including tagging and content verification workflows. (Associated Changelog: `docs/Versions/changelog/V_1_3.md`)
- **Tasks:
    - Version 1.3.1: Events Calendar Functionality
        - [ ] Develop backend API endpoints for event CRUD operations (admin-only, with scope settings).
        - [ ] Create/update database schema for `events` (id, title, description, date, location, created_by FK, church_id FK, division_id FK, scope).
        - [ ] Implement frontend calendar component to display events, filterable by scope/division.
        - [ ] Develop frontend forms for creating, editing, and RSVPing to events.
    - Version 1.3.2: Blogs & Announcements System
        - [ ] Develop backend API endpoints for blog post and announcement CRUD operations (admin-only).
        - [ ] Create/update database schema for `posts` (id, title, content, author_id FK, tags, verified_by FK, publish_date, category, division_id FK).
        - [ ] Implement frontend components for displaying posts, including search, filters, and tag cloud.
        - [ ] Develop admin interface for post creation, editing, publishing, and verification.

### Version 1.4.0: Lesson Studies & File Management
- **Description:** Provide access to SDA quarterly lesson materials and implement a secure file upload/download system for resources. (Associated Changelog: `docs/Versions/changelog/V_1_4.md`)
- **Tasks:
    - Version 1.4.1: Lesson Studies Hub
        - [ ] Integrate backend with a source for SDA quarterly lesson materials (e.g., external API or static content storage).
        - [ ] Develop frontend components for browsing and displaying lesson study content.
        - [ ] Implement basic search/filter for lesson studies.
    - Version 1.4.2: File Upload/Download System
        - [ ] Configure AWS S3 bucket for file storage with appropriate access policies.
        - [ ] Develop backend API endpoints for secure file uploads to S3.
        - [ ] Create/update database schema for `files` (id, filename, s3_key, uploaded_by FK, file_type, size, division_id FK).
        - [ ] Implement backend API endpoints for controlled file downloads from S3.
        - [ ] Develop frontend components for uploading and listing downloadable files.

### Version 1.5.0: UI/UX Refinement & Admin Dashboard Expansion
- **Description:** Finalize the user interface and user experience, ensuring responsiveness and polish, and expand the administrative dashboard with core functionalities. (Associated Changelog: `docs/Versions/changelog/V_1_5.md`)
- **Tasks:
    - Version 1.5.1: Overall UI/UX Polish
        - [ ] Conduct comprehensive review of all frontend components for responsiveness (mobile-first).
        - [ ] Implement consistent styling and design across the entire application (Tailwind CSS, if applicable).
        - [ ] Optimize frontend assets for performance (image optimization, lazy loading).
        - [ ] Ensure WCAG 2.1 AA accessibility compliance.
    - Version 1.5.2: Admin Dashboard Core Features
        - [ ] Consolidate user, church, events, and content moderation tools into a unified admin dashboard.
        - [ ] Implement basic analytics display (e.g., number of users, events, posts).
        - [ ] Develop role verification workflow within the admin panel, specifically for Pastor roles requiring approval.

## Summary of Version 1
- **Total Milestones:** 5 major milestones (1.1.0 to 1.5.0), each with 2 sub-components.
- **Final Goal:** Deploy a fully functional, user-friendly, and secure core platform that enables SDA churches in Nueva Vizcaya to manage information, events, and community engagement efficiently, ready for pilot testing and further iterative development.

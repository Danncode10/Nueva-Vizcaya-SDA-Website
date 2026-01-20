# **PHASE 4 — System Modeling (UML)**

## 4.1 Context Model

System Context Diagram (Input, Process, Output arrows and System at the center)

**System Context Diagram:**

```mermaid
graph TD
    AN[Anonymous Visitors] --> S[Nueva Vizcaya SDA<br/>Website System]
    A[SDA Members<br/>Youth, Members, Elders] --> S
    B[SDA Pastors<br/>Division/Church Pastors] --> S
    C[Church Treasurers<br/>Financial Roles] --> S
    D[SDA Admins<br/>System Admins] --> S

    S --> E[AWS Services<br/>Cognito, S3, RDS, EC2]
    S --> F[External SDA Resources<br/>Lesson Materials]

    AN --> G[Public Content Viewing<br/>Church Directory<br/>Events, Blogs, Lessons]
    A --> H[Registration, Login<br/>Profile Management<br/>Event Participation<br/>Content Creation]
    B --> I[Same as Members<br/>+ Church Leadership]
    C --> J[Financial Reporting<br/>Member Management]
    D --> K[Content Management<br/>User Administration<br/>Role Verification]
    E --> L[Authentication<br/>File Storage<br/>Database Operations]
    F --> M[Lesson Materials<br/>Integration]
```

**Key Interactions:**
- **Anonymous Visitors** → System: Public content viewing (church directory, events, blogs, lesson studies) without registration
- **SDA Members & Pastors** → System: Registration, login, profile management, event participation, content creation
- **Church Treasurers** → System: Financial reporting, member management
- **SDA Admins** → System: Content management, user administration, role verification
- **System** → AWS Services: Authentication, file storage, database operations
- **System** → External SDA Resources: Lesson materials integration

## 4.2 Interaction Model

Sequence Diagram

**User Registration & Approval Sequence:**

```mermaid
sequenceDiagram
    participant U as SDA Member
    participant W as Website
    participant D as Database
    participant Ap as Approver

    U->>W: Click "Register with Google"
    W->>U: Redirect to Google OAuth
    U->>W: Return with Google profile
    W->>U: Show approver search form
    U->>W: Type approver name (pastor/admin based on intended role)
    W->>D: Search users by name, filtered by eligible roles for intended user role
    D->>W: Return matching approvers
    W->>U: Display filtered approver list
    U->>W: Select approver
    W->>D: Create user with pending status
    D->>W: Return user ID
    W->>Ap: Send approval notification
    Ap->>W: Review pending requests
    W->>D: Get pending approvals for approver
    D->>W: Return approval requests
    Ap->>W: Approve/Reject request
    W->>D: Update user approval status
    D->>W: Confirm update
    W->>U: Send approval/rejection notification
    U->>W: Login with Google (if approved)
    W->>D: Verify approval status
    D->>W: Return user data
    W->>U: Grant access to full features
```

**Event Creation & Notification Sequence:**

```mermaid
sequenceDiagram
    participant A as SDA Admin
    participant W as Website
    participant D as Database
    participant N as Notification Service
    participant U as Users

    A->>W: Access event creation
    W->>D: Verify admin permissions
    D->>W: Confirm admin status
    A->>W: Submit event details (title, date, scope)
    W->>D: Create event record
    D->>W: Return event ID
    W->>N: Trigger notifications
    N->>D: Get users based on event scope
    D->>N: Return user list
    N->>U: Send event notifications
    U->>N: Acknowledge (optional)
```

**Anonymous Content Access & Optional Authentication Sequence:**

```mermaid
sequenceDiagram
    participant V as Anonymous Visitor
    participant W as Website
    participant D as Database

    V->>W: Visit website
    W->>D: Fetch public content (events, posts, churches)
    D->>W: Return public data
    W->>V: Display public content

    V->>W: Click "Upload File" (restricted action)
    W->>V: Show login prompt/modal
    V->>W: Click "Login"
    W->>V: Redirect to login page
    V->>W: Enter credentials
    W->>D: Verify user authentication
    D->>W: Return user data and permissions
    W->>V: Grant access to upload feature

    Note over V,W: User can now access restricted features
```

**Role Application & Verification Sequence:**

```mermaid
sequenceDiagram
    participant M as Member
    participant W as Website
    participant D as Database
    participant Ad as Admins

    M->>W: Submit pastor role application
    W->>D: Create role application record
    D->>W: Return application ID
    W->>Ad: Send verification notification
    Ad->>W: Review application
    W->>D: Check admin permissions
    D->>W: Confirm admin rights
    Ad->>W: Approve/Reject application
    W->>D: Update role status
    D->>W: Confirm update
    W->>M: Send approval/rejection notification
    W->>D: Update user roles if approved
```

## 4.3 Structural Model

Class Diagram / ER Diagram

**Entity-Relationship Diagram:**

```mermaid
erDiagram
    Divisions ||--o{ Churches : contains
    Divisions ||--o{ Users : has_members
    Divisions ||--o{ Events : hosts
    Divisions ||--o{ Posts : scoped_to
    Divisions ||--o{ Files : scoped_to

    Users ||--o{ User_Roles : has
    Users ||--o{ Events : creates
    Users ||--o{ Event_Attendees : attends
    Users ||--o{ Posts : authors
    Users ||--o{ Files : uploads

    Churches ||--o{ Events : hosts
    Churches ||--o{ Users : has_pastor

    Roles ||--o{ User_Roles : assigned_to

    Events ||--o{ Event_Attendees : has_attendees

    Divisions {
        int id PK
        string name
        int pastor_id FK
    }

    Users {
        int id PK
        string google_id
        string email
        int division_id FK
        int church_id FK
        string approval_status
        int approver_id FK
    }

    Churches {
        int id PK
        string name
        string address
        int pastor_id FK
        int division_id FK
    }

    Events {
        int id PK
        string title
        string description
        datetime event_date
        string location
        int created_by FK
        int church_id FK
        int division_id FK
        string scope
    }

    Posts {
        int id PK
        string title
        text content
        int author_id FK
        json tags
        int verified_by FK
        datetime publish_date
        string category
        int division_id FK
    }

    Files {
        int id PK
        string filename
        string s3_key
        int uploaded_by FK
        string file_type
        int size
        int division_id FK
    }

    Roles {
        int id PK
        string name
        json permissions
    }

    User_Roles {
        int user_id FK
        int role_id FK
    }

    Event_Attendees {
        int event_id FK
        int user_id FK
    }
```

**Key Relationships:**
- Divisions have many Churches, Users, Events, Posts, and Files
- Users belong to Divisions and Churches, have multiple Roles
- Churches have Events and a designated pastor
- Events have attendees and can be scoped to divisions or province-wide
- Users can create Posts and upload Files
- All content supports division-level scoping for proper access control

## 4.4 Behavioral Model

State Machine Diagram

**User Account Approval State Machine:**

```mermaid
stateDiagram-v2
    [*] --> Pending_Approval
    Pending_Approval --> Approved: Approver Approves
    Pending_Approval --> Rejected: Approver Rejects
    Approved --> Active: Login Successful
    Rejected --> [*]
    Active --> [*]
```

**Event Lifecycle State Machine:**

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Published: Publish Event
    Published --> Ongoing: Event Date Reached
    Ongoing --> Completed: Event Completed
    Completed --> Archived: Archive Event
    Archived --> [*]
```

**Post Publication State Machine:**

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Under_Review: Submit for Review
    Under_Review --> Published: Admin Approves
    Under_Review --> Rejected: Admin Rejects
    Rejected --> Draft: Edit & Resubmit
```

**File Upload State Machine:**

```mermaid
stateDiagram-v2
    [*] --> Not_Uploaded
    Not_Uploaded --> Selected: User Selects File
    Selected --> Uploading: Upload Initiated
    Uploading --> Available: Upload Successful
    Available --> Archived: File Deleted/Archived
    Archived --> [*]
```

These UML models provide a comprehensive view of the Nueva Vizcaya SDA Website system architecture, showing how different user types interact with the system, the step-by-step processes, the data relationships, and the state transitions throughout the application lifecycle.

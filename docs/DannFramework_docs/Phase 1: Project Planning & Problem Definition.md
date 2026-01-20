# **PHASE 1 — Project Planning & Problem Definition**

## 1.1 Problem Statement

**Answers**

* **What problem am I solving?** Lack of a centralized digital platform for managing SDA church information, events, resources, and community engagement in Nueva Vizcaya.
* **Who experiences this problem?** SDA church members, pastors, elders, treasurers, youth, and other church leaders in Nueva Vizcaya province.
* **How often does the problem occur?** Continuously, as church management and community engagement are ongoing daily, weekly, and monthly activities.
* **Why is this problem worth solving?** It will improve organization, accessibility, and community engagement for SDA churches, enabling better resource sharing, event coordination, and spiritual growth.
* **What happens if this problem remains unsolved?** Churches continue to rely on manual processes, scattered information, and limited digital reach, leading to reduced community engagement, administrative burden, and missed opportunities for growth and outreach.

**Suggested Answer Guide**

> "SDA church members and leaders in Nueva Vizcaya struggle with managing church information, events, and resources digitally because they lack a centralized online platform. This causes inefficient communication and scattered resources, resulting in reduced community engagement and increased administrative burden."

---

## 1.2 Target Users

**Answers**

* **Who are the primary users?** SDA church members in Nueva Vizcaya province, including regular members, youth, and community participants.
* **Are there secondary users or admins?** Yes, administrators include pastors, elders, and treasurers with elevated access for church management.
* **What is their technical skill level?** Basic to intermediate - comfortable with smartphones and basic web browsing, but may need user-friendly interfaces.
* **What devices do they commonly use?** Primarily smartphones for mobile access, with some desktop computers for administrative tasks.

**Suggested Answer Guide**

> "Primary users are SDA church members and leaders in Nueva Vizcaya with basic to intermediate level of technical skill, mostly using smartphones and computers."

---

## 1.3 Project Goals (Version 1 Focus)

**Answers**

* **What is the single most important outcome?** Successful deployment of a functional platform that SDA churches in Nueva Vizcaya can use for daily operations.
* **What must the system do *perfectly*?** User authentication, role-based access, and core functionalities like church directory, events calendar, and content management.
* **What can be ignored for now?** Advanced features like AI automation, mobile apps, and enterprise-level analytics.

**Suggested Answer Guide**

> "Version 1 succeeds if users can manage church information, events, and resources without advanced AI or mobile features."

---

## 1.4 Competition & Market Scan

**Answers**

* **What existing solutions exist?** Church Community Builder, Breeze ChMS, Planning Center, Fellowship One, and ACS Technologies.
* **What features do they offer?** Member management, event planning, donation tracking, communication tools, and basic website builders.
* **What do users complain about?** High costs, complex interfaces, limited mobile support, and lack of SDA-specific content integration.
* **What feature is missing or poorly done?** SDA-specific features like Sabbath School lesson integration, Fundamental Beliefs tagging, and localization for Philippine SDA churches.

**Suggested Answer Guide**

> "Competitors solve general church management but fail at SDA-specific content and affordable pricing for Philippine congregations. My project focuses on SDA-tailored features and free access for Nueva Vizcaya churches."

---

## 1.5 Feature Definition & Scope Control

**Answers**

* **What are MUST-HAVE features?** User authentication with role-based access, church directory, events calendar with CRUD, blogs and announcements, lesson studies hub, file upload system, basic admin dashboard.
* **What are NICE-TO-HAVE features?** Advanced search, user notifications, member directory, enhanced analytics.
* **What features are explicitly excluded?** AI automation, mobile app, advanced analytics, enterprise features (Version 1 focus).

**Suggested Answer Guide**

> MUST: Authentication, church directory, events, blogs, lesson studies, file uploads
> NICE: Advanced search, notifications, member profiles
> OUT: AI, mobile app (Version 1)

---

## 1.6 Platform & Project Type

**Answers**

* **Is this a website by default?** Yes, Version 1 is a responsive web application with mobile-first design.
* **Will it expand to mobile, AI, or robotics?** Yes - mobile app in Version 4, AI automation in Version 3, no robotics planned.
* **Does it require real-time processing?** Not for Version 1; basic CRUD operations are sufficient.
* **Does it integrate with hardware?** No hardware integration required for Version 1.

**Suggested Answer Guide**

> "Version 1 is a web application; mobile is planned for Version 4."

---

## 1.7 User Requirements

**Answers**

* **What actions can users perform?** Register/login, view church directory, browse and RSVP to events, read blogs and announcements, access lesson studies, upload/download files, view member profiles.
* **What actions are restricted?** Administrative actions like user management, content editing, system configuration (restricted to pastors, elders, treasurers).
* **What errors must be user-friendly?** Login failures, form validation errors, file upload issues, network connectivity problems with clear guidance.
* **Accessibility needs?** WCAG 2.1 AA compliance, mobile-responsive design, keyboard navigation, screen reader support, Filipino/English language options.

**Suggested Answer Guide**

> Users can register, browse content, and participate in events; admins manage the platform. All errors provide clear feedback, and the platform is fully accessible with mobile support.

---

## 1.8 System Requirements

**Answers**

* **Expected number of users?** 1000 users initially, scalable to more in future versions.
* **Response time expectations?** Less than 500ms for most operations to ensure smooth user experience.
* **Availability requirements?** High availability (99.9%) to support church operations and community engagement.
* **Storage needs?** PostgreSQL database on basic EC2 instance for structured data (prototype), AWS S3 for file uploads and media storage. This approach eliminates RDS costs by self-hosting PostgreSQL on EC2 as a cost-optimization strategy.

**Suggested Answer Guide**

> "System should support 1k users with <500ms response time."

---

## 1.9 Software Evolution Roadmap

**Answers**

* **What is Version 1?** Core platform with authentication, church directory, events, blogs, lesson studies, file uploads, and basic admin features.
* **What improves in Version 2?** Enhanced UI/UX, advanced search, user notifications, member profiles, and improved analytics.
* **When does AI appear?** Version 3 introduces AI automation, content summaries, and smart notifications.
* **When does mobile appear?** Version 4 adds native mobile app with offline capabilities.

**Suggested Answer Guide**

* V1: Core functionality
* V2: UI/UX
* V3: AI / automation
* V4: Mobile app

## 1.10 Monetization Strategy

**Answers**

* **Does this web/app have premium features?** No premium features planned; this is a free service provided as a commitment to the Lord by Lester Dann Lopez.
* **Is it free?** Yes, the platform is completely free for SDA churches and community members, with no intention to monetize.
* **Does it run ads?** No ads; this project is maintained voluntarily without profit motive.

**Suggested Answer Guide**

> "This platform is provided free of charge by Lester Dann Lopez as a commitment to the Lord, with no monetization planned."

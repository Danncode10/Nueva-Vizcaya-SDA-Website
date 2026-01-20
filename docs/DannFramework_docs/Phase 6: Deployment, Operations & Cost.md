# **PHASE 6 — Deployment, Operations & Cost**

## 6.1 Deployment Strategy

**Answers**

* **Manual or Automated?** Hybrid approach - manual deployment for initial releases, automated CI/CD pipeline for future updates. GitHub Actions for automated testing and deployment to staging environment.
* **Environments:**
  - **Development:** Local development environment with Docker containers
  - **Staging:** AWS EC2 instance for integration testing and pilot user access
  - **Production:** AWS EC2 instance with load balancer for live application
* **Rollback Strategy:** Database backups before deployments, blue-green deployment pattern. Rollback to previous stable version by redeploying previous Docker image. Data migration rollback scripts for schema changes.

---

## 6.2 CI/CD Pipeline

**Answers**

* **Build Triggers:** Automatic builds on push to main branch, pull requests, and scheduled nightly builds. Manual builds for hotfixes.
* **Automated Tests:** Unit tests for API endpoints (pytest), integration tests for database operations, end-to-end tests for critical user workflows (Playwright), security scans.
* **Deployment Automation:** GitHub Actions pipeline that builds Docker images, runs tests, and deploys to staging. Manual approval required for production deployment.

**Implementation:**

> **GitHub Actions Pipeline:**
> 1. Code checkout and dependency installation
> 2. Run automated tests (unit, integration, e2e)
> 3. Security scanning and code quality checks
> 4. Build Docker images for frontend and backend
> 5. Deploy to staging environment
> 6. Run smoke tests on staging
> 7. Manual approval for production deployment
> 8. Deploy to production with zero-downtime strategy

---

## 6.3 Monitoring & Logging

**Answers**

* **Key Metrics:**
  - Application performance: Response times, error rates, throughput
  - Infrastructure: CPU usage, memory usage, disk space, network traffic
  - User experience: Page load times, user session duration
  - Business metrics: Active users, feature usage, conversion rates

* **Error Tracking:** AWS CloudWatch for application logs, structured logging with request IDs for tracing. Sentry for frontend error tracking and user feedback.

* **Alerting Rules:**
  - High error rate (>5% of requests)
  - Response time degradation (>2 seconds average)
  - Infrastructure alerts (CPU >80%, memory >85%, disk >90%)
  - Security alerts (failed login attempts, unusual traffic patterns)

**Implementation:**

> **AWS CloudWatch + Application Monitoring:**
> - CloudWatch Logs for centralized logging
> - CloudWatch Metrics for performance monitoring
> - CloudWatch Alarms for automated alerts
> - X-Ray for distributed tracing (future enhancement)
> - Custom dashboards for key metrics visualization

---

## 6.4 Cost Estimation (AWS)

**Answers**

* **Monthly Cost Breakdown (Estimated for 1000 users):**
  - **EC2 Instance (t3.medium):** $30-50/month (application + PostgreSQL database server)
  - **S3 Storage:** $1-5/month (file storage)
  - **CloudWatch:** $5-10/month (monitoring and logs)
  - **Route 53:** $1-2/month (DNS)
  - **Data Transfer:** $5-15/month (depending on usage)
  - **Total Estimated:** $42-82/month for basic setup (20-25% cost reduction vs RDS)

**Authentication Service:** AWS Cognito configured with Google OAuth as the identity provider. Users authenticate through Google, Cognito manages user pools and provides JWT access tokens. No passwords are stored in our database - Google handles the secure authentication, and we store only the Google user ID for user identification.

**Database Storage Note:** Using PostgreSQL on EC2 eliminates RDS costs. User authentication via Google OAuth means no passwords stored locally. Database contains user profiles, roles, and application data but no sensitive credentials. Database files are not committed to Git - only schema migrations and seed data.

* **Cost per User:** $0.06-0.11 per active user per month (based on 1000 users), decreasing as user base grows due to AWS economies of scale.

* **Budget Management:** AWS Budgets with alerts at 50%, 75%, and 90% of monthly budget. Cost allocation tags for tracking expenses by service and environment.

**Cost Optimization Strategies:**

> **AWS Cost Optimization:**
> - Use EC2 reserved instances for production (20-50% savings)
> - Implement auto-scaling to reduce costs during low-traffic periods
> - Use CloudFront CDN for static assets to reduce data transfer costs
> - Regular cost analysis and right-sizing of resources
> - Leverage AWS Free Tier for development and testing

---

## 6.5 Infrastructure Architecture

**Answers**

* **Cloud Provider:** AWS (Amazon Web Services) as primary cloud provider, following the AWS-first strategy.
* **Scalability Approach:** Start with single EC2 instance running both application and PostgreSQL database. Implement application auto-scaling for horizontal scaling. Database optimization through indexing and query optimization before considering read replicas.
* **Security Measures:** VPC with security groups, HTTPS encryption, AWS WAF for web application firewall, regular security updates, and compliance with data protection regulations.

---

## 6.6 Backup & Disaster Recovery

**Answers**

* **Backup Frequency:** Daily automated backups for database, weekly backups for application code, continuous replication for critical data.
* **Recovery Procedures:** Automated failover for infrastructure, documented runbooks for manual recovery, regular disaster recovery testing.
* **Data Retention:** 30 days for database backups, 90 days for application logs, indefinite retention for user-generated content as legally required.

---

## 6.7 Performance Optimization

**Answers**

* **Caching Strategy:** Redis for session storage and API response caching, browser caching for static assets, CloudFront for global content delivery.
* **Database Optimization:** Database indexing, query optimization, connection pooling, read replicas for high-traffic queries.
* **CDN Usage:** CloudFront for static assets (images, CSS, JS), API Gateway caching for API responses, global edge locations for improved performance.

---

## 6.8 Maintenance Schedule

**Answers**

* **Update Frequency:** Weekly security patches, monthly feature updates, quarterly major version releases.
* **Downtime Windows:** Scheduled maintenance during low-traffic hours (2-4 AM Philippine time), zero-downtime deployments for critical updates.
* **Emergency Procedures:** Incident response plan with escalation procedures, emergency rollback capabilities, and communication protocols for stakeholders.

---

## 6.9 Compliance & Security

**Answers**

* **Data Protection:** Encryption at rest and in transit, secure API authentication, regular security audits, and vulnerability assessments.
* **Privacy Compliance:** GDPR/CCPA compliance for user data handling, cookie consent management, data minimization practices.
* **Audit Requirements:** Regular security audits, access logging, change management documentation, and compliance reporting for church data protection.

---

## 6.10 Support & Documentation

**Answers**

* **User Support:** In-app help system, FAQ documentation, email support for church administrators, community forums for user discussions.
* **Technical Documentation:** API documentation, deployment guides, troubleshooting runbooks, and architecture diagrams.
* **Training Materials:** Video tutorials for administrators, user guides, and onboarding materials for new church users.

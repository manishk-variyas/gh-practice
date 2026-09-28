# Software Versioning and Release Management

## 1. Document Control

| Field                      | Details                   |
| -------------------------- | ------------------------- |
| Project / Application      | `<Project Name>`          |
| Repository                 | `<GitHub Repository URL>` |
| Document Owner             | `<Name / Role>`           |
| Versioning Standard        | Semantic Versioning       |
| Current Production Version | `<vX.Y.Z>`                |
| Last Release Date          | `<YYYY-MM-DD>`            |
| Release Owner              | `<Name / Team>`           |
| Document Last Updated      | `<YYYY-MM-DD>`            |

---

# 2. Purpose

This document defines the versioning, change tracking, release management, deployment, and rollback practices for the `<Project Name>` application.

The objective is to provide traceability from:

**Requirement / Defect → Issue → Branch → Commit → Pull Request → Version → Release → Deployment**

This document serves as the central record for application versions and production releases.

---

# 3. Versioning Standard

The project follows **Semantic Versioning** using:

`MAJOR.MINOR.PATCH`

Example:

`v2.4.3`

Where:

| Component | Purpose                               | Example           |
| --------- | ------------------------------------- | ----------------- |
| MAJOR     | Breaking or incompatible change       | `v1.0.0 → v2.0.0` |
| MINOR     | New backward-compatible functionality | `v1.2.0 → v1.3.0` |
| PATCH     | Backward-compatible bug fix           | `v1.3.0 → v1.3.1` |

---

# 4. Version Change Rules

## 4.1 Major Version

Increase the **MAJOR** version when the release introduces incompatible or breaking changes.

Examples:

* Breaking API changes
* Major architectural changes
* Removal of existing functionality
* Database changes incompatible with previous releases
* Authentication or authorization redesign affecting integrations
* Major UI/workflow changes requiring migration

Example:

`v1.8.4 → v2.0.0`

---

## 4.2 Minor Version

Increase the **MINOR** version when new functionality is introduced while maintaining backward compatibility.

Examples:

* New feature
* New API endpoint
* New application module
* New report
* New workflow
* Enhancement that introduces additional functionality

Example:

`v1.8.4 → v1.9.0`

---

## 4.3 Patch Version

Increase the **PATCH** version when backward-compatible corrections or minor improvements are introduced.

Examples:

* Bug fixes
* Security patches
* Minor UI corrections
* Performance optimization
* Small configuration correction
* Documentation correction affecting deployment

Example:

`v1.8.4 → v1.8.5`

---

# 5. Branching Convention

The following branch naming convention shall be used.

| Change Type         | Branch Format                   | Example                       |
| ------------------- | ------------------------------- | ----------------------------- |
| New Feature         | `feature/<issue>-<description>` | `feature/231-lead-assignment` |
| Bug Fix             | `fix/<issue>-<description>`     | `fix/245-login-timeout`       |
| Enhancement         | `enhance/<issue>-<description>` | `enhance/267-customer-search` |
| Production Hotfix   | `hotfix/<issue>-<description>`  | `hotfix/301-payment-timeout`  |
| Refactoring         | `refactor/<description>`        | `refactor/auth-service`       |
| Documentation       | `docs/<description>`            | `docs/api-guide`              |
| Release Preparation | `release/<version>`             | `release/v1.6.0`              |

The `main` branch represents the stable and releasable application baseline.

Direct development on `main` should be avoided.

---

# 6. Commit Convention

The project follows structured commit messages.

Recommended format:

`<type>(<scope>): <description>`

Examples:

`feat(customer): add customer import functionality`

`fix(auth): correct token expiration handling`

`perf(search): optimize customer lookup`

`refactor(invoice): separate tax calculation service`

`docs(api): update customer API documentation`

`test(leads): add lead assignment tests`

Recommended commit types:

| Type       | Purpose                       |
| ---------- | ----------------------------- |
| `feat`     | New functionality             |
| `fix`      | Bug correction                |
| `perf`     | Performance improvement       |
| `refactor` | Internal code restructuring   |
| `test`     | Test addition or modification |
| `docs`     | Documentation                 |
| `style`    | Formatting / UI styling       |
| `build`    | Build system changes          |
| `ci`       | CI/CD changes                 |
| `chore`    | Maintenance activity          |

---

# 7. Release Lifecycle

The standard release lifecycle is:

```text
Requirement / Bug / Enhancement
            │
            ▼
       GitHub Issue
            │
            ▼
       Create Branch
            │
            ▼
        Development
            │
            ▼
         Commits
            │
            ▼
      Pull Request
            │
      ┌─────┴─────┐
      ▼           ▼
 Code Review   CI Checks
      │           │
      └─────┬─────┘
            ▼
           Merge
            │
            ▼
       Version Bump
            │
            ▼
          Git Tag
            │
            ▼
      GitHub Release
            │
            ▼
        Deployment
            │
            ▼
       Verification
```

---

# 8. Release Register

The following table shall contain all officially released versions.

| Version  | Release Date | Release Type | Git Tag  | Environment | Status   | Release Owner |
| -------- | ------------ | ------------ | -------- | ----------- | -------- | ------------- |
| `v1.0.0` | `<date>`     | Initial      | `v1.0.0` | Production  | Released | `<name>`      |
| `v1.1.0` | `<date>`     | Minor        | `v1.1.0` | Production  | Released | `<name>`      |
| `v1.1.1` | `<date>`     | Patch        | `v1.1.1` | Production  | Released | `<name>`      |

Recommended status values:

* Planned
* In Development
* Release Candidate
* Approved
* Deployed
* Released
* Rolled Back
* Deprecated

---

# 9. Release Record

A separate record should be maintained for each release.

---

## Release `<vX.Y.Z>`

### 9.1 Release Information

| Field              | Details                                         |
| ------------------ | ----------------------------------------------- |
| Version            | `<vX.Y.Z>`                                      |
| Release Name       | `<Release Name>`                                |
| Release Date       | `<YYYY-MM-DD>`                                  |
| Release Type       | `<Major / Minor / Patch / Hotfix>`              |
| Git Tag            | `<vX.Y.Z>`                                      |
| Git Commit SHA     | `<commit SHA>`                                  |
| Release Branch     | `<release/vX.Y.Z if applicable>`                |
| Target Environment | `<Development / Test / UAT / Production>`       |
| Release Owner      | `<Name>`                                        |
| Deployment Owner   | `<Name / Team>`                                 |
| Release Status     | `<Planned / Approved / Deployed / Rolled Back>` |

---

### 9.2 Release Objective

Describe the primary purpose of the release.

Example:

`This release introduces lead reassignment functionality, improves customer search performance, and resolves the authentication token timeout defect.`

---

# 10. Changes Included

## 10.1 New Features

| Issue  | Feature         | Branch                        | Pull Request | Description                     |
| ------ | --------------- | ----------------------------- | ------------ | ------------------------------- |
| `#231` | Lead Assignment | `feature/231-lead-assignment` | `#245`       | Allows managers to assign leads |
| `<ID>` | `<Feature>`     | `<Branch>`                    | `<PR>`       | `<Description>`                 |

---

## 10.2 Enhancements

| Issue  | Enhancement     | Branch                        | Pull Request | Description                   |
| ------ | --------------- | ----------------------------- | ------------ | ----------------------------- |
| `#267` | Customer Search | `enhance/267-customer-search` | `#271`       | Improved filtering and lookup |
| `<ID>` | `<Enhancement>` | `<Branch>`                    | `<PR>`       | `<Description>`               |

---

## 10.3 Bug Fixes

| Issue  | Defect        | Branch                  | Pull Request | Resolution                      |
| ------ | ------------- | ----------------------- | ------------ | ------------------------------- |
| `#245` | Login Timeout | `fix/245-login-timeout` | `#250`       | Corrected token expiry handling |
| `<ID>` | `<Defect>`    | `<Branch>`              | `<PR>`       | `<Resolution>`                  |

---

## 10.4 Security Fixes

| Reference       | Issue           | Severity                           | Resolution     |
| --------------- | --------------- | ---------------------------------- | -------------- |
| `<CVE / Issue>` | `<Description>` | `<Critical / High / Medium / Low>` | `<Resolution>` |

If there are no security changes:

`No security-related changes are included in this release.`

---

# 11. Pull Requests Included

| PR     | Description           | Issue  | Reviewer | Status |
| ------ | --------------------- | ------ | -------- | ------ |
| `#245` | Add lead assignment   | `#231` | `<name>` | Merged |
| `#250` | Correct token timeout | `#245` | `<name>` | Merged |

---

# 12. Build Information

| Field            | Details                         |
| ---------------- | ------------------------------- |
| Build Number     | `<Build ID>`                    |
| CI Workflow      | `<GitHub Actions Workflow>`     |
| Build Date       | `<YYYY-MM-DD HH:MM>`            |
| Build Status     | `<Pass / Fail>`                 |
| Artifact Version | `<version>`                     |
| Container Image  | `<repository:tag>`              |
| Container Digest | `<SHA256 digest if applicable>` |

Example:

`ghcr.io/company/crm:v1.6.0`

---

# 13. Release Validation

The following validation checks must be completed before release approval.

| Check                        | Result            | Evidence         |
| ---------------------------- | ----------------- | ---------------- |
| Code review completed        | Pass / Fail       | `<PR>`           |
| Unit tests passed            | Pass / Fail       | `<URL / Job ID>` |
| Integration tests passed     | Pass / Fail       | `<Reference>`    |
| Application build passed     | Pass / Fail       | `<Reference>`    |
| Security scan passed         | Pass / Fail       | `<Reference>`    |
| Dependency scan completed    | Pass / Fail       | `<Reference>`    |
| Database migration tested    | Pass / Fail / N/A | `<Reference>`    |
| UAT completed                | Pass / Fail / N/A | `<Reference>`    |
| Release notes reviewed       | Pass / Fail       | `<Reference>`    |
| Rollback procedure validated | Pass / Fail       | `<Reference>`    |

---

# 14. Testing Summary

## Unit Testing

Number of tests executed:

`<number>`

Results:

`<Passed / Failed / Skipped>`

---

## Integration Testing

Summary:

`<Details>`

---

## UAT

UAT Status:

`<Approved / Pending / Not Required>`

Approved By:

`<Name / Role>`

Date:

`<YYYY-MM-DD>`

---

# 15. Database Changes

Database change included:

`<Yes / No>`

If yes:

| Item                | Details                      |
| ------------------- | ---------------------------- |
| Migration ID        | `<ID>`                       |
| Migration Tool      | `<Alembic / Flyway / Other>` |
| Schema Change       | `<Description>`              |
| Backward Compatible | `<Yes / No>`                 |
| Rollback Supported  | `<Yes / No>`                 |

Migration command:

`<command or procedure reference>`

---

# 16. Configuration Changes

Document configuration changes introduced by the release.

| Configuration | Previous  | New       | Environment     |
| ------------- | --------- | --------- | --------------- |
| `<setting>`   | `<value>` | `<value>` | `<environment>` |

Do not document passwords, API keys, tokens, certificates, or other secrets in this document.

---

# 17. Dependency Changes

| Dependency  | Previous Version | New Version | Reason     |
| ----------- | ---------------- | ----------- | ---------- |
| `<package>` | `<version>`      | `<version>` | `<reason>` |

---

# 18. API Changes

API changes:

`<Yes / No>`

If applicable:

| Endpoint            | Change          | Compatibility             |
| ------------------- | --------------- | ------------------------- |
| `/api/v1/customers` | Added filtering | Backward compatible       |
| `<endpoint>`        | `<change>`      | `<compatible / breaking>` |

Breaking API changes require a **MAJOR** version increase unless governed by a separate API-versioning policy.

---

# 19. Deployment Plan

## Pre-Deployment

* Confirm release approval.
* Confirm production backup.
* Confirm database backup where applicable.
* Validate application artifacts.
* Verify secrets and configuration.
* Verify infrastructure capacity.
* Confirm rollback version.
* Notify relevant stakeholders.

## Deployment

Deployment procedure:

`<Reference deployment runbook or procedure>`

Deployment date/time:

`<YYYY-MM-DD HH:MM>`

Deployment executed by:

`<Name / Team>`

---

# 20. Post-Deployment Validation

| Validation                  | Status      |
| --------------------------- | ----------- |
| Application health endpoint | Pass / Fail |
| Authentication              | Pass / Fail |
| Database connectivity       | Pass / Fail |
| Critical API endpoints      | Pass / Fail |
| Critical user workflow      | Pass / Fail |
| Monitoring healthy          | Pass / Fail |
| Application logs reviewed   | Pass / Fail |
| Error rate normal           | Pass / Fail |

---

# 21. Rollback Plan

Previous stable version:

`<vX.Y.Z>`

Rollback tag:

`<Git tag>`

Rollback artifact:

`<Container Image / Package>`

Rollback conditions:

* Application unavailable after deployment
* Critical functionality failure
* Data integrity issue
* Authentication failure
* Severe performance degradation
* Critical security issue
* Database migration failure

Rollback procedure:

`<Reference rollback runbook>`

---

# 22. Rollback Record

Complete this section only if rollback occurs.

| Field              | Details     |
| ------------------ | ----------- |
| Failed Version     | `<version>` |
| Rollback Version   | `<version>` |
| Rollback Date      | `<date>`    |
| Reason             | `<reason>`  |
| Incident Reference | `<ticket>`  |
| Root Cause         | `<summary>` |
| Corrective Action  | `<details>` |

---

# 23. Known Issues

| Issue     | Severity     | Workaround     | Planned Fix |
| --------- | ------------ | -------------- | ----------- |
| `<issue>` | `<severity>` | `<workaround>` | `<version>` |

If no known issues:

`No known issues at the time of release.`

---

# 24. Release Risks

| Risk     | Impact     | Mitigation     |
| -------- | ---------- | -------------- |
| `<risk>` | `<impact>` | `<mitigation>` |

---

# 25. Compatibility

| Component        | Supported Version |
| ---------------- | ----------------- |
| Frontend         | `<version>`       |
| Backend          | `<version>`       |
| Database         | `<version>`       |
| Keycloak         | `<version>`       |
| Node.js          | `<version>`       |
| Python           | `<version>`       |
| Browser          | `<versions>`      |
| Operating System | `<versions>`      |

---

# 26. Release Approval

| Role               | Name     | Decision | Date     |
| ------------------ | -------- | -------- | -------- |
| Developer          | `<name>` | Approved | `<date>` |
| Technical Reviewer | `<name>` | Approved | `<date>` |
| QA                 | `<name>` | Approved | `<date>` |
| Product Owner      | `<name>` | Approved | `<date>` |
| Release Manager    | `<name>` | Approved | `<date>` |

Adjust approval roles according to project size and governance requirements.

---

# 27. Release Notes

## `<vX.Y.Z>` — `<Release Name>`

Release Date: `<YYYY-MM-DD>`

### Added

* `<New feature>`
* `<New feature>`

### Changed

* `<Enhancement>`
* `<Improvement>`

### Fixed

* `<Bug fix>`
* `<Bug fix>`

### Security

* `<Security correction>`

### Deprecated

* `<Deprecated feature>`

### Removed

* `<Removed functionality>`

### Known Issues

* `<Known issue>`

---

# 28. Traceability Matrix

This matrix provides end-to-end traceability for each change.

| Requirement / Issue | Branch                        | Commit  | Pull Request | Test     | Release  |
| ------------------- | ----------------------------- | ------- | ------------ | -------- | -------- |
| `#231`              | `feature/231-lead-assignment` | `<SHA>` | `#245`       | `<test>` | `v1.6.0` |
| `#245`              | `fix/245-login-timeout`       | `<SHA>` | `#250`       | `<test>` | `v1.6.0` |

The target traceability model is:

`Requirement → Issue → Branch → Commit → PR → Test → Version → Deployment`

---

# 29. Version History

| Version  | Release Date | Summary                    | Status     |
| -------- | ------------ | -------------------------- | ---------- |
| `v1.0.0` | `<date>`     | Initial production release | Active     |
| `v1.1.0` | `<date>`     | Added customer management  | Superseded |
| `v1.1.1` | `<date>`     | Authentication bug fix     | Superseded |
| `v1.2.0` | `<date>`     | Added lead management      | Current    |

---

# 30. Release Support Status

| Version | Status      | Support Until |
| ------- | ----------- | ------------- |
| `v2.x`  | Current     | `<date>`      |
| `v1.x`  | Maintenance | `<date>`      |
| `v0.x`  | Unsupported | `<date>`      |

Recommended lifecycle terminology:

* Current
* Maintenance
* Deprecated
* End of Support
* End of Life

---

# 31. Repository Release Checklist

Before creating a production release confirm:

* [ ] All required issues are complete.
* [ ] All required pull requests are merged.
* [ ] CI checks have passed.
* [ ] Tests have passed.
* [ ] Security scans have passed.
* [ ] Database migrations have been tested.
* [ ] Version number has been updated.
* [ ] Release notes have been prepared.
* [ ] Git tag has been created.
* [ ] GitHub Release has been created.
* [ ] Deployment artifact is immutable.
* [ ] Previous production version is available for rollback.
* [ ] Deployment approval has been obtained.
* [ ] Production deployment completed successfully.
* [ ] Post-deployment validation completed.
* [ ] Monitoring and logs reviewed.
* [ ] Release register updated.

---

# 32. Recommended Repository Documentation Structure

```text
repository/
│
├── README.md
├── CHANGELOG.md
├── VERSION
│
├── docs/
│   ├── VERSIONING_AND_RELEASE_MANAGEMENT.md
│   ├── DEPLOYMENT.md
│   ├── ROLLBACK.md
│   ├── ARCHITECTURE.md
│   └── SECURITY.md
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   │
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
└── source-code/
```

Recommended responsibility:

`VERSION`

Contains only the current application version.

Example:

`1.6.0`

`CHANGELOG.md`

Contains a chronological history of changes.

`VERSIONING_AND_RELEASE_MANAGEMENT.md`

Defines the versioning policy and maintains release governance.

GitHub Releases

Represent formally published application releases.

Git Tags

Identify the exact source-code revision corresponding to a release.

---

# 33. Change History for This Document

| Document Version | Date     | Change           | Author   |
| ---------------- | -------- | ---------------- | -------- |
| `1.0`            | `<date>` | Initial document | `<name>` |
| `<version>`      | `<date>` | `<change>`       | `<name>` |

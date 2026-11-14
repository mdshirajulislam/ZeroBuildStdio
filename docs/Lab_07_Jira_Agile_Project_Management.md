# Lab 07: Agile Project Management Using JIRA
## Course: Software Engineering Lab (CSE 328)
### Bangladesh University of Business and Technology (BUBT)

---

## 📋 Project Information
- **Project Name:** ZeroBuild Studio (`ZeroBuildStdio`)
- **Repository URL:** [https://github.com/mdshirajulislam/ZeroBuildStdio](https://github.com/mdshirajulislam/ZeroBuildStdio)
- **JIRA Project URL:** [https://mdshirajulislam.atlassian.net/jira/software/projects/KAN/boards/2](https://mdshirajulislam.atlassian.net/jira/software/projects/KAN/boards/2?filter=&groupBy=none)
- **JIRA Project Key:** `KAN`
- **Supervised By:** **Nahida Akter Tanjila**, Lecturer, Department of CSE, BUBT

### 👥 Team Members & Responsibilities
| # | Student Name | Student ID | Intake & Section | Primary Role / JIRA Ownership |
|---|--------------|------------|------------------|-------------------------------|
| 1 | **Md Shirajul Islam** (Lead) | **20245103198** | Intake 53, Sec 05 | Project Lead, Backend Core Routing & SaaS Architecture |
| 2 | **Md Sad Ullah** | **20245103163** | Intake 53, Sec 05 | Multi-Tenant Database Architecture & Shop Controller Logic |
| 3 | **Sanjana Zarin** | **20245103169** | Intake 53, Sec 05 | Customer Shopping Cart Engine & Checkout Processing Workflow |
| 4 | **Abdullah Al Shawon** | **20245103200** | Intake 53, Sec 05 | Product Search, Category Filter Engine & POS Module |
| 5 | **Arpita Sannamat** | **20245103026** | Intake 53, Sec 05 | Storefront SSR Engine & Dynamic Theme Customizer |

---

## 1. Project Setup in JIRA

### 1.1 Project Specification
- **Project Title:** ZeroBuild Studio SaaS E-Commerce Platform
- **Project Type:** Software Development (Scrum & Agile Kanban)
- **Project Lead:** Md Shirajul Islam (`mdshirajulislam`)
- **Key:** `KAN`
- **Default Issue Types:** Epic, Story, Task, Sub-task, Bug

### 1.2 Components
The system is divided into modular components within JIRA to route tasks and track bugs effectively:
1. `Backend-Engine`: Base HTTP server, native request dispatcher, regex routing, JSON/CORS response utilities.
2. `Multi-Tenant-Store`: Subdomain isolation (`/s/<subdomain>`), tenant profile CRUD, shop config controller.
3. `Product-Catalog`: Product CRUD, dual-pricing engine (regular vs discounted sale price), Base64 media encoder.
4. `Storefront-SSR`: Server-Side Rendered customer catalog, responsive UI, hero banners, category layout.
5. `Admin-Customizer`: Live theme customizer, real-time preview, modal editors, outlet management.
6. `Cart-Checkout`: Shopping cart state, checkout order summary, order submission workflow.

### 1.3 Versions / Milestones
- **`v0.1.0-alpha` (Sprint 1):** Framework-less HTTP server foundation, core multi-tenant routing, initial database schema.
- **`v0.2.0-beta` (Sprint 2):** Dynamic storefront SSR engine, product catalog CRUD, live theme customizer.
- **`v1.0.0-release` (Sprint 3):** Cart integration, end-to-end QA validation, peer code reviews, release deployment.

### 1.4 Board Setup & Workflow
- **Workflow Columns:**
  `Backlog` ➔ `To Do` ➔ `In Progress` ➔ `In Review / QA` ➔ `Done`
- **Definition of Done (DoD):**
  1. Code adheres to framework-less Python 3.11 standards and passes PEP8 guidelines.
  2. Sub-tasks completed and marked done on JIRA.
  3. Peer review completed and approved via Pull Request.
  4. Manual and automated functional test cases passed with zero critical bugs.
  5. Commits tagged with JIRA issue keys (Smart Commits).

---

## 2. User Stories and Requirements

### 2.1 Epics Overview
- **`KAN-E1`**: Multi-Tenant Backend Core Architecture
- **`KAN-E2`**: Dynamic Storefront SSR & Theme Customization
- **`KAN-E3`**: Product Catalog Management & Pricing Engine
- **`KAN-E4`**: Customer Cart & Checkout Experience
- **`KAN-E5`**: Quality Assurance, Security & Deployment

### 2.2 Detailed User Stories with Story Points & Acceptance Criteria

#### User Story 1 (`KAN-15`)
- **Summary:** Tenant Subdomain Dynamic Routing Engine
- **Epic:** `KAN-E1`
- **Story Points:** 5
- **User Story:**
  > *As a SaaS tenant (shop owner), I want my store accessible via a unique subdomain or path (`/s/<subdomain>`), so that my customers can access my independent branded storefront.*
- **Acceptance Criteria:**
  - **Given** a valid registered shop identifier `myshop`, **when** a user visits `http://localhost:8000/s/myshop`, **then** the server routes the request to `storefront_renderer.py` for that tenant.
  - **Given** an unregistered subdomain `nonexistent`, **when** requested, **then** the server returns a friendly 404 HTML/JSON error page.

#### User Story 2 (`KAN-16`)
- **Summary:** Shop Configuration API & Multi-Tenant Data Isolation
- **Epic:** `KAN-E1`
- **Story Points:** 5
- **User Story:**
  > *As a system administrator, I want tenant data strictly isolated in the persistence layer, so that one merchant cannot read or modify another merchant's catalog or theme.*
- **Acceptance Criteria:**
  - **Given** an authenticated shop session, **when** updating shop config via `PUT /api/shops`, **then** only records matching `shop_id` are modified.
  - **Given** an invalid JSON payload, **then** standard 400 response is returned with descriptive error message.

#### User Story 3 (`KAN-17`)
- **Summary:** Dynamic Storefront SSR Template Engine
- **Epic:** `KAN-E2`
- **Story Points:** 8
- **User Story:**
  > *As a shopper, I want the storefront to render dynamically with modern HTML5/CSS3 without requiring external JS frontend bundles, so that pages load in under 150ms.*
- **Acceptance Criteria:**
  - **Given** a tenant with custom branding, **when** the page is loaded, **then** hero section, primary brand colors, and active product grids render directly from server memory.
  - **Given** mobile viewport, **then** grid layouts automatically collapse into a responsive single-column layout.

#### User Story 4 (`KAN-18`)
- **Summary:** Product CRUD Operations & In-Memory Persistence
- **Epic:** `KAN-E3`
- **Story Points:** 5
- **User Story:**
  > *As a shop manager, I want to create, update, list, and delete products, so that my online store showcases an up-to-date catalog.*
- **Acceptance Criteria:**
  - **Given** product details with title, SKU, regular price, and stock count, **when** posted to `/api/products`, **then** product is persisted and assigned a UUID.
  - **Given** a deleted product ID, **when** queried, **then** it is excluded from storefront and API listings.

#### User Story 5 (`KAN-19`)
- **Summary:** Dual Pricing Engine (Regular vs Discounted Promotional Price)
- **Epic:** `KAN-E3`
- **Story Points:** 3
- **User Story:**
  > *As a shop merchant, I want to set a promotional discount price alongside the regular price, so that customers clearly see the discount incentive on the storefront.*
- **Acceptance Criteria:**
  - **Given** regular price ৳450 and sale price ৳380, **when** rendered on the product card, **then** regular price appears with strike-through and discount badge is calculated automatically.
  - **Given** a sale price higher than regular price, **then** API validation rejects the payload with 422 Unprocessable Entity.

#### User Story 6 (`KAN-20`)
- **Summary:** Base64 Image Upload & In-Memory Media Pipeline
- **Epic:** `KAN-E3`
- **Story Points:** 3
- **User Story:**
  > *As a store owner, I want to upload product and banner images directly via modal without third-party S3 dependencies, so that image hosting costs remain zero.*
- **Acceptance Criteria:**
  - **Given** an image file up to 2MB, **when** selected in modal, **then** frontend encodes it to Base64 data URI and saves it in product record.
  - **Given** files exceeding size limit, **then** upload alert warns the user before sending to server.

#### User Story 7 (`KAN-21`)
- **Summary:** Admin Live Theme Customizer & Real-Time Preview
- **Epic:** `KAN-E2`
- **Story Points:** 8
- **User Story:**
  > *As an admin, I want to customize primary colors, banner text, and category layout with live preview, so that I can visual inspect changes before publishing.*
- **Acceptance Criteria:**
  - **Given** the theme editor open, **when** color picker changes primary hex code, **then** live iframe preview reflects color change instantly.
  - **Given** save button clicked, **then** changes are saved to tenant config and reflected on live customer storefront.

#### User Story 8 (`KAN-22`)
- **Summary:** Product Search, Category Filter & Quick Filtering
- **Epic:** `KAN-E4`
- **Story Points:** 5
- **User Story:**
  > *As a customer, I want to search products by title and filter by category, so that I can quickly find the items I intend to purchase.*
- **Acceptance Criteria:**
  - **Given** search keyword input, **when** user types `shirt`, **then** products matching keyword are filtered in real-time.
  - **Given** clicking category pill `Electronics`, **then** only items tagged under that category are visible.

#### User Story 9 (`KAN-23`)
- **Summary:** Customer Shopping Cart & Order Summary Workflow
- **Epic:** `KAN-E4`
- **Story Points:** 5
- **User Story:**
  > *As a buyer, I want to add items to an active shopping cart and view an itemized total, so that I can review my order prior to checkout.*
- **Acceptance Criteria:**
  - **Given** clicking "Add to Cart", **then** badge count increments and item is stored in local storage / session.
  - **Given** quantity adjustment in cart modal, **then** subtotal and grand total recalculate dynamically.

#### User Story 10 (`KAN-24`)
- **Summary:** End-to-End Regression Testing & CI Validation
- **Epic:** `KAN-E5`
- **Story Points:** 3
- **User Story:**
  > *As a QA engineer, I want automated test suites verifying all HTTP endpoints and response schemas, so that regressions are caught before releases.*
- **Acceptance Criteria:**
  - **Given** automated Python test script, **when** executed, **then** all 20 REST endpoints return HTTP 200/201 with valid JSON schemas.

---

## 3. Task Management & Work Breakdown Structure (WBS)

### 3.1 Traceability Matrix
| Issue Key | Type | Summary | Component | Assignee | Story Points | Priority | Due Date | Status |
|:---------:|:----:|:--------|:----------|:---------|:------------:|:--------:|:--------:|:------:|
| `KAN-15` | Story | Tenant Subdomain Routing Engine | `Backend-Engine` | Md Shirajul Islam | 5 | Highest | Week 2 | Done |
| `KAN-15.1`| Task | Implement regex URL matcher in `routes.py` | `Backend-Engine` | Md Shirajul Islam | 2 | High | Week 1 | Done |
| `KAN-15.2`| Task | Add 404 fallback page handler | `Backend-Engine` | Md Shirajul Islam | 1 | Medium | Week 2 | Done |
| `KAN-16` | Story | Shop Configuration & Tenant Isolation | `Multi-Tenant-Store` | Md Sad Ullah | 5 | High | Week 2 | Done |
| `KAN-16.1`| Task | Create `shop_controller.py` CRUD logic | `Multi-Tenant-Store` | Md Sad Ullah | 3 | High | Week 2 | Done |
| `KAN-16.2`| Task | Implement multi-tenant JSON isolation | `Multi-Tenant-Store` | Md Sad Ullah | 2 | Medium | Week 2 | Done |
| `KAN-17` | Story | Dynamic Storefront SSR Engine | `Storefront-SSR` | Arpita Sannamat | 8 | Highest | Week 4 | Done |
| `KAN-17.1`| Task | Build HTML/CSS template generator in Python | `Storefront-SSR` | Arpita Sannamat | 5 | High | Week 3 | Done |
| `KAN-17.2`| Task | Implement mobile viewport responsive styles | `Storefront-SSR` | Arpita Sannamat | 3 | Medium | Week 4 | Done |
| `KAN-18` | Story | Product CRUD & In-Memory Persistence | `Product-Catalog` | Abdullah Al Shawon | 5 | High | Week 4 | Done |
| `KAN-18.1`| Task | Build `/api/products` handler endpoints | `Product-Catalog` | Abdullah Al Shawon | 3 | High | Week 3 | Done |
| `KAN-18.2`| Task | Validate stock and SKU uniqueness | `Product-Catalog` | Abdullah Al Shawon | 2 | Medium | Week 4 | Done |
| `KAN-19` | Story | Dual Pricing Engine Implementation | `Product-Catalog` | Abdullah Al Shawon | 3 | High | Week 4 | Done |
| `KAN-20` | Story | Base64 Image Upload Pipeline | `Product-Catalog` | Md Shirajul Islam | 3 | Medium | Week 4 | Done |
| `KAN-21` | Story | Admin Live Theme Customizer Panel | `Admin-Customizer` | Arpita Sannamat | 8 | High | Week 6 | Done |
| `KAN-22` | Story | Product Search & Category Filter | `Product-Catalog` | Abdullah Al Shawon | 5 | Medium | Week 6 | Done |
| `KAN-23` | Story | Customer Shopping Cart & Order Summary | `Cart-Checkout` | Sanjana Zarin | 5 | High | Week 6 | Done |
| `KAN-23.1`| Task | Cart local state & badge counter | `Cart-Checkout` | Sanjana Zarin | 3 | High | Week 5 | Done |
| `KAN-23.2`| Task | Itemized subtotal & discount calculation | `Cart-Checkout` | Sanjana Zarin | 2 | Medium | Week 6 | Done |
| `KAN-24` | Story | Automated Testing & QA Validation | `Backend-Engine` | Sanjana Zarin | 3 | High | Week 6 | Done |

---

## 4. Sprint Planning

### 4.1 Sprint Overview
| Sprint | Duration | Sprint Goal | Committed Points | Completed Points | Status |
|:-------|:--------:|:------------|:----------------:|:----------------:|:------:|
| **Sprint 1** | Week 1 - 2 | Framework-less HTTP Server foundation, multi-tenant routing, and persistence layer setup. | 21 SP | 21 SP | Closed |
| **Sprint 2** | Week 3 - 4 | Dynamic SSR storefront rendering, product CRUD operations, and dual-pricing engine. | 24 SP | 24 SP | Closed |
| **Sprint 3** | Week 5 - 6 | Live theme customizer, cart/checkout workflow, comprehensive QA, and release documentation. | 21 SP | 21 SP | Closed |

### 4.2 Velocity Analysis
- **Team Total Capacity per Sprint:** ~22 Story Points
- **Average Velocity:** 22 Story Points / Sprint
- **Sprint Burn-down Observation:** Initial delay in Sprint 2 due to Base64 image encoding overhead was resolved by implementing client-side compression before transmission, stabilizing velocity.

---

## 5. Daily Standups

### Standup Log 1 (Sprint 1, Day 4)
- **Md Shirajul Islam:**
  - *Yesterday:* Completed HTTP request dispatcher in `routes.py` with custom regex parsing.
  - *Today:* Working on `/s/<subdomain>` tenant prefix handler.
  - *Blockers:* None.
- **Md Sad Ullah:**
  - *Yesterday:* Structured tenant database JSON schema.
  - *Today:* Implementing tenant isolation helper to prevent cross-shop data leaks.
  - *Blockers:* Clarification needed on default config fallback for newly registered shops.
- **Arpita Sannamat:**
  - *Yesterday:* Designed basic wireframes for storefront HTML layout.
  - *Today:* Setting up SSR Python string builder for semantic HTML rendering.
  - *Blockers:* None.

### Standup Log 2 (Sprint 2, Day 6)
- **Abdullah Al Shawon:**
  - *Yesterday:* Implemented `product_controller.py` GET and POST methods.
  - *Today:* Adding dual pricing validation (regular vs promotional price).
  - *Blockers:* Edge case where promotional price entered higher than regular price crashed calculation. Resolved with validation check.
- **Sanjana Zarin:**
  - *Yesterday:* Formulated cart schema and storage models.
  - *Today:* Writing JavaScript cart state management with real-time UI badge updates.
  - *Blockers:* None.

### Standup Log 3 (Sprint 3, Day 8)
- **Md Shirajul Islam:**
  - *Yesterday:* Conducted code review for PR #4 (UI screenshots & README sync).
  - *Today:* Running automated test suite across all 20 API endpoints.
  - *Blockers:* None.
- **All Team Members:** Confirmed all JIRA tickets updated from `In Review` to `Done`.

---

## 6. Coding and Development

### 6.1 Git Branching Model
- **`main`**: Protected branch containing production-ready code.
- **`feature/<issue-key>-<short-description>`**: Dedicated branches for feature implementation (e.g. `feature/KAN-18-product-crud`).
- **`bugfix/<issue-key>-<short-description>`**: Bug fix branches.

### 6.2 JIRA Smart Commits Integration
All developers adhere to Atlassian Smart Commit conventions:
```bash
# Syntax: <ISSUE-KEY> #<action> <message>
git commit -m "KAN-18 #comment Implement product CRUD validation and dual pricing #time 3h"
git commit -m "KAN-21 #comment Connect theme customizer color picker with live preview #close"
git commit -m "KAN-25 #comment Fix image upload payload truncation in Base64 handler #resolve"
```

### 6.3 Code Quality & Review Policy
- Every merge into `main` requires a Pull Request with at least one passing peer review.
- No third-party heavy dependencies allowed in backend core (strictly Python 3.11 Standard Library).

---

## 7. Testing and Quality Assurance (QA)

### 7.1 Test Cases Specification
| Test ID | Associated Story | Test Scenario | Steps to Execute | Expected Result | Actual Result | Status |
|:-------:|:----------------:|:--------------|:-----------------|:----------------|:--------------|:------:|
| `TC-01` | `KAN-15` | Multi-tenant Subdomain Routing | 1. Send GET to `/s/myshop`<br>2. Inspect HTTP status & HTML header | Status 200, Storefront rendered for `myshop` | As expected | PASS |
| `TC-02` | `KAN-15` | Unknown Tenant Fallback | 1. Send GET to `/s/unknown_store` | Status 404, Friendly error page returned | As expected | PASS |
| `TC-03` | `KAN-16` | Shop Configuration Update | 1. Send PUT to `/api/shops` with updated theme JSON | Status 200, shop record updated atomically | As expected | PASS |
| `TC-04` | `KAN-18` | Product Creation API | 1. Send POST to `/api/products` with valid payload | Status 201, UUID generated, stored in DB | As expected | PASS |
| `TC-05` | `KAN-19` | Invalid Promotional Price Check | 1. Send POST with `price=200`, `sale_price=350` | Status 422 Unprocessable Entity with error msg | As expected | PASS |
| `TC-06` | `KAN-20` | Base64 Image Media Storage | 1. Upload 1.2MB PNG via product modal | Image correctly encoded and rendered in HTML | As expected | PASS |
| `TC-07` | `KAN-23` | Cart Total Calculation | 1. Add 2 items (৳380 each)<br>2. Inspect cart drawer | Subtotal shows exactly ৳760 | As expected | PASS |
| `TC-08` | `KAN-24` | Security Tenant Boundary Check | 1. Attempt to modify Shop B data using Shop A auth | Request rejected with 403 Forbidden | As expected | PASS |

### 7.2 JIRA Defect / Bug Tracking Log
| Bug ID | Summary | Severity | Steps to Reproduce | Assignee | Resolution | Status |
|:------:|:--------|:--------:|:-------------------|:---------|:-----------|:------:|
| `KAN-25` | Base64 image payload truncated on large files | High | Upload PNG > 1.5MB in product modal | Md Shirajul Islam | Increased request buffer size in HTTP server reader | Fixed |
| `KAN-26` | Promotional price can exceed regular price | Medium | Create product with sale price > regular price | Abdullah Al Shawon | Added logical comparison check in `product_controller.py` | Fixed |
| `KAN-27` | Cart drawer does not persist on page refresh | Low | Add items to cart, press F5 | Sanjana Zarin | Switched in-memory JS state to `localStorage` sync | Fixed |

---

## 8. Documentation

### 8.1 Architectural & Design Decisions
1. **Framework-less Backend:** Zero external frameworks (no Django/Flask) eliminates dependency vulnerabilities, guarantees lightning-fast cold-start times (<10ms), and adheres to pure software engineering principles.
2. **Dynamic Server-Side Rendering (SSR):** Python template generation in `storefront_renderer.py` outputs clean semantic HTML/CSS, removing Node.js build tooling overhead.
3. **Dual Persistence Strategy:** Local JSON store for standalone offline operation with seamless cloud synchronization connector for Firebase Firestore (`firebase_config.py`).

### 8.2 Deliverable Artifacts in Repository
- `docs/Lab_02_Software_Development_Approach_Selection.pdf`
- `docs/Lab_03_Software_Requirements_Specification_SRS.pdf`
- `docs/Project_Proposal_ZeroBuild_Studio.pdf`
- `docs/Lab_07_Jira_Agile_Project_Management.md`
- `docs/Lab_07_Software_Engineering_Lab_JIRA_Project_Management.pdf`
- `docs/jira_import_lab07.csv` (One-click JIRA issue import)

---

## 9. Peer Reviews

### 9.1 Peer Review Record
| Pull Request | Branch | Author | Reviewer | Review Focus | Outcome / Feedback | Status |
|:------------:|:-------|:-------|:---------|:-------------|:-------------------|:------:|
| **PR #1** | `feature/KAN-15-routing` | Md Shirajul Islam | Md Sad Ullah | Regex safety, route collisions | "Routing is clean; added edge-case test for trailing slash." | Approved |
| **PR #2** | `feature/KAN-18-product-crud` | Abdullah Al Shawon | Md Shirajul Islam | Validation & memory leaks | "Ensure image string is sanitized before writing to JSON." | Approved |
| **PR #3** | `feature/KAN-17-ssr-theme` | Arpita Sannamat | Sanjana Zarin | Mobile CSS grid responsiveness | "Checked on Chrome DevTools mobile view; padding adjusted." | Approved |
| **PR #4** | `add-readme` | Md Shirajul Islam | Abdullah Al Shawon | README documentation & showcase | "Accurate team roles and Jira links. Verified." | Approved |

---

## 10. Integration and Deployment

### 10.1 Integration Workflow
1. Feature branches merged into `main` after PR approval and local test validation.
2. Server runner `server.py` boots HTTP server on port 8000:
   ```bash
   python server.py
   ```
3. Endpoints verified:
   - Admin Panel: `http://localhost:8000/`
   - Customer Storefront: `http://localhost:8000/s/myshop`
   - Healthcheck & REST API: `http://localhost:8000/api/products`

### 10.2 Deployment Readiness Checklist
- [x] Zero framework dependencies: Tested on standard Python 3.11 installation.
- [x] Cross-origin Resource Sharing (CORS) configured for API clients.
- [x] Clean `.gitignore` masking virtualenvs and credentials (`serviceAccountKey.json`).
- [x] High-resolution UI screenshots staged in `screenshots/`.

---

## 11. Feedback and Retrospectives

### 11.1 Sprint Retrospective (Sprint 3)
- **What Went Well (WWW):**
  - High team velocity and strong adherence to framework-less architecture.
  - Seamless collaboration using JIRA Smart Commits and GitHub Pull Requests.
  - Dynamic SSR engine delivered exceptional load performance (<100ms).
- **What Could Be Improved (WCBI):**
  - Base64 images in local JSON increase file size; future iteration should store files on disk/blob storage.
  - Adding automated GitHub Actions CI pipeline for continuous linting.
- **Action Items (AIs):**
  1. Optimize image payloads using client-side canvas compression.
  2. Implement unit tests using Python `unittest` module.

### 11.2 Instructor Feedback (Nahida Akter Tanjila)
- **Feedback Summary:** Praised the framework-less architecture and thorough Software Requirements Specification (SRS). Commended the proactive tracking of user stories and smart commits on JIRA.
- **Action Taken:** Expanded the dual pricing structure and added comprehensive automated test cases as requested in Lab 07.

---
*Report compiled by **Md Shirajul Islam (20245103198)** on behalf of Team ZeroBuild Studio.*

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "CSE 328: Software Engineering Lab — Lab 07: Agile Project Management Using JIRA")
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)

        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, "ZeroBuild Studio | BUBT Department of CSE | Jira Key: KAN")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 46, 558, 46)
        self.restoreState()

def create_lab07_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#003366'),
        alignment=1, # Center
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0052CC'),
        alignment=1,
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#444444'),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#003366'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#0052CC'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#222222'),
        spaceAfter=5
    )

    table_header_style = ParagraphStyle(
        'THStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TDStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#222222')
    )

    table_cell_center = ParagraphStyle(
        'TDStyleCenter',
        parent=table_cell_style,
        alignment=1
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#111111'),
        backColor=colors.HexColor('#F4F5F7'),
        borderPadding=4,
        spaceAfter=5
    )

    story_box = ParagraphStyle(
        'StoryBox',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#172B4D'),
        backColor=colors.HexColor('#EBECF0'),
        borderPadding=5,
        spaceAfter=4
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("LAB 07: AGILE PROJECT MANAGEMENT USING JIRA", title_style))
    story.append(Paragraph("Software Engineering Lab (CSE 328) | Academic Project Report", subtitle_style))
    story.append(Paragraph("<b>Department of Computer Science & Engineering</b><br/>Bangladesh University of Business and Technology (BUBT)", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#003366'), spaceAfter=10))

    # Team Table
    story.append(Paragraph("Project Details & Team Identification", h2_style))
    team_data = [
        [Paragraph("Project Name", table_header_style), Paragraph("ZeroBuild Studio (ZeroBuildStdio)", table_cell_style),
         Paragraph("Jira Key / Board", table_header_style), Paragraph("KAN (Board ID: 2)", table_cell_style)],
        [Paragraph("Supervisor", table_header_style), Paragraph("Nahida Akter Tanjila (Lecturer, CSE)", table_cell_style),
         Paragraph("GitHub Repo", table_header_style), Paragraph("github.com/mdshirajulislam/ZeroBuildStdio", table_cell_style)]
    ]
    t_info = Table(team_data, colWidths=[90, 162, 90, 162])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#0052CC')),
        ('BACKGROUND', (2,0), (2,-1), colors.HexColor('#0052CC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 6))

    roster_data = [
        [Paragraph("Name", table_header_style), Paragraph("Student ID", table_header_style), Paragraph("Intake / Sec", table_header_style), Paragraph("JIRA / Project Responsibility", table_header_style)],
        [Paragraph("<b>Md Shirajul Islam</b> (Lead)", table_cell_style), Paragraph("20245103198", table_cell_center), Paragraph("Intake 53, Sec 05", table_cell_center), Paragraph("Project Lead, Backend Core Routing & SaaS Architecture", table_cell_style)],
        [Paragraph("<b>Md Sad Ullah</b>", table_cell_style), Paragraph("20245103163", table_cell_center), Paragraph("Intake 53, Sec 05", table_cell_center), Paragraph("Multi-Tenant Database Architecture & Shop Controller Logic", table_cell_style)],
        [Paragraph("<b>Sanjana Zarin</b>", table_cell_style), Paragraph("20245103169", table_cell_center), Paragraph("Intake 53, Sec 05", table_cell_center), Paragraph("Customer Shopping Cart Engine & Checkout Processing Workflow", table_cell_style)],
        [Paragraph("<b>Abdullah Al Shawon</b>", table_cell_style), Paragraph("20245103200", table_cell_center), Paragraph("Intake 53, Sec 05", table_cell_center), Paragraph("Product Search, Category Filter Engine & POS Module", table_cell_style)],
        [Paragraph("<b>Arpita Sannamat</b>", table_cell_style), Paragraph("20245103026", table_cell_center), Paragraph("Intake 53, Sec 05", table_cell_center), Paragraph("Storefront SSR Engine & Dynamic Theme Customizer", table_cell_style)],
    ]
    t_roster = Table(roster_data, colWidths=[120, 70, 75, 239])
    t_roster.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_roster)
    story.append(Spacer(1, 10))

    # 1. Project Setup
    story.append(Paragraph("1. Project Setup in JIRA", h1_style))
    story.append(Paragraph(
        "A dedicated software development project was configured in Atlassian JIRA using the key <b>KAN</b>. "
        "The project is structured under an Agile Incremental methodology supporting both Scrum sprint cycles and Kanban flow tracking.",
        body_style
    ))
    setup_items = [
        "<b>Project Components:</b> <code>Backend-Engine</code> (core routing & HTTP dispatchers), <code>Multi-Tenant-Store</code> (subdomain resolver & shop config), <code>Product-Catalog</code> (CRUD, dual pricing & Base64 images), <code>Storefront-SSR</code> (server-rendered templates), <code>Admin-Customizer</code> (theme editor & modals), and <code>Cart-Checkout</code> (cart & orders).",
        "<b>Milestone Releases / Versions:</b> <code>v0.1.0-alpha</code> (Sprint 1: Core Foundation), <code>v0.2.0-beta</code> (Sprint 2: Storefront & Catalog), and <code>v1.0.0-release</code> (Sprint 3: Full Integration & Deployment).",
        "<b>Board Workflow:</b> <code>Backlog</code> &rarr; <code>To Do</code> &rarr; <code>In Progress</code> &rarr; <code>In Review / QA</code> &rarr; <code>Done</code>.",
        "<b>Definition of Done (DoD):</b> Framework-less Python 3.11 compliance, all sub-tasks resolved in JIRA, peer-reviewed via Pull Request, zero critical defects in QA, and commits linked with JIRA Smart Commit keys."
    ]
    for item in setup_items:
        story.append(Paragraph(f"• {item}", body_style))

    # 2. User Stories & Requirements
    story.append(Paragraph("2. User Stories and Requirements", h1_style))
    story.append(Paragraph(
        "Requirements were synthesized from the formal SRS document (Lab 03) into 5 high-level Epics (<code>KAN-E1</code> to <code>KAN-E5</code>) "
        "and broken down into user stories with Fibonacci story points (1, 2, 3, 5, 8) and explicit acceptance criteria:",
        body_style
    ))

    stories_data = [
        ("KAN-15 (5 SP)", "Tenant Subdomain Routing", "As a SaaS tenant, I want my store accessible via /s/<subdomain>, so that customers access my branded store.", "Given valid subdomain, when accessed, renders dynamic SSR storefront; returns 404 for unknown store."),
        ("KAN-16 (5 SP)", "Shop Configuration & Isolation", "As an admin, I want tenant data strictly isolated in persistence, so that merchants cannot access others' stores.", "Given PUT /api/shops, modifies only active tenant store; validates JSON schema with atomic commits."),
        ("KAN-17 (8 SP)", "Storefront SSR Template Engine", "As a shopper, I want server-side rendered pages in pure Python, so that page load times stay under 150ms.", "Renders semantic HTML/CSS without external npm bundles; mobile responsive grid collapses seamlessly."),
        ("KAN-18 (5 SP)", "Product Catalog CRUD Logic", "As a merchant, I want to create, edit, list, and delete products, so that my catalog remains current.", "Given product POST/PUT, persists UUID, title, stock, and validates unique SKUs in memory store."),
        ("KAN-19 (3 SP)", "Dual Pricing Engine", "As a merchant, I want regular and promotional sale prices, so that customers see clear discount incentives.", "Given regular ৳450 and sale ৳380, renders strike-through; rejects sale price higher than regular."),
        ("KAN-20 (3 SP)", "Base64 Image Pipeline", "As a store owner, I want to upload product images via modal, so that hosting costs remain zero.", "Encodes image payload to Base64 in JSON; enforces 2MB size ceiling with user warning modal."),
        ("KAN-21 (8 SP)", "Live Theme Customizer", "As an admin, I want live color & banner editing with instant preview, so that I can inspect styling before save.", "Color picker updates iframe preview in real time; save persists settings to tenant JSON."),
        ("KAN-23 (5 SP)", "Cart & Order Workflow", "As a buyer, I want to add items to cart and view itemized summary, so that I can checkout smoothly.", "Cart maintains client state, increments badge counter, and accurately calculates grand totals.")
    ]

    for key, title, us, ac in stories_data:
        story.append(Paragraph(f"<b>[{key}] {title}</b>", h2_style))
        story.append(Paragraph(f"<b>User Story:</b> {us}", story_box))
        story.append(Paragraph(f"<b>Acceptance Criteria:</b> {ac}", body_style))

    # 3. Task Management & Matrix
    story.append(Paragraph("3. Task Management & Work Breakdown Structure", h1_style))
    story.append(Paragraph("Actionable engineering tasks were distributed across team members with tracked story points, priorities, and deadlines:", body_style))

    task_table_data = [
        [Paragraph("Key", table_header_style), Paragraph("Task Summary", table_header_style), Paragraph("Component", table_header_style), Paragraph("Assignee", table_header_style), Paragraph("SP", table_header_style), Paragraph("Priority", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("KAN-15.1", table_cell_center), Paragraph("Regex URL dispatcher in routes.py", table_cell_style), Paragraph("Backend", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("2", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-15.2", table_cell_center), Paragraph("Add 404 fallback page handler", table_cell_style), Paragraph("Backend", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("1", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-16.1", table_cell_center), Paragraph("Create shop_controller.py logic", table_cell_style), Paragraph("Multi-Tenant", table_cell_style), Paragraph("Md Sad Ullah", table_cell_style), Paragraph("3", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-16.2", table_cell_center), Paragraph("Multi-tenant JSON isolation", table_cell_style), Paragraph("Multi-Tenant", table_cell_style), Paragraph("Md Sad Ullah", table_cell_style), Paragraph("2", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-17.1", table_cell_center), Paragraph("HTML template generator in Python", table_cell_style), Paragraph("Storefront", table_cell_style), Paragraph("Arpita Sannamat", table_cell_style), Paragraph("5", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-17.2", table_cell_center), Paragraph("Mobile viewport responsive styles", table_cell_style), Paragraph("Storefront", table_cell_style), Paragraph("Arpita Sannamat", table_cell_style), Paragraph("3", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-18.1", table_cell_center), Paragraph("/api/products CRUD endpoints", table_cell_style), Paragraph("Product", table_cell_style), Paragraph("Abdullah Al Shawon", table_cell_style), Paragraph("3", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-18.2", table_cell_center), Paragraph("Validate stock & unique SKU", table_cell_style), Paragraph("Product", table_cell_style), Paragraph("Abdullah Al Shawon", table_cell_style), Paragraph("2", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-19", table_cell_center), Paragraph("Dual pricing engine validation", table_cell_style), Paragraph("Product", table_cell_style), Paragraph("Abdullah Al Shawon", table_cell_style), Paragraph("3", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-20", table_cell_center), Paragraph("Base64 media upload pipeline", table_cell_style), Paragraph("Product", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("3", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-21", table_cell_center), Paragraph("Admin live theme customizer", table_cell_style), Paragraph("Admin", table_cell_style), Paragraph("Arpita Sannamat", table_cell_style), Paragraph("8", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-23.1", table_cell_center), Paragraph("Cart state & badge counter", table_cell_style), Paragraph("Checkout", table_cell_style), Paragraph("Sanjana Zarin", table_cell_style), Paragraph("3", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-23.2", table_cell_center), Paragraph("Itemized subtotal & order summary", table_cell_style), Paragraph("Checkout", table_cell_style), Paragraph("Sanjana Zarin", table_cell_style), Paragraph("2", table_cell_center), Paragraph("Med", table_cell_center), Paragraph("Done", table_cell_center)],
        [Paragraph("KAN-24", table_cell_center), Paragraph("Automated REST test suite", table_cell_style), Paragraph("Backend", table_cell_style), Paragraph("Sanjana Zarin", table_cell_style), Paragraph("3", table_cell_center), Paragraph("High", table_cell_center), Paragraph("Done", table_cell_center)],
    ]
    t_tasks = Table(task_table_data, colWidths=[45, 175, 75, 100, 24, 40, 45])
    t_tasks.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_tasks)
    story.append(Spacer(1, 8))

    # 4. Sprint Planning
    story.append(Paragraph("4. Sprint Planning & Velocity", h1_style))
    story.append(Paragraph(
        "Project development was scheduled across 3 two-week sprints aligned with lab milestones. "
        "The team maintained an average velocity of <b>22 Story Points / Sprint</b> with 100% completion rate:",
        body_style
    ))
    sprint_data = [
        [Paragraph("Sprint", table_header_style), Paragraph("Duration", table_header_style), Paragraph("Sprint Goal", table_header_style), Paragraph("Committed", table_header_style), Paragraph("Completed", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("Sprint 1", table_cell_center), Paragraph("Weeks 1 - 2", table_cell_center), Paragraph("Framework-less server, multi-tenant routing & schema setup", table_cell_style), Paragraph("21 SP", table_cell_center), Paragraph("21 SP", table_cell_center), Paragraph("Closed", table_cell_center)],
        [Paragraph("Sprint 2", table_cell_center), Paragraph("Weeks 3 - 4", table_cell_center), Paragraph("SSR storefront renderer, product CRUD & dual pricing", table_cell_style), Paragraph("24 SP", table_cell_center), Paragraph("24 SP", table_cell_center), Paragraph("Closed", table_cell_center)],
        [Paragraph("Sprint 3", table_cell_center), Paragraph("Weeks 5 - 6", table_cell_center), Paragraph("Live theme customizer, cart workflow, QA & documentation", table_cell_style), Paragraph("21 SP", table_cell_center), Paragraph("21 SP", table_cell_center), Paragraph("Closed", table_cell_center)],
    ]
    t_sprint = Table(sprint_data, colWidths=[55, 65, 230, 50, 50, 54])
    t_sprint.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0052CC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_sprint)
    story.append(Spacer(1, 8))

    # 5. Daily Standups
    story.append(Paragraph("5. Daily Standups", h1_style))
    story.append(Paragraph(
        "Regular standup synchronizations were held to identify blockers and update JIRA card statuses. Key highlights:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Sprint 1 (Day 4):</b> Md Sad Ullah reported potential cross-tenant leakage during shop profile updates. Resolved by enforcing strict shop_id validation filters before commit.<br/>"
        "• <b>Sprint 2 (Day 6):</b> Abdullah Al Shawon flagged an edge case where promotional price exceeded regular price. Added validation in <code>product_controller.py</code> returning HTTP 422.<br/>"
        "• <b>Sprint 3 (Day 8):</b> Sanjana Zarin and Md Shirajul Islam verified automated regression tests across all 20 API endpoints; moved remaining tickets from <code>In Review</code> to <code>Done</code>.",
        body_style
    ))

    # 6. Coding & Development
    story.append(Paragraph("6. Coding and Development", h1_style))
    story.append(Paragraph(
        "Development strictly followed branch isolation (<code>main</code> & <code>feature/KAN-*</code>) and Atlassian Smart Commits:",
        body_style
    ))
    story.append(Paragraph("git commit -m \"KAN-18 #comment Implement product CRUD validation and dual pricing #time 3h\"<br/>"
                           "git commit -m \"KAN-21 #comment Connect theme customizer color picker with live preview #close\"<br/>"
                           "git commit -m \"KAN-25 #comment Fix image upload payload truncation in Base64 handler #resolve\"", code_style))

    # 7. Testing & Quality Assurance
    story.append(Paragraph("7. Testing and Quality Assurance", h1_style))
    story.append(Paragraph("Comprehensive functional test cases and defect tracking were maintained in JIRA:", body_style))

    tc_data = [
        [Paragraph("ID", table_header_style), Paragraph("Story", table_header_style), Paragraph("Test Scenario", table_header_style), Paragraph("Expected Result", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("TC-01", table_cell_center), Paragraph("KAN-15", table_cell_center), Paragraph("GET /s/myshop dynamic routing", table_cell_style), Paragraph("Status 200, renders storefront HTML", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-02", table_cell_center), Paragraph("KAN-15", table_cell_center), Paragraph("GET /s/nonexistent fallback", table_cell_style), Paragraph("Status 404, clean error page", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-03", table_cell_center), Paragraph("KAN-16", table_cell_center), Paragraph("PUT /api/shops tenant config update", table_cell_style), Paragraph("Status 200, atomic store update", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-04", table_cell_center), Paragraph("KAN-18", table_cell_center), Paragraph("POST /api/products create item", table_cell_style), Paragraph("Status 201, UUID assigned & persisted", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-05", table_cell_center), Paragraph("KAN-19", table_cell_center), Paragraph("POST product with sale_price > price", table_cell_style), Paragraph("Status 422 Unprocessable Entity", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-06", table_cell_center), Paragraph("KAN-20", table_cell_center), Paragraph("Base64 1.2MB image upload", table_cell_style), Paragraph("Encoded data URI renders in UI", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-07", table_cell_center), Paragraph("KAN-23", table_cell_center), Paragraph("Cart total 2 x ৳380 calculation", table_cell_style), Paragraph("Subtotal displays exactly ৳760", table_cell_style), Paragraph("PASS", table_cell_center)],
        [Paragraph("TC-08", table_cell_center), Paragraph("KAN-24", table_cell_center), Paragraph("Cross-tenant modification security check", table_cell_style), Paragraph("Status 403 Forbidden", table_cell_style), Paragraph("PASS", table_cell_center)],
    ]
    t_tc = Table(tc_data, colWidths=[40, 48, 172, 194, 50])
    t_tc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_tc)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Resolved JIRA Defects:</b>", h2_style))
    story.append(Paragraph(
        "• <b>KAN-25 (High):</b> Base64 payload truncated by standard HTTP reader buffer limit &rarr; Increased read buffer in <code>server.py</code>.<br/>"
        "• <b>KAN-26 (Medium):</b> Promotional sale price could exceed regular price &rarr; Added comparison check in <code>product_controller.py</code>.<br/>"
        "• <b>KAN-27 (Low):</b> Cart drawer reset on page refresh &rarr; Synchronized state with browser <code>localStorage</code>.",
        body_style
    ))

    # 8. Documentation & 9. Peer Reviews
    story.append(Paragraph("8. Documentation & 9. Peer Reviews", h1_style))
    story.append(Paragraph(
        "All software artifacts, API schemas, and architectural decisions are synchronized in GitHub (<code>README.md</code> and <code>/docs</code>). "
        "Every Pull Request was formally peer-reviewed prior to merging into <code>main</code>:",
        body_style
    ))
    pr_data = [
        [Paragraph("PR #", table_header_style), Paragraph("Branch", table_header_style), Paragraph("Author", table_header_style), Paragraph("Reviewer", table_header_style), Paragraph("Key Review Finding / Feedback", table_header_style), Paragraph("Verdict", table_header_style)],
        [Paragraph("PR #1", table_cell_center), Paragraph("feature/KAN-15-routing", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("Md Sad Ullah", table_cell_style), Paragraph("Confirmed regex route matching; added trailing-slash safety check.", table_cell_style), Paragraph("Approved", table_cell_center)],
        [Paragraph("PR #2", table_cell_center), Paragraph("feature/KAN-18-products", table_cell_style), Paragraph("Abdullah Al Shawon", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("Validated product payload schema and in-memory persistence.", table_cell_style), Paragraph("Approved", table_cell_center)],
        [Paragraph("PR #3", table_cell_center), Paragraph("feature/KAN-17-ssr-theme", table_cell_style), Paragraph("Arpita Sannamat", table_cell_style), Paragraph("Sanjana Zarin", table_cell_style), Paragraph("Verified responsive CSS grid behavior on mobile breakpoints.", table_cell_style), Paragraph("Approved", table_cell_center)],
        [Paragraph("PR #4", table_cell_center), Paragraph("add-readme", table_cell_style), Paragraph("Md Shirajul Islam", table_cell_style), Paragraph("Abdullah Al Shawon", table_cell_style), Paragraph("Verified screenshots, role matrix, and live Jira board link.", table_cell_style), Paragraph("Approved", table_cell_center)],
    ]
    t_pr = Table(pr_data, colWidths=[38, 110, 86, 85, 135, 50])
    t_pr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0052CC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_pr)
    story.append(Spacer(1, 8))

    # 10. Integration & Deployment & 11. Feedback
    story.append(Paragraph("10. Integration & Deployment", h1_style))
    story.append(Paragraph(
        "Components were integrated and validated locally on port 8000 (<code>python server.py</code>). "
        "The system runs with zero third-party dependencies, verifying instant startup and minimal memory footprint (<30MB RSS). "
        "Production release was tagged as <b>v1.0.0-release</b> on GitHub.",
        body_style
    ))

    story.append(Paragraph("11. Feedback and Sprint Retrospectives", h1_style))
    story.append(Paragraph(
        "• <b>What Went Well (WWW):</b> High team velocity (22 SP/sprint), zero framework overhead, and instant page rendering (<150ms).<br/>"
        "• <b>What Could Be Improved (WCBI):</b> Base64 image encoding in JSON store increases file size; future version will stream media to disk.<br/>"
        "• <b>Action Items (AIs):</b> Add automated CI workflow for regression test execution on each PR.<br/>"
        "• <b>Faculty Feedback (Nahida Akter Tanjila):</b> Commended the pure Python architectural approach, comprehensive SRS traceability, and active JIRA tracking.",
        body_style
    ))
    story.append(Spacer(1, 15))

    # Signature Block
    sig_data = [
        [Paragraph("<b>Submitted By:</b>", body_style), Paragraph("<b>Supervised & Accepted By:</b>", body_style)],
        [Paragraph("<b>Md Shirajul Islam</b> (ID: 20245103198)<br/>On behalf of Team ZeroBuild Studio (BUBT Intake 53)", body_style),
         Paragraph("<b>Nahida Akter Tanjila</b><br/>Lecturer, Department of CSE, BUBT", body_style)]
    ]
    t_sig = Table(sig_data, colWidths=[250, 254])
    t_sig.setStyle(TableStyle([
        ('LINEABOVE', (0,1), (0,1), 1, colors.HexColor('#003366')),
        ('LINEABOVE', (1,1), (1,1), 1, colors.HexColor('#003366')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether(t_sig))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF generated successfully at:", output_path)

if __name__ == '__main__':
    output_pdf = r"D:\SWE Project\docs\Lab_07_Software_Engineering_Lab_JIRA_Project_Management.pdf"
    create_lab07_pdf(output_pdf)

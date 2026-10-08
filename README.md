# ZeroBuildStdio 🚀

Welcome to **ZeroBuildStdio** – A fully functional, multi-vendor e-commerce platform built strictly with **Python (Standard Library)** and **Vanilla JavaScript**. 

This project aims to provide a fast, secure, and easily extensible SaaS storefront and admin dashboard without relying on any heavy frameworks. It utilizes a custom Python `http.server` implementation for handling the backend and API endpoints.

---

## ✨ Features

- **Multi-Tenant SaaS Architecture:** Manage multiple isolated storefronts, each with its own subdomain and unique settings.
- **Admin Dashboard:** A robust backend panel for managing:
  - 🛍️ Shops (Creation and configuration)
  - 📦 Products (CRUD operations, pricing, and image management)
  - 🎨 Theme Customization (Header, Footer, Primary Colors, Category UI Builder, and Outlets Builder)
- **Dynamic Storefront Renderer:** Beautiful, user-facing storefronts generated on-the-fly dynamically.
- **Framework-less Environment:** Built fully with 100% Python standard libraries and Vanilla JS/HTML/CSS. No Next.js, Django, Flask, or external CSS frameworks.
- **Real-World Ready:** Features like Sale vs Regular Pricing, Image base64 uploads, interactive Modal-based workflows, and seamless UI/UX interactions.

---

## 🛠️ Technology Stack

- **Backend:** Python (`http.server` and custom routing logic)
- **Frontend:** Vanilla JavaScript, HTML5, CSS3
- **Data Persistence:** Modular approach, prepared for Firebase (`firebase-admin`) but falls back to local in-memory/JSON storage cleanly.

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdshirajulislam/ZeroBuildStdio.git
cd ZeroBuildStdio
```

### 2. Install Dependencies (Optional)
If you intend to use Firebase or other specific external modules:
```bash
pip install -r requirements.txt
```

### 3. Run the Server
Simply execute the Python server file to start the custom HTTP server:
```bash
python server.py
```
> **Note:** The server typically runs on `http://localhost:8000`.

### 4. Access the Application
- **Admin Dashboard:** Open your browser and navigate to `http://localhost:8000/`
- **Storefront Examples:** Access an active shop via `http://localhost:8000/s/<subdomain>`

---

## 📁 Project Structure

```
ZeroBuildStdio/
├── controllers/          # Business logic (e.g., product_controller, shop_controller)
├── utils/                # Utility modules (e.g., response helpers)
├── public/               # Static assets (HTML, CSS, JS)
├── server.py             # Entry point, initializes the HTTP Server
├── routes.py             # Handles GET, POST, PUT, DELETE routing
├── dashboard_renderer.py # Renders the secure admin UI dynamically
├── storefront_renderer.py # Renders the user-facing storefronts
└── requirements.txt      # Python dependencies (Firebase, etc.)
```

---

## 🤝 Contributing
Contributions, issues, and feature requests are always welcome! Let's build together without the bloat of frameworks.

## 📝 License
This project is open-source and available under the MIT License.

---
*Crafted with precision by Md. Shirajul Islam.*

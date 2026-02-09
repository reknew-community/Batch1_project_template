# Logistics Data Platform – FastAPI

This project exposes REST APIs for managing logistics master and transactional data using **FastAPI** and **MySQL**.
It is intended to be used by multiple teams via **Swagger UI** for creating, updating, and deleting data.

---

## 🚀 Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn
- Swagger (OpenAPI)

---

## 📁 Modules Covered
This service exposes APIs for the following tables:

- **Hubs**
- **Routes**
- **Route Hubs** (Route ↔ Hub mapping with sequence)
- **Bookings**

> Data creation is done via APIs. Tables can be auto-created locally for development.

---

## ⚙️ Project Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd FASTAPI_LOGISTICS

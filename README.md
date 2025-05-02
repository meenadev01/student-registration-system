# Student Registration System

A full-stack web application for managing student registrations, built with **React** (frontend) and **FastAPI** (backend). Features include student registration, login, search, filtering by department and CGPA, and deletion.

## 🚀 Features

- ✅ User authentication (login/register)
- 🎓 Student registration form
- 🔍 Search and filter by department, semester, and CGPA
- 🗑️ Delete student records
- 📦 FastAPI backend with MySQL integration
- ⚛️ React frontend with Axios and React Router

---

## 🖥️ Tech Stack

**Frontend:**  
- React  
- Axios  
- React Router  
- CSS

**Backend:**  
- FastAPI  
- MySQL  
- SQLAlchemy  
- CORS Middleware

---

## 🛠️ Setup Instructions

### 📌 Prerequisites
- Node.js and npm
- Python 3.9+
- MySQL

---

### 📦 Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload

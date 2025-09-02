# Task Manager API (FastAPI)

A simple Task Manager REST API built with FastAPI, SQLAlchemy, and JWT Authentication.  
Users can register, log in, and manage their personal tasks securely.  
Deployed live on Render.

---

## Features
- User registration and login with JWT authentication  
- Secure password hashing (bcrypt)  
- Create, Read, Update, Delete (CRUD) tasks  
- Each user can only access their own tasks  
- Task fields: id, title, description, status, due_date, created_at, updated_at  
- Task status as Enum (Pending, In Progress, Completed)  
- Pagination support (skip, limit) for listing tasks  

---

## Project Structure
```
app/
│── main.py
│── core/         # database, config, security
│── models/       # SQLAlchemy models (User, Task)
│── schemas/      # Pydantic schemas
│── routers/      # API routes (users, tasks)
│── auth/         # JWT handling and auth dependencies
```

---

## Run Locally

### 1. Clone repo

git clone https://github.com/shaifalichouhan/task-manager-api.git
```
cd task-manager-api
```

### 2. Create virtual environment
```
python -m venv .venv
```
# Windows
```
.\.venv\Scriptsctivate
```
# macOS/Linux
```
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the app
```
uvicorn app.main:app --reload
```

### 5. Open Swagger docs
```
http://127.0.0.1:8000/docs
```

---

## Deployment
Deployed on Render:  
Live API URL: https://task-manager-api-fd3r.onrender.com

---

## Example Workflow (Swagger)
1. Register: POST /api/users/register  
2. Login: POST /api/users/login → get JWT token  
3. Authorize: Paste token in Swagger "Authorize"  
4. Manage tasks:  
   - Create → POST /api/tasks/  
   - List → GET /api/tasks/  
   - Update → PUT /api/tasks/{id}  
   - Delete → DELETE /api/tasks/{id}  

---

## Deliverables
- GitHub Repo  
- Live API  
- Swagger Docs  

---



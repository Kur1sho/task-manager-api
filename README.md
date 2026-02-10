# Task Manager API
A production-style REST API built with FastAPI, featuring JWT authentication, user-scoped data, Docker support, and cloud deployment.

## Features
- User registration and login
- JWT authentication (protected endpoints)
- Per-user task isolation
- CRUD task operations
- SQLite persistence via SQLAlchemy
- Auto-generated OpenAPI/Swagger docs
- Dockerized for consistent deployment
- Cloud-deployable (Render)

## Tech Stack
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **JWT (python-jose)**
- **Passlib** (password hashing)
- **Docker**


## Live Demo
Swagger UI:  
https://task-manager-api-lgw0.onrender.com/docs
> Note: Render free instances may sleep when inactive. First request may take ~30–60 seconds.


## Run Locally (Windows PowerShell)
### 1) Create and activate virtual environment
powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
### 2) Install dependencies
pip install -r requirements.txt
### 3) Run the API
python -m uvicorn app.main:app --reload
### 4) Open docs
http://127.0.0.1:8000/docs
## Run with Docker
### Build the image
docker build -t task-api .
### Run the container
docker run -p 8000:8000 task-api
### Then open:
http://127.0.0.1:8000/docs

## API Overview
### Auth
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login and receive JWT token
### Tasks (JWT required)
Method	Endpoint	Description
GET	/tasks	Get users tasks
POST	/tasks	Create task
GET	/tasks/{task_id}	Get specific task
DELETE	/tasks/{task_id}	Delete task
## Deployment (Render)
This service is deployable as a Render Web Service using:
- requirements.txt for dependencies
- Procfile for the start command
### Example live deployment:
https://task-manager-api-lgw0.onrender.com/docs

## Purpose
This project demonstrates:
- Backend API design
- Authentication and authorization
- Database integration
- Containerization with Docker
- Cloud deployment workflow

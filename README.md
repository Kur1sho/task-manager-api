# Task Manager API

A simple Task Manager REST API built with FastAPI, SQLite, and JWT authentication.

## Features
- User registration + login
- JWT authentication (protected endpoints)
- CRUD tasks stored in SQLite
- Tasks are scoped to the authenticated user
- Auto-generated Swagger docs

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (password hashing)

## Run locally (Windows PowerShell)
### 1) Create and activate a virtual environment
powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
### 2) Install dependencies
pip install -r requirements.txt
### 3) Run the API
python -m uvicorn app.main:app --reload
### 4) Open docs
Swagger UI: http://127.0.0.1:8000/docs

## API Overview
### Auth
POST /auth/register (JSON body)
POST /auth/login (OAuth2 form: username + password)

### Tasks (JWT required)
GET /tasks
POST /tasks
GET /tasks/{task_id}
DELETE /tasks/{task_id}

## Deployment (Render)
This project is deployable as a Render Web Service using:
requirements.txt for dependencies
Procfile for the start command

Note: Render free instances may sleep when inactive, causing a short delay on first request.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task model
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str  # todo, doing, done


# In-memory storage
tasks: List[Task] = []


@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(i)
    raise HTTPException(status_code=404, detail="Task not found")

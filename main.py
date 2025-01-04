from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Step 1: Define the Task model
class Task(BaseModel):
    id: int
    title: str = Field(..., max_length=50, description="Title of the task")
    description: Optional[str] = Field(None, max_length=200, description="Details of the task")
    completed: bool = Field(default=False, description="Task completion status")

# Step 2: In-memory database to store tasks
tasks = []

# Step 3: Create operation
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    # Ensure unique IDs
    if any(existing_task["id"] == task.id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists.")
    
    tasks.append(task.dict())
    return task

# Step 4: Read all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Step 5: Read a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

# Step 6: Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found.")

# Step 7: Delete a task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return
    raise HTTPException(status_code=404, detail="Task not found.")

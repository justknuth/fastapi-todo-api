from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models import Todo, TodoCreate, TodoUpdate


router = APIRouter

db: List[Todo] = []
next_id = 1

@router.get('/')
def read_root():
    return {"message": "Welcome to the FastAPI To-Do API"}


@router.get('/todos', response_model=List[Todo])
def get_todos():
    return db


@router.post('/todos', response_model=Todo, status_code=201)
def create_todo(todo_create: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        task=todo_create.task,
        completed=False
    )
    db.append(new_todo)
    next_id += 1
    return new_todo


@router.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(stats_code=404, detail="Todo not found")


@router.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    for todo in db:
        if todo.id == todo_id:
            if todo_update.task is not None:
                todo.task = todo_update.task
            if todo_update.completed is not None:
                todo.completed = todo_update.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete('/todos/{todo_id}', status_code=204)
def delete_todo(todo_id: int):
    for i, todo in enumerate(db):
        if todo.id == todo_id:
            db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
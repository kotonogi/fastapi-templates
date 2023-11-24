from fastapi import APIRouter, Depends, HTTPException
from fastapi_templates.db import get_session
from fastapi_templates.services.tasks.api import get_tasks_repositorys
from fastapi_templates.services.tasks.models import Tasks
from fastapi_templates.services.tasks.schemas import TasksCreate, TasksRead, TasksUpdate

router = APIRouter()


@router.get("/", response_model=list[Tasks])
def list_tasks(limit=20, offset=0, session=Depends(get_session)):
    repo = get_tasks_repositorys(session)
    tasks = repo.list_tasks(limit, offset)
    return tasks


@router.post("/", response_model=TasksRead)
def create_task(task: TasksCreate, session=Depends(get_session)):
    repo = get_tasks_repositorys(session)
    return repo.create_task(task)


@router.get(path="/{id}", response_model=TasksRead)
def get_task(id: int, session=Depends(get_session)):
    repo = get_tasks_repositorys(session)
    task = repo.get_task(id)
    if task is None:
        return HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch(path="/{id}", response_model=TasksRead)
def update_task(id: int, task: TasksUpdate, session=Depends(get_session)):
    repo = get_tasks_repositorys(session)
    updated_task = repo.update_task(id, task)
    if updated_task is None:
        return HTTPException(status_code=404, detail="Task not found")
    return updated_task

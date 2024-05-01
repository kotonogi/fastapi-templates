from sqlmodel import Session

from .repository import TasksRepository


def get_tasks_repository(session: Session) -> TasksRepository:
    return TasksRepository(session)

from sqlmodel import Session

from .repository import TasksRepository


def get_tasks_repositorys(session: Session) -> TasksRepository:
    return TasksRepository(session)

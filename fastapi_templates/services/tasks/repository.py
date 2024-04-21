from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from fastapi_templates.services.tasks.schemas import TasksCreate, TasksUpdate

from .models import Tasks


class TasksRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_tasks(self, limit: int, offset: int) -> list[Tasks]:
        """登録されているタスクを取得する

        Args:
            limit (int): 取得結果数の上限
            offset (int): スキップする取得件数 e.g. 3 -> 4件目から4+{limit}件まで取得

        Returns:
            list[Tasks]: タスクのリスト
        """
        statement = select(Tasks).offset(offset).limit(limit)
        result = self.session.exec(statement).all()

        return list(result)

    def get_task(self, id: int) -> Optional[Tasks]:
        statement = select(Tasks).where(Tasks.id == id)
        results = self.session.exec(statement)
        try:
            return results.one()
        except NoResultFound:
            return None

    def create_task(self, task: TasksCreate) -> Tasks:
        target = Tasks.model_validate(task)
        self.session.add(target)
        self.session.commit()
        self.session.refresh(target)

        return target

    def update_task(self, id: int, task: TasksUpdate) -> Optional[Tasks]:
        update_target = self.get_task(id)

        if update_target is None:
            return None

        update_args = task.dict()

        for key, value in update_args.items():
            setattr(update_target, key, value)

        self.session.add(update_target)
        self.session.commit()
        self.session.refresh(update_target)

        return update_target

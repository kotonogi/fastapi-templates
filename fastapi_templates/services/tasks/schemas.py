from datetime import datetime

from .models import TasksBase


class TasksCreate(TasksBase):
    pass


class TasksRead(TasksBase):
    id: int


class TasksUpdate(TasksBase):
    name: str
    span_from: datetime
    span_to: datetime
    completed_at: datetime
    is_deleted: bool

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class TasksBase(SQLModel):
    name: str
    span_from: Optional[datetime] = None
    span_to: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_deleted: bool = False


class Tasks(TasksBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
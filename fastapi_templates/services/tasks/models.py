from datetime import datetime
from typing import Optional

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from sqlmodel import Field, SQLModel


class TasksBase(SQLModel):
    name: str
    span_from: None | datetime = None
    span_to: None | datetime = None
    completed_at: None | datetime = None
    is_deleted: bool = False

    model_config = ConfigDict(alias_generator=to_camel)


class Tasks(TasksBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

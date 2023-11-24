from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory
from fastapi_templates.services.tasks.models import Tasks


class TasksFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Tasks
        # セッション内のみの保存(トランザクションをコミットしない)
        sqlalchemy_session_persistence = "flush"

    name = Sequence(lambda x: f"タスク名-{x}")

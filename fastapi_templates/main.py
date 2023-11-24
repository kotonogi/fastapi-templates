from fastapi import FastAPI

from .services.tasks.views import router as tasks_router

app = FastAPI()


# 各APIパスルート
app.include_router(tasks_router, prefix="/tasks")

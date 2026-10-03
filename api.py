from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="Todo API — Разработчик: Галлямов Ришат")

app.include_router(todo_router)

from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи (Галлямов Ришат)",
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Прочитать следующую главу книги (Галлямов Ришат)",
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Пример задачи 1 (Галлямов Ришат)"},
                    {"item": "Пример задачи 2 (Галлямов Ришат)"},
                ]
            }
        }

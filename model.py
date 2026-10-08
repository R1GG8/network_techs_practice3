from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи (Галлямов Ришат)",
            }
        }

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


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
from fastapi import APIRouter, HTTPException, Path, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

templates = Jinja2Templates(directory="templates/")


@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        request,                                   
        "todo.html",                               
        {"todos": todo_list}                       
    )


@todo_router.get("/todo")
async def retrieve_todo(request: Request):
    return templates.TemplateResponse(
        request,
        "todo.html",
        {"todos": todo_list}
    )


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title="The ID of the todo to retrieve (Галлямов Ришат)."),
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request,
                "todo.html",
                {"todo": todo}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo с указанным ID не найдена (Галлямов Ришат).",
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="The ID of the todo to be updated (Галлямов Ришат)."),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo успешно обновлена Галлямовым Ришатом."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo с указанным ID не найдена для обновления (Галлямов Ришат).",
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(
    todo_id: int = Path(..., title="The ID of the todo to delete (Галлямов Ришат)."),
) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo успешно удалена Галлямовым Ришатом."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo с указанным ID не найдена для удаления (Галлямов Ришат).",
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Все задачи успешно удалены Галлямовым Ришатом."}
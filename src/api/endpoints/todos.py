import logging
from databases.database import Database
from databases.in_memory_database import InMemoryDatabase
from models.todo import Todo

# TODO: Replace with real database which implements the Database interface
db: Database = InMemoryDatabase()

def get_all():
    """
    Returns all the todos.
    Handles the request for GET /todos.
    """
    logging.debug("todos - get_all")
    #return [{"text": "test", "status": "active"},{"text2": "test", "status": "completed"}]
    return [todo.to_json() for todo in db.get_todos()], 200

def get_by_id(todo_id: str):
    """
    Returns the todo with this id or 404 if it isn't present.
    Handles the request for GET /todos/{todo_id}.
    """
    logging.debug(f"todos - get_by_id - id: {todo_id}")
    todo: Todo = db.get_todo_by_id(todo_id)
    if not todo:
        logging.error(f"todos - get_by_id - unable to find todo with id: {todo_id}")
        return f"Unable to find todo with id {todo_id}", 404

    return todo.to_json(), 200
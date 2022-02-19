import logging
from databases.database import Database

from databases.in_memory_database import InMemoryDatabase

# TODO: Replace with real database which implements the Database interface
db: Database = InMemoryDatabase()

def get_all():
    """
    Returns all the todos.
    """
    #return [{"text": "test", "status": "active"},{"text2": "test", "status": "completed"}]
    return [todo.to_json() for todo in db.get_todos()], 200
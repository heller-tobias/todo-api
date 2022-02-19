import logging
from typing import List
from databases.database import Database
from models.todo import Todo

class InMemoryDatabase(Database):
    """
    Represents an InMemoryDatabase which looses its state after the restart. Implements the Database interface.
    Is needed for the first implementation of an API.
    """
    def __init__(self) -> None:
        super().__init__()
        self.todos: List[Todo] = []

    def init(self) -> bool:
        """
        Initializes the database. In this case no connection is created.
        """
        pass

    def get_todos(self) -> List[Todo]:
        """
        Returns a list of all todos.
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: str) -> Todo:
        """
        Returns the todo with the passed id or None if it doesn't exist.
        """
        filtered = [todo for todo in self.todos if todo.id == todo_id]
        if not len(filtered):
            # IDEA: Could also throw exception but this happens to often.
            return None
        return filtered[0]

    def create_todo(self, todo: Todo) -> str:
        """
        Adds the todo to the database.
        Returns the id of the created todo.
        """
        # If it exist -> replace
        if self.get_todo_by_id(todo.id):
            self.delete_todo(todo.id)

        # If it doesn't exist -> add
        self.todos.append(todo)
        return todo.id

    def delete_todo(self, todo_id: str) -> bool:
        """
        Deletes the todo with a certain id.
        Returns whether the todo got deleted or not.
        """
        found_todo: Todo = self.get_todo_by_id(todo_id)

        if not found_todo:
            return False
        
        self.todos.remove(found_todo)
        return True
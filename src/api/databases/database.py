from typing import List

from models.todo import Todo

class Database():
    """
    Describes the Interface for a Database Connector used in this application.
    """
    
    def init(self) -> bool:
        """
        Initializes the database, e.g. starts connecting.
        Returns whether it was successful or not.
        """
        pass

    def get_todos(self) -> List[Todo]:
        """
        Returns a list of all todos.
        """
        pass

    def get_todo_by_id(self, todo_id: str) -> Todo:
        """
        Returns the todo with the passed id or None if it doesn't exist.
        """
        pass

    def create_todo(self, todo: Todo) -> str:
        """
        Adds the todo to the database.
        Returns the id of the newly added todo.
        """
        pass

    def delete_todo(self, todo_id: str) -> bool:
        """
        Deletes the todo with a certain id.
        Returns whether the todo got deleted or not.
        """
        pass
from datetime import datetime
from enum import Enum
from typing import Dict
import uuid

class TodoStatus(Enum):
    ACTIVE = 1,
    COMPLETED = 2

class Todo():
    """
    Represents a single Todo in the list.
    """

    def __init__(self, text: str, status: str, changed: str = datetime.now().isoformat(), id = uuid.uuid1()) -> None:
        """
        Initializes a Todo Object.
        
        :raises
            ValueError: if status is not valid.
        """
        self.text: str = text
        try:
            self.status = TodoStatus[status.upper()]
        except:
            raise ValueError(f"status: {status} not supported")
        self.changed = changed
        self.id = id

    
    def to_json(self) -> Dict:
        """
        Converts a Todo Object to JSON.
        """
        return {"id": self.id, "text": self.text, "status": self.status.name.lower(), "changed": self.changed}
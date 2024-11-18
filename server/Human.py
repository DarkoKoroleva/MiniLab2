from pydantic import BaseModel

class Human(BaseModel):
    name: str = None
    id: int = None

    def __init__(self, name, id):
        super().__init__()
        self.name = name
        self.id = id

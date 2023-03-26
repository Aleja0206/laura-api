from pydantic import  BaseModel

class Person(BaseModel):
    id: int
    name: str


class Friend(BaseModel):
    idfrom: int
    idto: int

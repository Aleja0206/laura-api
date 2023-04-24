from bson import ObjectId
from pydantic_mongo import ObjectIdField


class Income:
    id: ObjectIdField = None
    value: int
    reason: str

    class Config:
        json_encoders = {ObjectId: str}

from datetime import datetime

from bson import ObjectId
from pydantic_mongo import ObjectIdField


class Invoice:
    id: ObjectIdField = None
    value: int
    cause: str
    currency: str
    payment_method: str
    date: datetime = datetime.now()

    class Config:
        json_encoders = {ObjectId: str}


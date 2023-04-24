import os
from dotenv import load_dotenv

load_dotenv(override=False)
from pymongo import MongoClient
client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv("DATABASE")]
print(db.name)

print()

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "ai_journal"

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

entries_collection = db.entries 
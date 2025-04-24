from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi
import sys

load_dotenv()

# Get MongoDB connection string from environment variable
MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    raise ValueError("MONGODB_URL environment variable is required")

# Extract database name from connection string
DATABASE_NAME = os.getenv("DATABASE_NAME")
if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME environment variable is required")

# Get the CA certificate path
ca = certifi.where()

# Check if running on Render
is_on_render = os.getenv("RENDER") == "true"

# Create MongoDB client with Atlas configuration
client_options = {
    "tlsCAFile": ca,
    "retryWrites": True,
    "w": "majority",
    "serverSelectionTimeoutMS": 30000,  # Increase timeout to 30s
}

# Add this option only when on Render to bypass strict certificate verification
if is_on_render:
    client_options["tlsInsecure"] = True

client = AsyncIOMotorClient(MONGODB_URL, **client_options)
db = client[DATABASE_NAME]

entries_collection = db.entries 
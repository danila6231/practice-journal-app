from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi
import ssl

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

# Create MongoDB client connection options
if is_on_render:
    # Updated connection options for Render with TLS/SSL fixes
    client = AsyncIOMotorClient(
        MONGODB_URL,
        tlsCAFile=ca,
        tls=True,
        tlsInsecure=True,
        retryWrites=True,
        serverSelectionTimeoutMS=60000,
        connectTimeoutMS=30000,
        socketTimeoutMS=30000,
        w="majority"
    )
else:
    # Standard connection for local development
    client = AsyncIOMotorClient(
        MONGODB_URL,
        tlsCAFile=ca,
        retryWrites=True,
        w="majority"
    )

db = client[DATABASE_NAME]

entries_collection = db.entries 
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

# Get MongoDB connection string from environment variable
MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    raise ValueError("MONGODB_URL environment variable is required")

# Extract database name from connection string
DATABASE_NAME = MONGODB_URL.split('/')[-1].split('?')[0]
if not DATABASE_NAME:
    raise ValueError("Database name must be specified in the MongoDB URL")

# Get the CA certificate path
ca = certifi.where()

# Create MongoDB client with Atlas configuration
client = AsyncIOMotorClient(
    MONGODB_URL,
    tlsCAFile=ca,
    retryWrites=True,
    w="majority"
)
db = client[DATABASE_NAME]

entries_collection = db.entries 
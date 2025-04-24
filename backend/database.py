from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

# Get MongoDB connection string from environment variable
# Default to localhost if not provided
MONGODB_URL = os.getenv(
    "MONGODB_URL",
    "mongodb://localhost:27017/ai_journal"
)

# Extract database name from connection string or use default
if "mongodb+srv://" in MONGODB_URL:
    # For Atlas URLs, database name comes after the last '/'
    DATABASE_NAME = MONGODB_URL.split('/')[-1].split('?')[0] or "ai_journal"
else:
    # For local URLs, database name is the last part
    DATABASE_NAME = MONGODB_URL.split('/')[-1] or "ai_journal"

# Create MongoDB client with proper TLS configuration
client = AsyncIOMotorClient(
    MONGODB_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)
db = client[DATABASE_NAME]

entries_collection = db.entries 
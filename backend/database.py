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

# Create MongoDB client with Atlas configuration
client_options = {
    "retryWrites": True,
    "w": "majority",
    "serverSelectionTimeoutMS": 60000,  # Increase timeout to 60s
    "connectTimeoutMS": 30000,
    "socketTimeoutMS": 30000,
}

# Set SSL context options
if is_on_render:
    # Use more permissive SSL settings on Render
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    client_options["ssl_cert_reqs"] = ssl.CERT_NONE
    client_options["tlsInsecure"] = True
    client_options["ssl"] = True
else:
    # Standard SSL settings for local development
    client_options["tlsCAFile"] = ca

client = AsyncIOMotorClient(MONGODB_URL, **client_options)
db = client[DATABASE_NAME]

entries_collection = db.entries 
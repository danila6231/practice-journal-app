from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import entries

app = FastAPI(title="AI Journal API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(entries.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Journal API"} 
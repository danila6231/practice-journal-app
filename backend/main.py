from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import entries

app = FastAPI(title="AI Journal API")

# Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "http://localhost:8000",
#         "https://practice-journal-app.vercel.app",
#         "https://practice-journal-app.netlify.app",
#         "https://practice-journal-app.onrender.com",
#         "https://practice-journal-frontend.onrender.com",
#         "*",
#     ],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
#     expose_headers=["Content-Length"],
#     max_age=600,
# )

# Include routers
app.include_router(entries.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Journal API"} 
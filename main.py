# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.note_routes import router as note_router

# Initialize FastAPI app
app = FastAPI(
    title="Notes Management API",
    description="A simple REST API for managing notes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(note_router, tags=["notes"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Notes Management API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
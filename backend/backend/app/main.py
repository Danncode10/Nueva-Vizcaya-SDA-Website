from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.auth import router as auth_router
from .core.database import engine
from . import models

models.Base.metadata.create_all(bind=engine)  # Create tables for development

app = FastAPI(title="Nueva Vizcaya SDA Website API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to Nueva Vizcaya SDA Website API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

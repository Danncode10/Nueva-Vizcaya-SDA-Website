from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .api import auth
from .core.database import Base, engine
from .core.security import get_current_user_from_jwt # Import the new dependency
from .models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Nueva Vizcaya SDA Website API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Nueva Vizcaya SDA Website API"}

# Example of a protected endpoint
@app.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user_from_jwt)): # Use the new dependency
    return {"email": current_user.email, "id": current_user.id}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models import User, Role, UserRole
from ..core.config import settings
from pydantic import BaseModel
import boto3

router = APIRouter()

cognito = boto3.client('cognito-idp', region_name=settings.aws_region)

class RegisterRequest(BaseModel):
    email: str
    approver_name: str
    intended_role: str = "member"

class LoginRequest(BaseModel):
    email: str
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    # Check if user exists
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    # Find approver
    approvers = search_approvers(request.approver_name, request.intended_role, db)
    if not approvers:
        raise HTTPException(status_code=400, detail="No eligible approver found")

    approver = approvers[0]  # select first

    # Create user
    user = User(email=request.email, approver_id=approver.id, approval_status="pending")
    db.add(user)
    db.commit()

    # TODO: send notification to approver
    return {"message": "Registration request sent", "user_id": user.id}

def search_approvers(search_term: str, intended_role: str, db: Session):
    # For pastor, only admins
    if intended_role == "pastor":
        eligible_roles = ["admin"]
    else:
        eligible_roles = ["pastor", "admin"]

    # Find users with roles, email contains search_term
    users = db.query(User).filter(User.email.contains(search_term)).all()
    eligible = []
    for user in users:
        user_roles = db.query(Role.name).join(UserRole).filter(UserRole.user_id == user.id).all()
        role_names = [r.name for r in user_roles]
        if any(role in eligible_roles for role in role_names):
            eligible.append(user)
    return eligible

@router.post("/login")
def login(request: LoginRequest):
    try:
        response = cognito.admin_initiate_auth(
            UserPoolId=settings.cognito_user_pool_id,
            ClientId=settings.cognito_client_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': request.email,
                'PASSWORD': request.password
            }
        )
        return {
            "access_token": response['AuthenticationResult']['AccessToken'],
            "refresh_token": response['AuthenticationResult']['RefreshToken']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Login failed")

@router.post("/refresh")
def refresh_token(request: RefreshRequest):
    try:
        response = cognito.admin_initiate_auth(
            UserPoolId=settings.cognito_user_pool_id,
            ClientId=settings.cognito_client_id,
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': request.refresh_token
            }
        )
        return {
            "access_token": response['AuthenticationResult']['AccessToken']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Refresh failed")

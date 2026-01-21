from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models import User, Role, UserRole
from ..core.config import settings
from pydantic import BaseModel
import boto3
from typing import List

router = APIRouter()

cognito = boto3.client('cognito-idp', region_name=settings.aws_region)

class RegisterRequest(BaseModel):
    email: str
    password: str
    approver_id: int
    intended_roles: list[str] = ["member"]

class LoginRequest(BaseModel):
    email: str
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str

class ApproverResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    # Check if user exists
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    # Verify approver exists and has permission
    approver = db.query(User).filter(User.id == request.approver_id).first()
    if not approver:
        raise HTTPException(status_code=400, detail="Invalid approver")

    # TODO: check if approver has approval permission based on intended_roles

    # Create user
    user = User(email=request.email, approver_id=request.approver_id, approval_status="pending")
    db.add(user)
    db.commit()

    # TODO: store intended_roles, assign roles after approval
    # For now, just member role
    member_role = db.query(Role).filter(Role.name == "member").first()
    if member_role:
        user_role = UserRole(user_id=user.id, role_id=member_role.id)
        db.add(user_role)
        db.commit()

    # TODO: send notification to approver
    return {"message": "Registration request sent", "user_id": user.id}

@router.get("/approvers/search", response_model=List[ApproverResponse])
def search_approvers_endpoint(
    role: str = Query(..., description="Intended role for the user"),
    q: str = Query(..., description="Search term for approver name or email"),
    db: Session = Depends(get_db)
):
    if len(q) < 2:
        return []

    # For pastor, only admins can approve
    if role == "pastor":
        eligible_roles = ["admin"]
    else:
        eligible_roles = ["pastor", "admin"]

    # Search users by name or email
    users = db.query(User).filter(
        (User.email.contains(q)) | (User.email.contains(q))
    ).all()

    eligible = []
    for user in users:
        user_roles = db.query(Role.name).join(UserRole).filter(UserRole.user_id == user.id).all()
        role_names = [r.name for r in user_roles]
        if any(role_name in eligible_roles for role_name in role_names):
            eligible.append(ApproverResponse(id=user.id, name=user.email, email=user.email))  # Using email as name for now

    return eligible

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
        if 'AuthenticationResult' in response:
            return {
                "access_token": response['AuthenticationResult']['AccessToken'],
                "refresh_token": response['AuthenticationResult']['RefreshToken']
            }
        else:
            # Handle challenge (e.g., NEW_PASSWORD_REQUIRED)
            return {
                "challenge": response.get('ChallengeName'),
                "challenge_parameters": response.get('ChallengeParameters'),
                "session": response.get('Session')
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Login failed: {str(e)}")

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

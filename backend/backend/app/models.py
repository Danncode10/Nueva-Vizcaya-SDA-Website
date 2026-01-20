from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
import datetime
from .core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cognito_sub = Column(String, unique=True, nullable=True)  # Cognito user sub
    email = Column(String, unique=True, index=True)
    division_id = Column(Integer, ForeignKey("divisions.id"), nullable=True)
    church_id = Column(Integer, ForeignKey("churches.id"), nullable=True)
    approval_status = Column(String, default="pending")  # pending, approved, rejected
    approver_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    permissions = Column(JSON, default=list)

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)

class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    designated_pastor_id = Column(Integer, ForeignKey("users.id"), nullable=True)

class Church(Base):
    __tablename__ = "churches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    pastor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    division_id = Column(Integer, ForeignKey("divisions.id"))
    contact_info = Column(JSON, default=dict)

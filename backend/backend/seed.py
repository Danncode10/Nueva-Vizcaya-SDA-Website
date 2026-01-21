#!/usr/bin/env python3
"""
Seed script to populate initial data for testing.
Run with: python seed.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal, engine
from app.models import Role, User, UserRole
from sqlalchemy.orm import Session

def seed_data():
    db: Session = SessionLocal()

    try:
        # Create roles
        pastor_role = Role(name="pastor")
        admin_role = Role(name="admin")
        member_role = Role(name="member")

        db.add_all([pastor_role, admin_role, member_role])
        db.commit()

        # Create test users
        pastor_user = User(
            email="pastor@test.com",
            approval_status="approved"
        )
        admin_user = User(
            email="admin@test.com",
            approval_status="approved"
        )

        db.add_all([pastor_user, admin_user])
        db.commit()

        # Assign roles
        db.add(UserRole(user_id=pastor_user.id, role_id=pastor_role.id))
        db.add(UserRole(user_id=admin_user.id, role_id=admin_role.id))
        db.commit()

        print("✅ Seed data created successfully!")
        print(f"Created roles: pastor, admin, member")
        print(f"Created users: pastor@test.com (pastor), admin@test.com (admin)")
        print("You can now test registration with approver_name='pastor@test.com' or 'admin@test.com'")

    except Exception as e:
        print(f"❌ Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()

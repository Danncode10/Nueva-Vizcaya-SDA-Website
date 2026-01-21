import requests
from jose import jwt, jwk
from jose.utils import base64url_decode
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any

from app.core.config import settings
from app.core.database import get_db
from app.models import User
from sqlalchemy.orm import Session

security_scheme = HTTPBearer()

class CognitoJWTVerifier:
    def __init__(self, user_pool_id: str, region: str):
        self.user_pool_id = user_pool_id
        self.region = region
        self.jwks_url = f"https://cognito-idp.{region}.amazonaws.com/{user_pool_id}/.well-known/jwks.json"
        self.keys = self._fetch_jwks()

    def _fetch_jwks(self) -> Dict[str, Any]:
        try:
            response = requests.get(self.jwks_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()["keys"]
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Could not fetch JWKS: {e}")

    def decode_jwt(self, token: str) -> Dict[str, Any]:
        headers = jwt.get_unverified_headers(token)
        kid = headers['kid']

        key = next((k for k in self.keys if k['kid'] == kid), None)
        if not key:
            raise HTTPException(status_code=401, detail="Invalid token: JWK not found")

        # Reconstruct the public key
        try:
            public_key = jwk.construct(key)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Could not construct public key: {e}")

        # Decode and verify the token
        try:
            decoded_token = jwt.decode(
                token,
                public_key,
                algorithms=['RS256'], # Cognito uses RS256
                audience=settings.cognito_client_id,
                options={"verify_signature": True, "verify_aud": True, "verify_exp": True}
            )
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.JWTError as e:
            raise HTTPException(status_code=401, detail=f"Invalid token: {e}")

jwt_verifier = CognitoJWTVerifier(
    user_pool_id=settings.cognito_user_pool_id,
    region=settings.aws_region
)

async def get_current_user_from_jwt(credentials: HTTPAuthorizationCredentials = Security(security_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt_verifier.decode_jwt(credentials.credentials)
        username = payload.get('username') # Cognito uses 'username' for the user ID

        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials: Username missing in token")

        # In our current setup, Cognito users are linked to our local User model via email.
        # We need to rethink this if 'username' is not the email.
        # For now, assuming Cognito 'username' is the email we store in our User model.
        user = db.query(User).filter(User.email == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found in database")
        return user
    except HTTPException:
        raise # Re-raise already constructed HTTPExceptions
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Could not validate credentials: {e}")

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.db.base import Session
from app.security.jwt_utils import verify_access_token

security = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token:str = Depends(security)):
    return verify_access_token(token)

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()
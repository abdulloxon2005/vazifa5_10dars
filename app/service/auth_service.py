from os import access

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repo.user_repo import get_user_by_username
from app.schemas.auth_schemas import SignUpDto, LoginDto, TokenResponse
from app.repo import user_repo
from app.schemas.token_schemas import TokenData
from app.schemas.user_schemas import UserCreate
from app.security.jwt_utils import create_acces_token, create_refresh_token
from app.security.password_util import hash_password, verify_password


def sign_up(db: Session,signup_dto: SignUpDto):
    db_user = get_user_by_username(db,username=signup_dto.username)
    if db_user:
        raise ValueError("username is already exist")
    user_create = UserCreate(username=signup_dto.username,password=hash_password(signup_dto.password))
    return user_repo.add_user(db,user_create )

def login(db:Session,login_dto:LoginDto):
    db_user = get_user_by_username(db,username=login_dto.username)

    if not db_user or not verify_password(login_dto.password,db_user.password):
        raise HTTPException(status_code=401,detail="Username or password is not valid")

    roles = [role.name for role in db_user.roles]
    access_token = create_acces_token(TokenData(username=db_user.username,user_id=db_user.id,roles=roles))
    refresh_token = create_refresh_token(db_user.id)

    return TokenResponse(access_token=access_token,refresh_token=refresh_token)

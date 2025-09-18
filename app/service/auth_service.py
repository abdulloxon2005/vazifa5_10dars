from sqlalchemy.orm import Session

from app.repo.user_repo import get_user_by_username
from app.schemas.auth import SignUpDto
from app.repo import user_repo
from app.schemas.user_schemas import UserCreate
from app.security.password_util import hash_password


def sign_up(db: Session,signup_dto: SignUpDto):
    db_user = get_user_by_username(db,username=signup_dto.username)
    if db_user:
        raise ValueError("username is already exist")
    user_create = UserCreate(username=signup_dto.username,password=hash_password(signup_dto.password))
    return user_repo.add_user(db,user_create )
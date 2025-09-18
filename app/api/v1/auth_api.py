from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.auth_schemas import SignUpDto, TokenResponse, LoginDto
from app.schemas.user_schemas import UserResponse
from app.service.auth_service import sign_up,login

router = APIRouter(prefix="/auth",tags=["auth"])


@router.post("/signup",response_model=UserResponse)
def handle_signup(data:SignUpDto,db:Session = Depends(get_db)):
    return sign_up(db,signup_dto=data)


@router.post("/login",response_model=TokenResponse)
def handle_signup(data:LoginDto,db:Session = Depends(get_db)):
    return login(db,login_dto=data)

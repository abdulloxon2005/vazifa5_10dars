from fastapi import APIRouter
from fastapi.params import Depends

from app.api.deps import get_current_user, is_admin
from app.schemas.token_schemas import TokenData

router = APIRouter()


@router.get("/users/me",response_model=TokenData)
def handle_me(current_user:TokenData = Depends(get_current_user)):
    return current_user

@router.get("/users/admin")
def handle_me(current_user: TokenData = Depends(is_admin)):
    return f"salom admindan {current_user.username}"
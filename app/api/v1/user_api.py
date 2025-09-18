from fastapi import APIRouter
from fastapi.params import Depends

from app.api.deps import get_current_user
from app.schemas.token_schemas import TokenData

router = APIRouter()


@router.get("/users/me",response_model=TokenData)
def handle_me(current_user:TokenData = Depends(get_current_user)):
    return current_user
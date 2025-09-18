import uvicorn
from fastapi import FastAPI
from app.api.v1 import auth_api,user_api
from app.db import Base
from app.db.base import engine, Session
from app.schemas.auth_schemas import SignUpDto
from app.service.auth_service import add_admin
from app.schemas.user_schemas import UserCreate

Base.metadata.create_all(engine)
app = FastAPI()

# with Session() as session:
#
#     add_admin(session,SignUpDto(username="ali",password="admin"))
app.include_router(auth_api.router)
app.include_router(user_api.router)
uvicorn.run(app)
import uvicorn
from fastapi import FastAPI
from app.api.v1 import auth_api,user_api
from app.db import Base
from app.db.base import engine
Base.metadata.create_all(engine)
app = FastAPI()


app.include_router(auth_api.router)
app.include_router(user_api.router)
uvicorn.run(app)
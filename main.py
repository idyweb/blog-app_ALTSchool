from typing import List

from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session

from apis.base import api_router
from config import settings
from db.base_class import Base
from db.repository.blog import list_blogs
from db.session import engine
from db.session import get_db
from schemas.blog import ShowBlog


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/", response_model=List[ShowBlog])
def hello_api(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

from fastapi import FastAPI

from apis.base import api_router
from config import settings
from db.base_class import Base
from db.session import engine


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


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI🚀"}

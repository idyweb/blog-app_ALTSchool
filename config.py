import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "ALTSchool Second Semester Exams"
    PROJECT_VERSION: str = "1.0.0"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.db"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 10


settings = Settings()

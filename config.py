class Settings:
    PROJECT_NAME: str = "ALTschool Second Semester Exams"
    PROJECT_VERSION: str = "1.0.0"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.db"


settings = Settings()

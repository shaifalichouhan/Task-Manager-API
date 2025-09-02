from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager API"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./task_manager.db"
    SECRET_KEY: str  # <- put this in your .env (see instructions below)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # default 60 minutes

    class Config:
        env_file = ".env"


settings = Settings()

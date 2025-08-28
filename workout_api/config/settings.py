## To set up the main FastAPI application and include routers.
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
	app_name: str = "WorkoutAPI"
	DB_URL: str = Field(default="postgresql+asyncpg://user:password@localhost/workout_db")

settings = Settings()
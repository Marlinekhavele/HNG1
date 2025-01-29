from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    email: str = "your-email@example.com"
    github_url: str = "https://github.com/yourusername/your-repo"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Automatización Boyeros"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "change_me_in_production"
    
    # Database
    DATABASE_URL: str = "sqlite:///./boyeros.db"
    
    # ESP32 Defaults
    DEFAULT_POLLING_INTERVAL: int = 60  # seconds

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

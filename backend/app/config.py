from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "WeatherGPT"
    frontend_origin: str = "http://localhost:5173"
    weather_api_key: str = ""
    ai_api_key: str = ""
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

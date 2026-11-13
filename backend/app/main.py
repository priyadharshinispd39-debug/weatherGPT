from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routes import weather, chat, alerts, forecast, history, profile

app = FastAPI(title="WeatherGPT – SIH26068", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.frontend_origin,
        "http://localhost:5173",
        "https://whimsical-sundae-42774c.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(weather.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(alerts.router, prefix="/api")
app.include_router(forecast.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(profile.router, prefix="/api")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "WeatherGPT"}

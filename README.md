# WeatherGPT – SIH26068

AI-Powered Conversational Weather Intelligence prototype for IntelliJ IDEA.

## Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Health: http://127.0.0.1:8000/api/health

## Frontend
```bash
cd frontend
npm install
npm run dev
```
Open the URL shown by Vite, usually http://localhost:5173.

This starter is designed around the SIH26068 architecture: dashboard, conversational chat, role context, risk/advisory engine, alerts, history and map placeholders. Demo weather data is used so it runs without an API key; official weather/IMD feeds and an AI provider can be connected next.

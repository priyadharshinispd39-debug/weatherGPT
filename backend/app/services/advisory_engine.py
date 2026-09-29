from .weather_service import get_weather

def answer_question(question, city, role, language):
    w = get_weather(city); q = question.lower()
    if "spray" in q or "pesticide" in q:
        answer = f"Rain probability is {w['rain_probability']}% and wind is {w['wind_kmh']} km/h in {city}. Consider avoiding pesticide spraying during expected rainfall or strong-wind periods and follow local agricultural guidance."
    elif "fish" in q or "fishing" in q:
        answer = f"The prototype assessment for {city} is {w['risk']} risk, with wind around {w['wind_kmh']} km/h and rain probability {w['rain_probability']}%. Check official marine warnings before going offshore."
    elif "severe" in q or "danger" in q or "alert" in q:
        answer = f"The current prototype risk level for {city} is {w['risk']}. Check official warnings for confirmed extreme-weather information."
    else:
        answer = f"In {city}, it is {w['temperature']}°C with {w['humidity']}% humidity, {w['wind_kmh']} km/h wind and {w['rain_probability']}% rain probability. The prototype risk level is {w['risk']}."
    return {"question": question, "city": city, "role": role, "language": language, "risk": w["risk"], "answer": answer, "grounding": "Based on retrieved prototype weather data; connect authoritative feeds for deployment."}

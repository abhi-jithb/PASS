SUPPORTED_CITIES = ["karunagappally", "kollam", "kochi"]
WEATHER_DATA = {
    "kollam": {"temp": 28, "humidity": 50, "condition":"Mazha"},
    "karunagappally": {"temp": 28, "humidity": 70, "condition":"Venal"},
    "kochi": {"temp": 30, "humidity": 60, "condition":"Karmegham"}
}
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Weather API"}

@app.get("/cities")
def home_weather():
    return {"cities": SUPPORTED_CITIES}

@app.get("/weather/{city}")
def get_weather(city: str):
    city = city.lower()
    if city not in SUPPORTED_CITIES:
       return {"error": "City not supported"}
    return WEATHER_DATA[city]

@app.get("/weather/{city}/details")
def get_weather_details(city: str):
    if city not in SUPPORTED_CITIES:
        return {"error": "City not supported"}
    return {"city": city, "details": WEATHER_DATA[city]}


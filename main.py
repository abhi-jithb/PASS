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
def get_weather(city: str, unit: str = "C"):
    city = city.lower()
    if city not in SUPPORTED_CITIES:
        return {"error": "City not supported"}
    
    weather = WEATHER_DATA[city]
    temp_c = weather["temp"]

    if unit.upper() == "F":
        temp = temp_c * 9 / 5 + 32
    else:
        temp = temp_c

    return {
        "city": city,
        "temp": round(temp, 2),
        "unit": unit.upper(),
        "humidity": weather["humidity"],
        "condition": weather["condition"]
    }


@app.get("/weather/{city}/details")
def get_weather_details(city: str):
    if city not in SUPPORTED_CITIES:
        return {"error": "City not supported"}
    return {"city": city, "details": WEATHER_DATA[city]}


from fastapi import FastAPI
import random

SUPPORTED_CITIES = ["karunagappally", "kollam", "kochi", "paravur", "punalur", "kottarakkara", "chavara", "ochira", "anchal"]

WEATHER_DATA = {
    "kollam": {"temp": 28, "humidity": 50, "condition": "Mazha"},
    "karunagappally": {"temp": 29, "humidity": 60, "condition": "Venal"},
    "paravur": {"temp": 27, "humidity": 65, "condition": "Chill"},
    "punalur": {"temp": 26, "humidity": 70, "condition": "Mazha"},
    "kottarakkara": {"temp": 28, "humidity": 68, "condition": "Karmegham"},
    "chavara": {"temp": 29, "humidity": 72, "condition": "Venal"},
    "ochira": {"temp": 27, "humidity": 75, "condition": "Mazha"},
    "anchal": {"temp": 25, "humidity": 80, "condition": "Choodu"}
}

KOLLAM_FUN_FACT = [
    "Pacha Lays ath njangalku vendi aanu.",
    "We need hot peanuts else porinjadi nadakkum",
    "Biryaniyik opppam salad illlenkil, njangal seen aakuvee",
    "Forget gold or land disputes, here people fight over chips!",
    "Kollam’s nightlife? It’s like a twilight zone—shops close by 8 PM and the only nightlife you get is dodging stray dogs."
    "Kollam is that grumpy uncle in your family—tough exterior, but secretly sweet if you know him."
]

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

@app.get("/kollam/funfact")
def kollam_fun_fact():

    fact = random.choice(KOLLAM_FUN_FACT)

    return {
        "fun_fact": fact
    }

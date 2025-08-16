


<img width="1920" height="1080" alt="nasahub" src="https://github.com/user-attachments/assets/e8544200-f902-41ee-a2f2-7375cad5043d" />




# Project Name
Long Description about project. This project do that. This project is awesome...
## Team members
1. [Abhijit B](https://github.com/abhi-jithb)
2. [Sumayya Sainu](https://github.com/Zumayyahhh)

## Link to product walkthrough
[link to video](Link Here)


## How it Works?

1. Users interact with the FastAPI backend via an intuitive web UI that connects to multiple endpoints.
2. The API supplies weather data for supported cities, including temperature unit conversion, humidity, and weather conditions.
3. Kollam-specific endpoints feature randomized fun facts and humorous alerts reflecting local culture.
4. The frontend dynamically updates UI elements with icons, background themes, and animated cards for an engaging experience.  
5. Live API requests update weather info and fun facts seamlessly with async fetch calls.

*Embed your demo video here*

---

## Libraries Used

- **FastAPI** - for API backend and serving static front-end files  
- **Uvicorn** - ASGI server for running FastAPI  
- **JavaScript (Vanilla)** - frontend dynamic behavior  
- **CSS3** - styling and animations for a modern aesthetic  

---

## How to Configure

1. Clone the repository.  
2. Ensure you have Python 3.7+ installed.  
3. Install dependencies by running:  pip install fastapi uvicorn

4. Make sure the `static/` folder contains your `index.html`, `style.css`, and `script.js` files for the frontend.  
5. The FastAPI app is configured to mount the `static/` directory to serve frontend assets.

---

## How to Run

1. Start the FastAPI server using:  uvicorn main:app --reload
2. 2. Open your web browser and navigate to:  
http://127.0.0.1:8000/static/index.html

3. Use the UI to select cities, get weather, view fun facts, and enjoy Kollam’s unique weather alerts.  
4. Explore the API endpoints directly if needed for testing (e.g., `/weather/kollam`, `/kollam/funfact`).

---

Enjoy exploring Kollam’s weather with a splash of local flavor and humor!


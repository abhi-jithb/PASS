const API_BASE = '/api'; // Updated to use relative API paths
let currentUnit = 'C';
let selectedCity = null;

// Weather condition emojis
const weatherEmojis = {
    'Mazha': '🌧️',
    'Venal': '☀️',
    'Chill': '🌤️',
    'Karmegham': '☁️',
    'Choodu': '🔥'
};

// Load cities on page load
document.addEventListener('DOMContentLoaded', async () => {
    await loadCities();
});

async function loadCities() {
    try {
        const response = await fetch(`${API_BASE}/cities`);
        const data = await response.json();
        
        const cityGrid = document.getElementById('cityGrid');
        const citiesList = document.getElementById('citiesList');
        
        // Clear existing content
        cityGrid.innerHTML = '';
        citiesList.innerHTML = '';
        
        // Populate city buttons
        data.cities.forEach(city => {
            const button = document.createElement('button');
            button.className = 'city-btn';
            button.textContent = city;
            button.onclick = () => selectCity(city, button);
            cityGrid.appendChild(button);
            
            // Add to showcase list
            const tag = document.createElement('div');
            tag.className = 'city-tag';
            tag.textContent = city;
            citiesList.appendChild(tag);
        });
    } catch (error) {
        console.error('Error loading cities:', error);
        document.getElementById('weatherDisplay').innerHTML = 
            '<div class="error">Error loading cities. Please check if the API server is running.</div>';
    }
}

async function selectCity(city, button) {
    // Update active button
    document.querySelectorAll('.city-btn').forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
    
    selectedCity = city;
    await loadWeather(city);
}

async function loadWeather(city) {
    const weatherDisplay = document.getElementById('weatherDisplay');
    weatherDisplay.innerHTML = '<div class="loading">Loading weather data...</div>';
    
    try {
        const response = await fetch(`${API_BASE}/weather/${city}?unit=${currentUnit}`);
        const data = await response.json();
        
        if (data.error) {
            weatherDisplay.innerHTML = `<div class="error">${data.error}</div>`;
            return;
        }
        
        const emoji = weatherEmojis[data.condition] || '🌈';
        
        weatherDisplay.innerHTML = `
            <div class="weather-icon">${emoji}</div>
            <div class="temperature">${data.temp}°${data.unit}</div>
            <div class="condition">${data.condition}</div>
            <div class="humidity">💧 Humidity: ${data.humidity}%</div>
        `;
    } catch (error) {
        console.error('Error loading weather:', error);
        weatherDisplay.innerHTML = '<div class="error">Error loading weather data</div>';
    }
}

async function loadFunFact() {
    const funFactText = document.getElementById('funFactText');
    funFactText.innerHTML = 'Loading a fun fact... 🎲';
    
    try {
        const response = await fetch(`${API_BASE}/kollam/funfact`);
        const data = await response.json();
        
        funFactText.innerHTML = `"${data.fun_fact}" 😄`;
    } catch (error) {
        console.error('Error loading fun fact:', error);
        funFactText.innerHTML = 'Error loading fun fact. Please try again! 😅';
    }
}

// Unit toggle functionality
document.querySelectorAll('.unit-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
        document.querySelectorAll('.unit-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        currentUnit = btn.dataset.unit;
        
        if (selectedCity) {
            await loadWeather(selectedCity);
        }
    });
});

// Add some random floating animations
document.addEventListener('mousemove', (e) => {
    const shapes = document.querySelectorAll('.shape');
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    
    shapes.forEach((shape, index) => {
        const speed = (index + 1) * 50;
        const xOffset = (x - 0.5) * speed;
        const yOffset = (y - 0.5) * speed;
        
        shape.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
    });
});
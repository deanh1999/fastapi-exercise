from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv('API_KEY')
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.get("/", tags=["Hello World"], summary="test", description="Return hello world.")
def root():
    return {'hello' : 'world'}

# Endpoint to get weather data for a specific city
@app.get("/weather/{city}", tags=["Weather"], summary="Get weather data", description="Retrieve weather data for a specific city.")
def get_weather(city):
    weather_data = get_weather_data(city)
    processed_weather_data = process_weather_data(weather_data)
    return processed_weather_data


# Function to get weather data from the OpenWeatherMap API
def get_weather_data(city):
    params = {
        'q': city,
        'APPID': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail='City not found')
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()


# function to process and filter relevant weather data
def process_weather_data(data):
    main_data = data.get('main', {})
    if not main_data:
        raise ValueError("Invalid response from weather API")

    min_temp = main_data.get('temp_min')
    max_temp = main_data.get('temp_max')
    avg_temp = round((min_temp + max_temp) / 2, 2)
    humidity = main_data.get('humidity')

    return {
        'min_temperature': min_temp,
        'max_temperature': max_temp,
        'average_temperature': avg_temp,
        'humidity': humidity
    }


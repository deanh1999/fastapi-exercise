import requests

# Your API key (replace 'YOUR_API_KEY' with your actual API key)
api_key = '00d83c29be4cae3841c332b7fa131d23'
city = 'Belfast'
units = 'metric'
BASE_URL = 'http://127.0.0.1:8000'

def test_weather_api():
    url = f'{BASE_URL}/weather/{city}'

    try:
        response = requests.get(url)
        data = response.json()

        print(f"The max temp in {city} today: {data['max_temperature']}°C")
        print(f"The min temp in {city} today: {data['min_temperature']}°C")
        print(f"The average temp in {city} today: {data['average_temperature']}°C")
        print(f"Humidity in {city} today: {data['humidity']}%")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_weather_api()
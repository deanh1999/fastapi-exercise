import pytest
from main import process_weather_data, get_weather_data
from unittest.mock import patch, Mock
from fastapi import HTTPException

valid_data = {
        'coord': {'lon': -121.9358, 'lat': 37.7021},
        'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
        'base': 'stations',
        'main': {
            'temp': 17.08,
            'feels_like': 16.49,
            'temp_min': 10.82,
            'temp_max': 21.08,
            'pressure': 1012,
            'humidity': 63,
            'sea_level': 1012,
            'grnd_level': 987
        },
        'visibility': 10000,
        'wind': {'speed': 0.58, 'deg': 231, 'gust': 0.88},
        'clouds': {'all': 100},
        'dt': 1719319249,
        'sys': {'type': 2, 'id': 2005759, 'country': 'US', 'sunrise': 1719319652, 'sunset': 1719372800},
        'timezone': -25200,
        'id': 5344157,
        'name': 'Dublin',
        'cod': 200
    }

# Test weather data is processed correctly
def test_process_weather_data_valid():
    expected_result = {
        'min_temperature': 10.82,
        'max_temperature': 21.08,
        'average_temperature': round((10.82 + 21.08) / 2, 2),
        'humidity': 63
    }
 
    result = process_weather_data(valid_data)
    assert result == expected_result
 
# test invalid weather data passed in
def test_process_weather_data_invalid():
    invalid_data = {}
 
    with pytest.raises(ValueError) as exc_info:
        process_weather_data(invalid_data)
 
    assert str(exc_info.value) == "Invalid response from weather API"


# Test for a successful response
def test_get_weather_data_success():
    city = "Dublin"
    
    with patch('main.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = valid_data
        mock_get.return_value = mock_response
        result = get_weather_data(city)
        
        assert result == valid_data

# Test for a 404 error response
def test_get_weather_data_city_not_found():
    city = "testcity"
    
    with patch('main.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "City not found"
        mock_get.return_value = mock_response
        
        with pytest.raises(HTTPException) as exc_info:
            get_weather_data(city)
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "City not found"
 
# Test for a non-200 error response
def test_get_weather_data_error():
    city = "Dublin"
    
    with patch('main.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response
        
        with pytest.raises(HTTPException) as exc_info:
            get_weather_data(city)
       
        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "Internal Server Error"
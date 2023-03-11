import requests
import json

while True:
    # Accept user input for latitude and longitude
    latitude_str = input("Enter latitude: ")
    longitude_str = input("Enter longitude: ")

    # Convert latitude and longitude to float numbers
    try:
        latitude = float(latitude_str)
        longitude = float(longitude_str)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Set API endpoint URL and parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    # Make API request
    response = requests.get(url, params=params)

    # Parse JSON response into Python dictionary
    data = json.loads(response.text)

    # Extract current weather data from dictionary
    current_weather = data["current_weather"]
    current_temp = current_weather["temperature"]
    current_wind_speed = current_weather["windspeed"]

    # Print weather data
    print(f"Current temperature: {current_temp} C")
    print(f"Current wind speed: {current_wind_speed} m/s")
    break
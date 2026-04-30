# This python program get weather data from api, convert to json and save in file
import requests
import json

# Step 1: Input City
city = input("Enter the city name: ")

# Url
url = f"https://wttr.in/{city}?format=j1"

# Request data
response = requests.get(url)
data = response.json()

# Extract Temperature
temp = data['current_condition'][0]['temp_C']

# Create Result dictionary
weather_data = {
    "City": city,
    "Temperature": temp
}

# Save to JSON file
with open("weather_data.json", 'w') as file:
    json_data = json.dumps(weather_data)

# Print Result
print(f"\n📍 City: {city}")
print(f"Temperature: {temp}C")
print("✅Data saved to weather_data.json file. ")
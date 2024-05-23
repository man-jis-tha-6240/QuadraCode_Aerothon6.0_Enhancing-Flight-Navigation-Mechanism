# import requests
# import json

# # Example function to fetch data from an API (OpenWeatherMap API is used here)
# def fetch_weather_data(api_url):
#     response = requests.get(api_url)
#     return response.json()

# # Save sample data
# def save_sample_data(data, filename='../data/sample_data.json'):
#     with open(filename, 'w') as f:
#         json.dump(data, f)

# if __name__ == '__main__':
#     # Replace with your actual API key and URL
#     api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=a9763486b7b4e8d2cadbdde4ea55ef65'
#     sample_data = fetch_weather_data(api_url)
#     save_sample_data(sample_data)

import os
import requests
import json

# Example function to fetch data from an API (OpenWeatherMap API is used here)
def fetch_weather_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Save sample data
def save_sample_data(data, filename='./data/sample_data.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    # Replace with your actual API key and URL
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=a9763486b7b4e8d2cadbdde4ea55ef65'
    sample_data = fetch_weather_data(api_url)
    save_sample_data(sample_data)

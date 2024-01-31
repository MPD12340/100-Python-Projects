import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\nDetails of current weather\n")
    city = input("Please input the city name\n")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=imperial"
    
    weather_data = requests.get(request_url).json()
    print(f"current weather for {weather_data['name']}:\n")
    print(f"The temperature is {weather_data['main']['temp']}\n")
    print(f"The condition for the weather is {weather_data['weather'][0]['description']}")

if __name__=='__main__':
 get_current_weather()
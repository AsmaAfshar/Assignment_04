import requests
import os
api_key = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # response = requests.get(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad HTTP status codes
        data = response.json()
        print("\n🌦️ Weather Information:")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    except requests.exceptions.HTTPError:
        print("❌ City not found or API request returned an error.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")

def main():
    print("Welcome to the Weather App!")
    city = input("Enter city name: ").strip()
    api_key = "223ea76b5d265c919aa88680dded74ee"  # Replace with your real API key

    get_weather(city, api_key)
    

if __name__ == "__main__":
    main() 
    

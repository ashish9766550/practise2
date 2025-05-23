import requests
def weather(city_name,api_key):
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city_name,
        "appid":api_key,
        "units":"metric"
}
    
    try:
         response=requests.get(base_url,params=params) 
         response.raise_for_status()
         weather_data=response.json()
         return weather_data
    except requests.exceptions.ConnectionError as a:
        print("connection error",a)
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    return None

cityname="janakpur"
api_key="0f562fa6dcd12c675f1290478a6b6fd7"
weather_info=weather(cityname,api_key)
if weather_info:
    print(f"cityname:{cityname}")
    print(f"Description :{weather_info['weather'][0]['description'].capitalize()}")
    print(f"Temperature:{weather_info['main']['temp']}celcius")
    print(f"Feels like:{weather_info['main']['feels_like']}celcius")
    print(f"  Humidity: {weather_info['main']['humidity']}%")
    print(f"  Wind Speed: {weather_info['wind']['speed']} m/s")
    print(f"visibility:{weather_info['visibility']}")
    
else:
    print("error came in the city name ")




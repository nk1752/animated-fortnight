import os
import requests

def weather():
  print("weather function")
  
  city = os.getenv('CITY')
  print(f"city: {city}")

  API_key = os.getenv('API_KEY')
  print(f"API_key: {API_key}")

  #url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
  url = 'https://google.com'
  response = requests.get(url)
  data = response.json()
  print(f"weather: {data}")


  # with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
  #   print(f"result=Weather in {city} is 75F", file=fh)

if __name__ == '__main__':
    weather()
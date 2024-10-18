import os
import requests

def weather():
  city = os.getenv('CITY')
  print(f"city: {city}")

  API_key = os.getenv('API_kEY')
  print(f"API_key: {API_key}")

  url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
  response = requests.get(url)
  data = response.json()
  print(f"weather: {data}")


  # with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
  #   print(f"result=Weather in {city} is 75F", file=fh)

if __name__ == '__main__':
    weather()
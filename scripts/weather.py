import os
import requests

def weather():
  print("weather function")
  
  city = os.getenv('CITY')
  print(f"city: {city}")

  API_key = os.getenv('API_KEY')
  print(f"API_key: {API_key}")

  url = 'http://api.weatherapi.com/v1/current.json?key={API_key}&q={city}&aqi=yes'
  #url = 'https://google.com'
  response = requests.get(url)
  if response.status_code == 200:
    print("Success")
  else:
    print("Failed")
    

  # with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
  #   print(f"result=Weather in {city} is 75F", file=fh)

if __name__ == '__main__':
    weather()
import os
import requests
import json

def postman():
  print("Postman Echo function")
  
  
  url = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'
  response = requests.get(url)
  
  if response.status_code == 200:
    print("Success")
    data_json = response.json()
    print(data_json)
    data_dict = json.loads(data_json)
    print(data_dict)
  else:
    print("Failed")
    

  # with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
  #   print(f"result=Weather in {city} is 75F", file=fh)

if __name__ == '__main__':
    postman()
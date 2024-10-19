import os
import requests

def postman():
  print("Postman Echo function")
  
  
  url = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'
  response = requests.get(url)
  if response.status_code == 200:
    print("Success")
  else:
    print("Failed")
    

  # with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
  #   print(f"result=Weather in {city} is 75F", file=fh)

if __name__ == '__main__':
    postman()
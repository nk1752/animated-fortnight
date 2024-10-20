import os
import requests
import json

"""
json.dumps(): Serializes to a JSON string.
json.dump(): Serializes to a file or file-like object.
json.loads(): Deserializes from a JSON string.
json.load(): Deserializes from a file or file-like object.

"""


def postman() -> int:
    print("Postman Echo function")

    url = "https://postman-echo.com/get?foo2=bar2&foo5=bar5"
    response = requests.get(url)

    if response.status_code == 200:
        print("Success")    
    else:
        print("Failed")

    with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
        print(f"status_code={response.status_code}", file=fh)

    return response.status_code

if __name__ == "__main__":
    postman()

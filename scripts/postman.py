import os
import requests
import json


def postman() -> int:
    print("Postman Echo function")

    url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    response = requests.get(url)

    if response.status_code == 200:
        print("Success")

        print(f"Response: {response}")

        data_json = response.json()
        print(data_json)

        data_dict = json.loads(data_json)
        print(data_dict)

    else:
        print("Failed")

    with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
        print(f"statis_code={response.status_code}", file=fh)


if __name__ == "__main__":
    postman()

import os
import requests
import json


def postman() -> int:
    print("Postman Echo function")

    url = "https://postman-echo.com/get?foo2=bar2&foo5=bar5"
    response = requests.get(url)

    if response.status_code == 200:
        print("Success")

        # print respone
        print(json.dumps(response.json(), indent=4))

    else:
        print("Failed")

    with open(os.getenv("GITHUB_OUTPUT"), "a") as fh:
        print(f"statis_code={response.status_code}", file=fh)

    return response.status_code


if __name__ == "__main__":
    postman()

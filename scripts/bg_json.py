import os
import json

def bg_json() -> int:
    print("bg json function")

    # get bg value from env
    bg = os.getenv("BG")
    print(f"bg -> {bg}")

    # Open the JSON file and load it into a Python dictionary
    with open('config.json', 'r') as file:
        config_dict = json.load(file)

    # Print the dictionary
    #print(config_dict)

    # print all keys and values
    for key, value in config_dict.items():
        if key == "{bg}":
            print(key, value["DEV"])
            env_id = value["DEV"]
    
    # step values
    with open(os.getenv("GITHUB_OUTPUT"), "a") as fh:
        print(f"env_id={env_id}", file=fh)

if __name__ == '__main__':
    bg_json()
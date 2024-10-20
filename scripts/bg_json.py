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
        print(key, value["DEV"])

    # print RegionsBank DEV value
    env_id = config_dict['RegionsBank']['DEV']
    print(f"env_id -> {env_id}")
    
    # step values
    with open(os.getenv("GITHUB_OUTPUT"), "a") as fh:
        print(f"env_id={env_id}", file=fh)

if __name__ == '__main__':
    bg_json()
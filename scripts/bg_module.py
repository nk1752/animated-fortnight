import os
import json
import yaml


def bg_json(bg) -> int:
    print("bg json function")

    print(f"bg -> {bg}")
    # print bg data type
    print(f"bg data type -> {type(bg)}")

    # Open the JSON file and load it into a Python dictionary
    with open('config.json', 'r') as file:
        config_dict = json.load(file)

    print('key, value pairs of dictionary')
    for key, value in config_dict.items():
        print(f'key: {key} --> value: {value}')

    print(f'find bg value in dictionary & get env_id from DEV')
    env_id = None
    for key, value in config_dict.items():
        if key == 'BP':
            env_id = value['DEV']
            return 200
    return 0
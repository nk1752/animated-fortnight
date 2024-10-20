import os
import json
import yaml


def bg_json(bg):
    print("bg json function")

    print(f"bg -> {bg}")

    # Open the JSON file and load it into a Python dictionary
    with open('config.json', 'r') as file:
        config_dict = json.load(file)

    print('key, value pairs of dictionary')
    for key, value in config_dict.items():
        print(f'key: {key} --> value: {value}')

    print(f'find bg value in dictionary & get env_id from DEV')
    env_id = None
    for key, value in config_dict.items():
        if key == bg:
            env_id = value['DEV']
            break
        
def bg_json(bg):
    print("bg json function")

    print(f"bg -> {bg}")

    # Open the YAML file and load it into a Python dictionary
    with open('config.yaml', 'r') as file:
        config_dict = yaml.load(file, Loader=yaml.FullLoader)
    

    print('key, value pairs of dictionary')
    for key, value in config_dict.items():
        print(f'key: {key} --> value: {value}')

    print(f'find bg value in dictionary & get env_id from DEV')
    env_id = None
    for key, value in config_dict.items():
        if key == bg:
            env_id = value['DEV']
            break
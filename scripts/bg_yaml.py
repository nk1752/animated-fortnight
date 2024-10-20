import os
import yaml

def bg_json(bg) -> int:
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
    
    
    print(f'step values')
    with open(os.getenv("GITHUB_OUTPUT"), "a") as fh:
        print(f"env_id={env_id}", file=fh)


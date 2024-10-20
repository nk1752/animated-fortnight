import os
import yaml

def display_yaml():
  # load config.yaml
  with open('config.yaml') as fh:
    config_dict = yaml.load(fh, Loader=yaml.FullLoader)

  # print config.yaml
  print(f"config: {config_dict}")

  
if __name__ == '__main__':
    display_yaml()
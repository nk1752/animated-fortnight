import os
import json

def display_json():

  # load config.json
  with open('config.json') as fh:
    config_dict = json.load(fh)

  # print config.json
  print(f"config: {config_dict}", dafault_flow_style=False)

  with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
    print(f"result={config_dict['RegionsBank']['DEV']}", file=fh)

if __name__ == '__main__':
    display_json()
import os
import json

def display_json():

  # load config.json
  with open('config.json') as fh:
    config = json.load(fh)

  # print config.json
  print(f"config: {config}")

  with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
    print(f"result={config['RegionsBank']['DEV']}", file=fh)
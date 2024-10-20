import os

# import functions from bg_json.py and bg_yaml.py
from bg_module import bg_json
from bg_module import bg_yaml

def bg():
  bg = os.getenv("BG")

  bg_json(bg)
  bg_yaml(bg)

if __name__ == '__main__':
  bg()


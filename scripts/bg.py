import os

# import functions from bg_json.py and bg_yaml.py
from bg_module import bg_json


bg = os.getenv("BG")

bg_json(bg)

if __name__ == '__main__':
  bg()


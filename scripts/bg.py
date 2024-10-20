import os

# import functions from bg_json.py and bg_yaml.py
from bg_module import bg_json


bg = os.getenv("BG")

env_id = bg_json(bg)

print(f"{bg} env_id: {env_id}")

if __name__ == '__main__':
  bg()


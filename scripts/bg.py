import os

# import functions from bg_json.py and bg_yaml.py
from bg_module import bg_json


bg = os.getenv("BG")

status = bg_json(bg)

print(f"{bg} env_id: {status}")

if __name__ == '__main__':
  bg()


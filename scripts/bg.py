import os

# import functions from bg_json.py and bg_yaml.py
from bg_json import bg_json
from bg_yaml import bg_yaml

bg = os.getenv("BG")

bg_json(bg)
bg_yaml(bg)
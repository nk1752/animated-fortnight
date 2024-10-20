import os

# import functions from bg_json.py and bg_yaml.py
import bg_json
import bg_yaml

bg = os.getenv("BG")

bg_json(bg)
bg_yaml(bg)
# This is a simple python script that adds two numbers and returns the sum.
import os
import json

from dict import load_dict
from bg_module import bg_json

def main():

  bg_name = os.environ.get('BG_NAME')

  fgw_dict = load_dict(bg_name)

   # convert the fgw_dict to json
  json_data = json.dumps(fgw_dict, indent=4)
  print(json_data)

  # write the json data to a file
  with open('output.json', 'w') as file:
    file.write(json_data)

if __name__ == '__main__':
    main()
  
  
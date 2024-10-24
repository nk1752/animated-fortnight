# This is a simple python script that adds two numbers and returns the sum.
import os

from dict import load_dict
from bg_module import bg_json

def main():

  bg_name = os.environ.get('BG_NAME')

  load_dict(bg_name)

if __name__ == '__main__':
    main()
  
  
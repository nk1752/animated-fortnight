# This is a simple python script that adds two numbers and returns the sum.
import os

from my_module import my_function
from bg_module import bg_json

def main():

  my_function()  # Output: Hello from my function!
  status = bg_json('BG')  # Output: bg json function
  print(f"BG env_id: {status}")  # Output: BG env_id: 200

if __name__ == '__main__':
    main()
  
  
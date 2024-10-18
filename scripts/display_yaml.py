import os
import yaml

def mul_two():
  num1 = os.getenv('num1')
  num2 = os.getenv('num2')
  
  print(f"num 1: {num1}")
  print(f"num 2: {num2}")

  mul = int(num1) * int(num2)
  print(f"Mul: {mul}")

  with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
    print(f"result={mul}", file=fh)
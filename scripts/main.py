# This is a simple python script that adds two numbers and returns the sum.
import os

def main():
  num1 = os.getenv('num1')
  num2 = os.getenv('num2')
  
  print(f"num 1: {num1}")
  print(f"num 2: {num2}")

  sum = int(num1) + int(num2)
  print(f"Sum: {sum}")

  with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
    print(f"result={sum}", file=fh)

if __name__ == '__main__':
    main()
  
  
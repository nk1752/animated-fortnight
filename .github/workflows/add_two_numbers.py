# This is a simple python script that adds two numbers and returns the sum.
import os

def add_two_numbers()->int:

  a = os.getenv('num1')
  b = os.getenv('num2')
  
  sum = a + b
  print( f"a + b = sum" )
  
  os.setenv('sum', sum)
  return sum

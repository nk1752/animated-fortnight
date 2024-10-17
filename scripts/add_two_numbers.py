import sys
import os

def add_two_numbers()->int:

  a = os.getenv('num1')
  b = os.getenv('num2')
  
  sum = a + b
  print( f"a + b = sum" )
  
  os.setenv('sum', sum)
  return sum

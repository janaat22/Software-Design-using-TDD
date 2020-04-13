from functools import reduce
from validate_input_service import validate_input

def factorial(number):
  validate_input(number)
  
  return 1 if number == 0 else \
    reduce(lambda product, i: product * i, range(1, number + 1))

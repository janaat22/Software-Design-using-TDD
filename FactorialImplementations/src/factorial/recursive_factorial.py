from validate_input_service import validate_input

def factorial(number):
  validate_input(number)
  
  return 1 if number < 2 else number * factorial(number - 1)

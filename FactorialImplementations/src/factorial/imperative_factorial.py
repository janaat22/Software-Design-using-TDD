from validate_input_service import validate_input

def factorial(number):
  validate_input(number)
  
  product = 1
  
  for i in range(1, number + 1):
    product = product * i
  
  return product

import art

def add(n1,n2):
  '''Takes in 2 int or float inputs and adds them together.'''
  return n1 + n2

def subtract(n1,n2):
  '''Takes in 2 int or float inputs and subtracts one from the other.'''
  return n1 - n2

def multiply(n1,n2):
  '''Takes in 2 int or float inputs and multiplies them.'''
  return n1 * n2

def divide(n1,n2):
  '''Takes in 2 int or float inputs and divides one by the other.'''
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  }

def calculator():
  '''Performs calculations based on user input and allows for chaining operations.'''
  print(art.logo)
  
  num1 = float(input("First number: "))
  for symbol in operations:
    print(symbol)

  calculate = True

  while calculate:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Next number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    more_calculations = input(f"Type 'y' to perform another operation on {answer} or 'n' to start a new calculation: ")
    if more_calculations.lower() == 'y':
      num1 = answer
    else:
      calculate = False
      calculator()

calculator()
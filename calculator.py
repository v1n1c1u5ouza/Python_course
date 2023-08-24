while True:
  num_1 = input('Enter a number: ')
  num_2 = input('Enter another number: ')
  operator = input('Enter a operator (+-/*): ')
  
  valid_num = None
  num_1_float = 0
  num_2_float = 0
  
  try:
    num_1_float = float(num_1)
    num_2_float = float(num_2)
    valid_num = True
  except:
    valid_num = None

  if valid_num is None:
    print('One or both numbers is invalid.')
    continue
  
  valid_opearator = '+-/*'
  
  if operator not in valid_opearator:
    print('Invalid operator')
    continue
  
  if len(operator) > 1: 
    print('Enter only one operator')
    continue
  
  print('Executing the calculation. see the result down below')
  
  if operator == '+':
    print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
  elif operator == '-':
    print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
  elif operator == '/':
    print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
  elif operator == '*':
    print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
  else:
    print("You weren't supposed to get here")
  
  exit = input('You want to exit? [y]es: ').lower().startswith('y')
  
  if exit is True:
    break
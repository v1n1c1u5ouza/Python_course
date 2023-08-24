def multiply(*args):
  total = 1
  for numbers in args:
    total *= numbers  
  return total  
  
numbers = 4, 5, 6, 7, 78
multiplication = multiply(*numbers)
print(multiplication)

def odd_even(number):
  multiple_of_two = number % 2 == 0

  if multiple_of_two:
    return f'{number} is even'
  return f'{number} is odd'

print(odd_even(2))
print(odd_even(13))
print(odd_even(40))
print(odd_even(32))
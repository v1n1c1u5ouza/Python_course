""" 
  inform if this number is even or odd. If the user does not enter a number
  integer, inform that it is not an integer.
"""
entry = input('Enter a number: ')

try:
  entry_int = int(entry)
  even_odd = entry_int % 2 == 0
  even_odd_text = 'even' 
  
  if even_odd:
    even_odd_text = 'par'
    
  print(f'The number {entry_int} is {even_odd_text}')
except:
  print('You have not entered an integer')
"""
  Write a program that asks the user for the time and, based on the time
  described, display the appropriate salutation. Ex.
  Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
entry =  input("Enter the time in whole numbers: ")

try:
  hour = int(entry)
  
  if hour >= 0 and  hour <= 11:
    print('Goog Morning')
  elif hour >= 12 and hour <= 17:
    print('Good afternon')
  elif hour >= 18 and hour <= 23:
    print('Good night')
  else:
    print('Unknown hour')
except:
  print('Please enter only whole numbers')
  
"""
  Write a program that asks for the user's first name. If the name has 4 letters or
  minus write "Your name is short"; if it has between 5 and 6 letters, write
  "Your name is normal"; greater than 6 write "Your name is too long".
"""
name = input('Enter your name: ')
name_len = len(name)

if name_len > 1:
  if  name_len <= 4:
    print('Your name is short')
  elif name_len >= 5 and name_len <= 6:
    print('Your name is normal')
  else:
    print('Your name is to big')
else: 
  print('Enter more letters')


name = input('Enter your name: ')
age = input('Enter your age: ')

if name and age:
  print(f'Your name is {name}')
  print(f'Your name inverted is {name[::-1]}')
  
  if ' ' in name:
    print('Your name has spaces')
  else:
    pass
    print('Your name has NO spaces')
    
  print(f'Your name has {len(name)} letters')
  print(f'The first letter of your name is {name[0]}')
  print(f'The last letter of your name is {name[-1]}') 
else:
  print('Sorry, you let the fields empty')
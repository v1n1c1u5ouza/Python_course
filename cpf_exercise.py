"""
  Calculation of the second digit of the CPF
  CPF: 746.824.890-70
  Collect the sum of the first 9 digits of the CPF,
  PLUS THE FIRST DIGIT,
  multiplying each of the values ​​by a
  countdown starting from 11

  Ex.: 746.824.890-70 (7468248907)
    11 10 9 8 7 6 5 4 3 2
  * 7 4 6 8 2 4 8 9 0 7 <-- FIRST DIGIT
    77 40 54 64 14 24 40 36 0 14

  Sum all results:
  77+40+54+64+14+24+40+36+0+14 = 363
  Multiply the previous result by 10
  363 * 10 = 3630
  Get the remainder by dividing the previous count by 11
  3630% 11 = 0
  If the previous result is greater than 9:
      result is 0
  contrary to this:
      result is the account value

  The second digit of the CPF is 0
"""

import re
import sys

entry = input('CPF [746.824.890-70]: ')
user_cpf = re.sub(r'[^0-9]', '', entry )

sequential_entry = entry = entry[0] * len(entry)

if sequential_entry:
  print('You sent sequential data')
  sys.exit()
  
nine_digits = user_cpf[:9]
regressive_counter_1 = 10

digit_result_1 = 0
for digit in nine_digits:
  digit_result_1 += int(digit) * regressive_counter_1
  regressive_counter_1 -= 1 
digit_1 = (digit_result_1 * 10) % 11 
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)
regressive_counter_2 = 11

digit_result_2 = 0
for digit in ten_digits:
  digit_result_2 += int(digit) * regressive_counter_2
  regressive_counter_2 -= 1 
digit_2 = (digit_result_2 * 10) % 11 
digit_2 = digit_2 if digit_2 <= 9 else 0
 
calc_cpf = f'{nine_digits}{digit_1}{digit_2}'

if user_cpf == calc_cpf:
    print(f'{user_cpf} é válido')
else:
    print('CPF inválido')
              

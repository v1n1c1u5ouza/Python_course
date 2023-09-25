try:
  a = 18
  b = 0
  # print('line 1'[10000])
  c = a / b
  print('line 2')
except ZeroDivisionError as err:
  print(err.__class__.__name__)
  print(err)
except NameError:
  print('b is not defined')
except (TypeError, IndexError) as err:
  print('TypeError + IndexError')
  print('MSG:', err)
  print('Nome:', err.__class__.__name__)
except Exception:
  print('ERRO DESCONHECIDO.')
  
print('CONTINUAR')
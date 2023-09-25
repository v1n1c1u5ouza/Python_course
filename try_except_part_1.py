try:
  a = 18
  b = 0
  print('line 1'[10000])
  c = a / b
  print('line 2')
except ZeroDivisionError:
  print('divided by zero.')
except NameError:
  print('b is not defined')
except (TypeError, IndexError):
  print('TypeError + IndexError')
except Exception:
  print('ERRO DESCONHECIDO.')
  
print('CONTINUAR')
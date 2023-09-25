try:
  print('Open file')
  # 8/0
except ZeroDivisionError as err:
  print(err.__class__.__name__)
  print(err)
  print('divided by zero.')
except IndexError:
  print('IndexError')
except (NameError, ImportError):
  print('NameError + ImportError')
else:
    print('No errors')
finally:
  print('Close file')
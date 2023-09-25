def do_not_accept_zero(d):
  if d == 0:
    raise ZeroDivisionError('You are trying to divide by zero')
  return True

def must_be_int_or_float(n):
  type_n = type(n)
  if not isinstance(n, (float, int)):
    raise TypeError(
      f'"{n}" must be int or float. '
      f'"{type_n.__name__}" sended.'
    )
  return True

def divide(n, d):
  must_be_int_or_float(n)
  must_be_int_or_float(d)
  do_not_accept_zero(d)
  return n / d

print(divide(8, '0'))
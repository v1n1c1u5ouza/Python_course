def create_multiplier(multiplier):
  def multiply(number):
    return number * multiplier
  return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(2))
print(triple(2))
print(quadruple(2))
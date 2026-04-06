def add(a, b):
  #Баг: вместо сложения стоит вычитание
  return a - b
  
def subtract(a, b):
  return a - b
  
def multiply(a, b):
    #Баг: вместо умножения стоит сложение
  return a + b
  
def divide(a,b):
  if b == 0:
    raise ValueError("На ноль делить нельзя!")
  return a / b

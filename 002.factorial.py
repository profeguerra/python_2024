def factorial(numero):
  if numero == 0:
    return 1
  elif numero < 0:
    return "No se puede calcular el factorial de un número negativo"
  elif numero == 1:
    return 1
  else:
    return numero * factorial(numero - 1)


print(factorial(3))
import re

#special sequences 

mensajes = [
  "A RegEx, or Regular Expression, is a sequence of characters 100 that forms a search pattern.",
  "Returns a match if the specified characters are at the beginning of the string",
  "Dictionaries are used to store data values in key:value pairs."
]


'''
#patron = "\AA"
patron = "\AReturns"

resultado = re.findall(patron, mensaje_2)

print(resultado)

if resultado:
  print('found!')
else:
  print('not found!')
'''


#patron = r"\bval"
#patron = '\s'
patron = '\S'

for index, mensaje in enumerate(mensajes):
  resultado = re.findall(patron, mensaje)
  if resultado:
    print(f'Patron {patron}, encontrado en el indice {index} : mensaje {mensaje}')
import re

mensaje = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern."

palabra = "sequence"


if palabra in mensaje:
  print('found!')
else: 
  print('not found!')


#email = "xcvkp@example.com"

email = '@guerra!.'

if '@' in email and '.' in email:
  print('Correo valido')



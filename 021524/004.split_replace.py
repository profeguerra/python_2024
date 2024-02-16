import re

mensaje = 'Create and print a dictionary'

'''
patron = '\s'

#resultado = re.split(patron, mensaje)

resultado = re.split(patron, mensaje, 2)

print(resultado)
'''


patron = '\s'
replace = '-'

vecescambio = 2

#resultado = re.sub(patron, replace, mensaje, vecescambio)
resultado = re.sub(patron, replace, mensaje)

print(resultado)



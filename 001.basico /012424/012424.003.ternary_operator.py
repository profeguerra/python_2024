'''
003 Ternary Operator
rule: condicion_if_true if condicion else condicion_if_false
'''

amigo = False

if amigo:
    'mensaje permitido'
else:
    "no me puede enviar mensaje"



'Mensaje permitido' if amigo else "no me puedes enviar mensaje"

#print('Mensaje permitido' if amigo else "no me puedes enviar mensaje")


vacaciones = False

status_vacaciones = "puedes salir de vaciones" if vacaciones else "no puedes salir de vacaciones"

#print(status_vacaciones)


edad = 2 

status_edad = 'vas en primaria' if edad > 5 else 'vas en kinder'

print(status_edad)

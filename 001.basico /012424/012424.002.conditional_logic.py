'''
002. Condicionales
- if
- else
- else if = elif

- and, ambas tiene que ser True
- or, al menos 1 de las 2 debe de ser True, entra 

'''

is_old = False
licencia_conducir = False

if is_old or licencia_conducir:
    print('Puedes conducir')
else:
    print('No puedes conducir')

'''
#if is_old == True:
if is_old:
    print('Tienes edad para manejar')
elif licencia_conducir:
    print('Puedes conducir')
else:
    print('No tienes edad para manejar')

if is_old and licencia_conducir:
    print('Eres un buen ciudadano con licencia y la edad suficiente')
else:
    print('Lo siento, no puedes conducir')


edad = int(input('Cual es tu edad? '))

if edad >= 18 and edad <= 70: 
    print('Eres mayor de edad y puedes manejar bien')
elif edad > 71:
    print('Aun que eres mayor de edad, dudamos que puedas manejar')
else:
    print('Que estas haciendo?')

'''

user = input('user: ')
password = input('password: ')

'''
if user == 'luis' and password == '123':
    print('Acceso a la aplicacion')
else:
    print('Usuario o contrase#a incorrectos')
'''

if user == 'luis' and password == '123':
    print('Eres usuario normal')
elif user == 'maggie' and password == '432':
    print('eres usuario administrador')
elif user == 'octopus' and password == '678':
    print('eres usuario super administrador')
elif user == 'paulina' and password == '456':
    print('eres usuario super super administrador')
else:
    print('no eres un usuario registrado')


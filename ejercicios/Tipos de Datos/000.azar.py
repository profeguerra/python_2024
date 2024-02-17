import random


jugadores = ['Paulina', 'Ibra', 'Maggie', 'Ulises', 'Luis']
ejercicios = [1,2,3,4,5,6,7,8,9,10,11,12]
ganadores = []

'''
for index, ejercicio in enumerate(ejercicios):
    ganador = random.choice(jugadores)
    ganadores.append(ganador)

for index, ganador in enumerate(ganadores):
    print(index + 1, ganador)
'''


for index in range(1, 13):
    ganador = random.choice(jugadores)
    ganadores.append(ganador)
#print(ganadores)
'''
for index, ganador in enumerate(ganadores):
    ganadores = index + 1, ganador
    print(ganadores)
    archivo = open('lista_gandores.txt', 'a')
    archivo.write(str(ganadores))
'''

ganadores_final = ''

for index, ganador in enumerate(ganadores):
    orden = index + 1
    ganadores_final = f'{orden}. {ganador}\n'
    print(ganadores_final)
    archivo = open('lista_gandores_001.txt', 'a')
    archivo.write(ganadores_final)


archivo.close()
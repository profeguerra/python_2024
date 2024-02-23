'''
fizz buzz 
multiplos del 3 = fizz 
multiplos del 5 = buzz 
multiplos del 3 y 5 = fizz buzz
'''

lista_numeros = []
index = 0
for numero in range(1, 101):
    #print(numero)

    lista_numeros.append(numero)
    #print(lista_numeros)
    if numero % 3 == 0 and numero % 5 == 0:
        lista_numeros[index] = 'fizz buzz'
        
    elif numero % 3 == 0:
        lista_numeros[index] = 'fizz'
        
    elif numero % 5 == 0:
        lista_numeros[index] = 'buzz'

    index += 1

print(lista_numeros)

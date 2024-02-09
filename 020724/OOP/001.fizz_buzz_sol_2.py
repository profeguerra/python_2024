'''
fizz buzz 
multiplos del 3 = fizz 
multiplos del 5 = buzz 
multiplos del 3 y 5 = fizz buzz
'''

lista_numeros = []

for numero in range(1, 21):

    #print(lista_numeros)
    if numero % 3 == 0 and numero % 5 == 0:
       lista_numeros.append('fizz buzz')
        
    elif numero % 3 == 0:
       lista_numeros.append('fizz')
        
    elif numero % 5 == 0:
        lista_numeros.append('buzz')

    else:
        lista_numeros.append(numero)

print(lista_numeros)


'''
fizz buzz 
multiplos del 3 = fizz 
multiplos del 5 = buzz 
multiplos del 3 y 5 = fizz buzz
'''

lista_numeros = []

for numero in range(1, 101):
    lista_numeros.append(numero)

#print(lista_numeros)
    
for index, value in enumerate(lista_numeros):
    #print(f'index: {index} - value: {value}')

    if value % 3 == 0 and value % 5 == 0:
       lista_numeros[index] = 'fizz buzz'
        
    elif value % 3 == 0:
       lista_numeros[index] = 'fizz'
        
    elif value % 5 == 0:
        lista_numeros[index] = 'buzz'
        
print(lista_numeros)
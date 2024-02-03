'''
001 Walrus Operator 
" := "
- permite asignar una variale y al mismo tiempo devolver el valor 
- entro en la 3.8 
'''

name = 'Luis'
print(name)
print(type(name))

print(second_name := "Ricardo")
print(type(second_name))

'''
lista = []
entra = input("Escribe algo: ")
while entra != 'fin':
    lista.append(entra)
    entra = input('Escribe algo: ')
print(lista)
'''

lista = []
while(entra := input('escribe algo: ')) != 'fin':
    lista.append(entra)
print(lista)
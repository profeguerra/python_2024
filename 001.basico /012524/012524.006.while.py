'''
006 while
'''

'''
iterador = 0

while iterador < 5: 
    print(iterador)
    iterador += 1
    #iterador = iterador + 1
print('Done!')
'''

option = 0 
while option != '3':
    print('1, revisa tu saldo')
    print('2, retirar')
    print('3, salir')
    option = input('optione: ')
    if option == '3':
        input('dentro del if')
        option = '3'
        #break
    
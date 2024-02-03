''''
003 Global keyword
- nos permite llamar a una variable global dentro de una funcion donde la variable es local
'''


#constante
USD = 20.34

#global 
total = 100



def print_total():
    #local
    total = 1
    total += 1
    print(total)

#print_total() #2


def print_total_2():
    #llamado a la variable global 
    global total
    print(type(total))
    total += 1
    print(type(total))
    print(total)

print_total_2() #
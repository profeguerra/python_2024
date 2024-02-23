
def suma_cinco(numero):
    try:
        if numero:
            return int(numero) + 5
        else:
            return 'Por favor ingresa un numero'
    except ValueError as error: 
        return error



print(suma_cinco('')) 

#assert(suma_cinco(1) == 6) #ok
#assert(suma_cinco(1) == 1) #ok


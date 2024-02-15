def suma_return(numero_uno, numero_dos):
    return numero_uno + numero_dos

#print(suma_return(1,1))


def suma_yield(numero_uno, numero_dos):
    yield numero_uno + numero_dos

#print(suma_yield(2, 2)) 

ejemplo_yield = suma_yield(2, 2)

print(next(ejemplo_yield))


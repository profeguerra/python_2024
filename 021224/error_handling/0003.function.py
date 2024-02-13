def suma_dos(numero_uno, numero_dos):
    try: 
        return numero_uno + numero_dos
    except(TypeError, ZeroDivisionError) as error:
        return error


print(suma_dos(1, 1))
print(suma_dos(1, '1'))

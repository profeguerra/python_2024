''''
003 Lambda 
- son funciones anonimas
- puede tomar cualquier numero de argumentos, pero solo tiene una expresion
- el resultado se guarda en una variable
- la funcion lambda puede recibir 1 o 2, o cualquier numero de parametros (argumentos)
'''

def suma(numero):
    return numero + 1

print(f"Funcion normal: {suma(1)}")

resultado = lambda numero: numero + 1

print(f"Funcion anonima: {resultado(1)}")


resultado_dos = lambda numero_uno, numero_dos: numero_uno + numero_dos + 1

print(resultado_dos(2, 2))

''''
004 docstrings
- Nos permiten generar documentación de una función 
'''

def convertir_porcentaje(valor):
    ''''
    Info: esta función, convierte un entero en decimal, en prorción de un porcentaje (100)
    '''
    resultado = valor / 100
    return resultado

#print(convertir_porcentaje())

#help(convertir_porcentaje(1))
print(convertir_porcentaje.__doc__)
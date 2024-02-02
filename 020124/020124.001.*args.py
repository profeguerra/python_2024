'''
001 args se usa para funciones 
- regla: 
    1. argumentos/parametros, 
    2. *args
    3. default params
    4. **kwargs

- *args, no ayuda a pasar cualquier numero de argumentos a una funcion, estos se convierten en una tupla. 

'''

def suma(valor_uno, valor_dos, valor_tres=10):
    print(valor_uno + valor_dos + valor_tres)

#suma(8,8,9)

#*args "*""

def suma_calificaciones(*args):
    #los argumentos los convierte en una tupla 
    print(args)
    print(type(args))
    resultado = 0
    for valores in args:
        resultado += valores
    return resultado

#print(suma_calificaciones(8,10,9,6,8,7,10))


def promedio_tiempo_vuelta(auto1, auto2, auto3, auto4):
    promedio = (auto1 + auto2 + auto3, auto4) / 4 
    return promedio

#print(promedio_tiempo_vuelta(1.13, 1.35, 1.26))



def promedio_tiempo_vuelta_optimizada(*args):
    print(args)
    print(len(args))
    print(type(args))
    
    promedio = 0
    for tiempos in args:
        promedio += tiempos
    return promedio / len(args)

print(promedio_tiempo_vuelta_optimizada(2.20, 2.13, 2.22, 3.34, 2.56, 1.59))
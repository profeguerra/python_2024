'''
001 Dictionaries 
- sirven para guardar multiples valores o datos
- para declarar un diccionario, usamos las llaves "{ }"
- se compone de un 'key' y un 'value', siempre en pares
- "permite" duplicados, pero solo muestra el ultimo 
'''

car_dict = {
    'key': 'value',    #1
    'marca': 'VW',     #2
    'modelo': 'Jetta', #3
    'anio': 2023,      #4
    'anio': 2024,      #5
    'version': 'sport',#6
    'direccion_fabrica': ['calle conocida', 'colonia desconocida'],#7 
    'vendido': True    #8
}

#print(car_dict)
'''
print(car_dict['direccion_fabrica'][0])
print(car_dict['direccion_fabrica'][1])

print(car_dict['marca'])
print(car_dict['modelo'])
print(car_dict['anio'])
'''

#print(len(car_dict))


student_dict = dict(nombre = 'Maggie', edad = 12, matricula = '123455JDF')

print(type(student_dict))
print(student_dict['edad'])
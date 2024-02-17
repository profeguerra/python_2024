'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''

horas_trabajadas = int(input('Horas trabajadas: '))
costo_horas = int(input('costo horas: '))

resultado = horas_trabajadas * costo_horas
print('Monto a pagar: $', resultado, '.00')
'''
002 Return
- todas a funciones regresan algo
- no todas imprimen algo
- una funciones debe de hacer una cosa, bien
- al aplicar el "return" sales de la funcion
'''

consumo = float(input("Consumo: "))
propina = float(input("%Propina: "))

def convertir_porcentaje(valor):
    ''''
    Info: esta función, convierte un entero en decimal, en prorción de un porcentaje (100)
    '''
    resultado = valor / 100
    return resultado

porcentaje_propina = convertir_porcentaje(propina)

def calcular_monto_propina(monto_pagar, porcentaje_propina):
    ''''
    Info: esta función, calcula la propina en proporción a un monto
    '''
    resultado = monto_pagar * porcentaje_propina
    return resultado

propina_calculada = calcular_monto_propina(consumo, porcentaje_propina)

def redondeo_dos_decimales(valor, decimales=2):
    ''''
    Info: esta función, toma un valor y hace un redondeo predefinido a dos decimales
    '''
    return round(valor, 2)

monto_pagar = redondeo_dos_decimales(consumo)
monto_propina = redondeo_dos_decimales(propina_calculada)

def calcular_total(monto_pagar, monto_propina):
    ''''
    Info: esta función, calcula el monto total, sumando el monto de consumo más el monto de la propina y regresa un mensaje predeterminado
    '''
    total = monto_pagar + monto_propina
    return f"Monto consumido ${monto_pagar}, monto propina ${monto_propina}, monto total ${total}"

print(calcular_total(monto_pagar, monto_propina))


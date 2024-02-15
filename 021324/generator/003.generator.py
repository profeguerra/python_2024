def numeros_naturales():
    numero = 0
    while numero < 10:
        yield numero
        numero += 1

numeros_naturales_variable = numeros_naturales()

print(next(numeros_naturales_variable)) #0
print(next(numeros_naturales_variable)) #1
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable)) #5
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable))
print(next(numeros_naturales_variable)) #9


for number in numeros_naturales():
    print(number)

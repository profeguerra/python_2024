

while True:
    try: 
        age = int(input('age? '))
        10 / age
        print(age)
    except TypeError:
        print('error 001 - please enter a number')
    except ValueError:
        print('error 002 - seguramente, ingresaste una letra, por favor ingresa un numero')
    except ZeroDivisionError:
        print('error 003 - ingresaste un 0 y la edad debe ser mayor a 0, por favor intentalo nuevamente')
    else:
        print('Datos guardados correctamente, gracias')
        break

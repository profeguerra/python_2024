''''
001 Funcitons
- blockes de codigo que se pueden reutilizar y llamar
- pueden o no, recibir parametros (argumentos)
'''

'''

def say_hello():
    print("Hello")

#Llamando la funcion
say_hello()


def say_hello_user(user_name):
    print(f"Hello {user_name}")


say_hello_user("Octopus")
say_hello_user("Maggie")
say_hello_user("Paulina")
say_hello_user("Ibra")
say_hello_user("Luis")
'''

def wellcome_user(user_name):
    return f"Hello {user_name}"

print(wellcome_user('Paulina'))

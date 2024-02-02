''''
01. Default params (parametros) and keywordsargs (argumentos)
- 
'''

''''
def say_hello_user_phone(user_name, user_phone):
    print(f'Hello user {user_name}, you can call me {user_phone}')


#possitional
#say_hello_user_phone('Luis', '3311223344')
#say_hello_user_phone('33123344', 'Luis')

#keyword arguments, es decirle explicitamente,que valor de cada argumento no tiene una posicion, ya que sera asignado 
say_hello_user_phone(user_name='Luis', user_phone='3311223344')
say_hello_user_phone(user_phone='3311223344', user_name='Luis')
'''
#default parameters
def say_hello_user_phone(user_name='Pauline', user_phone='3311223344'):
    print(f'Hello user {user_name}, you can call me {user_phone}')

say_hello_user_phone()
say_hello_user_phone("Ibra", '5511223344')
say_hello_user_phone('5511223344', "Ibra")
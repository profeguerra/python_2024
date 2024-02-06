''' 
Class: Humano 
- Attributes: 
    - Lugar de nacimiento
    - fecha nacimiento
    - color: 
    - raza: 
    

- Method: 
    - camina 
    - corre
    - habla
    - duerme
    - come
    - siente
    
'''

#nombre clase en Mayuscula
class Persona:

    #atributos
    first_name = ''
    last_name = ''
    born_year = ''

    #metodos 
    def say_hello(self):
        return 'Hello'
    
    def say_bye(self):
        return 'Bye'

#instanciar = crear
persona_uno = Persona()
persona_uno.first_name = "Luis"
persona_uno.last_name = "Guerra"
persona_uno.born_year = 1966

#invoke = llamar a un metodo
print(persona_uno.first_name)
print(persona_uno.last_name)
print(persona_uno.born_year)
print(persona_uno.say_hello())
print(persona_uno.say_bye())


persona_dos = Persona()
persona_dos.first_name = 'Maggie'
print(persona_dos.first_name)

persona_tres = Persona()
persona_tres.first_name = 'Ibra'
print(persona_tres.first_name)

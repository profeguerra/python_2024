'''
002 supper()
- el metodo super() hace referencia a la clase padre 
- Humano (padre) = super() para hacer herencia 
'''

class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad 

    def mueve(self):
        return 'se mueve'


class Perro(Animal):

    def __init__(self, especie, edad, nombre):
        #super().__init__(especie, edad)
        Animal.__init__(self, especie, edad)
        self.nombre = nombre

    def mueve(self):
        return super().mueve()


perro_uno = Perro('Pitbull', '6', 'Kaiser')
print(perro_uno.especie)
print(perro_uno.edad)
print(perro_uno.nombre)
print(perro_uno.mueve())

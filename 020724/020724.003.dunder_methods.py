''' 
003 dunder methos / magic methods 
- se caracterizan por iniciar con doble guion bajo en cada metodo
- un ejemplo es __init__ que nos ayuda a inicializar lo atributos de un metodo 
- la mayoria o casi todos los magic methods se pueden modificar 
'''


class Laptop:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


    def __str__(self):
        return f"Hello, I am a {self.brand} model {self.model} color {self.color}, this is cool, right?"
    

laptop_one = Laptop('Mac', 'Macbook Pro', 'Silver')
print(laptop_one.__str__())
print(str(laptop_one))




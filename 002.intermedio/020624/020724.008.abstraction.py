class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def drive(self):
        pass

#vehicle_one = Vehicle
#print(vehicle_one)

class Car(Vehicle):

    def drive(self):
        return f"Conduciendo en la ciudad {self.brand} del modelo {self.model}"
    

class Truck(Vehicle):

    def drive(self):
        return f"Condunciendo en el campo, {self.brand} modelo {self.model}"


class Moto(Vehicle):

    def drive(self):
        return f"Conduciendo mi {self.brand} modelo {self.model} en la pista"
    

car_one = Car("VW", "Jetta")
print(car_one.drive)
print(car_one.drive())

truck_one = Truck("Ford", "Lobo")
print(truck_one.drive())

mot_one = Moto("Ducati", "848 evo")
print(mot_one.drive())
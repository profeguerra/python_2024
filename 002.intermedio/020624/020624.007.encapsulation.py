class Car:

    def __init__(self, brand, model, price) -> None:
        self.__brand = brand
        self.__model = model
        self.__price = price

    def get_price(self):
        return self.__price
    

hyundai = Car('Hyundai', 'X', 200)

print(hyundai.__price)
print(hyundai.get_price())

print(dir(hyundai))
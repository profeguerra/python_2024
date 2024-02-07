class Man:

    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year

    def walk(self):
        return 'Walking'
    

class Woman:

    def __init__(self, born_country):
        self.born_country = born_country

    def run(self):
        return 'running'



class Son(Man, Woman):
    pass


son_one = Son('Juan', 2000)
print(son_one)
print(son_one.run)
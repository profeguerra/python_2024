class Human:

    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year

    def walk(self):
        return 'Walking'
    
################################################################################3

class Man(Human):
    
    def __init__(self, name, born_year, last_name):
        super().__init__(name, born_year)
        self.last_name = last_name


    #polimorfismo = polimorphisim 
    def walk(self):
        #return super().walk()
        return 'walking like a man'
    

man_one = Man('Marco', 1945, 'Corleone')

print(man_one.walk())



class Woman(Human):

    def __init__(self, name, born_year, born_place):
        #super().__init__(name, born_year)
        Human.__init__(self, name, born_year)
        self.born_place = born_place

woman_one = Woman('Maria', 2014, 'Mexico')


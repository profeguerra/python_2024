class Cellphone: 


    #__init__ es un method "magic" = constructor = en un metodo que obliga a inicializar attributos 
    def __init__(self, brand, model, color):        
        self.brand = brand
        self.model = model
        self.color = color
        

    def start_on(self):
        return 'Device is on'
    
    def power_off(self):
        return 'Turning off device'
    

#instance 
iphone = Cellphone('Apple', 'iPhone 15', 'Negro')
print(iphone.brand)


samsung = Cellphone('Samsung', 'Galaxy', 'Silver')
#samsung = Cellphone('Samsung')
#invoke method 
print(samsung.start_on())
'''
002. Static methods (classmethods / decorators)
- los metodos estaticos pueden ser accesibles sin instanciar un objeto, solo llamando la clase
'''

class Student:

    def __init__(self, id, full_name):
        self.id = id 
        self.full_name = full_name

    def speak(self):
        return 'Speaking'
    
    def walk(self):
        return 'Walking'
    
    @staticmethod
    def run():
        return 'Running'
    
    @classmethod
    def sleep(cls, starting, end):
        return f'Sleeping from {starting} to {end}'
    
    
    
ulises = Student(100, 'Ulises Arteaga')
#print(ulises.speak())
print(f'instanciando un objeto: {ulises.run()}')

print(f'sin instanciar un objeto: {Student.run()}')

print(Student.sleep("10:00", "7:00"))




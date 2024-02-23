class Game:

    def __init__(self, id, name):
        self.id = id
        self.name = name

game_one = Game(1, 'Fizz Buzz')
#print(game_one.id)
#print(game_one.name)

class Dynamic_list:

    def __init__(self, start_number, end_number, list_number):
        self.start_number = start_number
        self.end_number = end_number
        self.list_number = list_number

    def create_list(self):
        for value in range(self.start_number, self.end_number):
            self.list_number.append(value)
        return self.list_number
    
 


my_list = []
dynamic_list = Dynamic_list(1, 21, my_list)
list_created = dynamic_list.create_list()
#print(list_created)
#print(type(list_created))

############################################################################################

class Evaluate:

    def __init__(self, list_number, counter):
        self.list_number = list_number
        self.counter = counter

    def list_validation(self):
        return type(self.list_number)
    
    def fizz_buzz(self):
        for number in self.list_number:
            if number % 3 == 0 and number % 5 == 0:
                self.counter += 1
                return self.list_number[self.counter] 
    def fizz(self):
        for number in self.list_number:
            if number % 3 == 0:
                print(self.list_number[self.counter], 'fizz')
                self.list_number[self.counter] = 'fizz'
                self.counter += 1
    
    '''
    def fizz(self):
        for number in self.list_number:
            if number % 3 :
                self.list_number[self.index] = 'fizz'
                print('fizz')
    
    def buzz(self):
        for number in self.list_number:
            if number % 5 == 0:
                self.list_number[self.index] = 'buzz'
                print('buzz')
    '''

#list_number = [13, 14, 15, 16]
#evaluate_one = Evaluate(list_number)

'''
print(evaluate_one.fizz_buzz())
print(evaluate_one.fizz())
print(evaluate_one.buzz())
'''




evaluate_one = Evaluate(list_created, 0)
print(evaluate_one.fizz_buzz())
print(evaluate_one.list_validation())
print(evaluate_one.fizz())
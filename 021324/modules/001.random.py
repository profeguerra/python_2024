import random


random_numer_float = random.random()
print(round(random_numer_float, 4))

random_numer_int = random.randint(1, 20)
print(random_numer_int)


friends = ['Hugo', 'Maria', 'Ulises', 'Maggie']
random_choice = random.choices(friends)
print(random_choice)
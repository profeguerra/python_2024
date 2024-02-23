import random

list_numbers = [1,2,3,4,5,6,7,8,9,0]
list_letters_lowercase = ['a','b','c','d','e']
list_letters_upppercase = []
list_chars = ['!', '@', '#']


'''
user_numbers = int(input('How many numbers: '))

for iteration in range(0, user_numbers):
    password_number = ''
    random_int = random.choice(list_numbers)
    password_number += str(random_int)

print(password_number)
'''

user_letters = int(input('How many letters: '))


for iteration in range(0, user_letters):
    password_letter = ''
    print(iteration)
    password_letter += random.choice(list_letters_lowercase)
print(password_letter)
import random

list_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
list_numbers = ['1','2','3','4','5','6','7','8','9','0']
list_symbols = ['!','@','#','$','%','ˆ','&','*','(',')','-','+']


number_letter = int(input('Chars? '))
number_numbers = int(input('Numbers? '))
number_symbols = int(input('Symbols? '))

def random_character(number_characters, list_elements):
    password_character = ''
    for character in range(1, number_characters + 1):
        password_character += random.choice(list_elements)
        #print(password_character)
    return(password_character)

random_letters = random_character(number_letter, list_letters)
#print(random_letters)
random_numbers = random_character(number_numbers, list_numbers)
#print(random_numbers)
random_symbols = random_character(number_symbols, list_symbols)
#print(random_symbols)

def concatenate_characters(random_letters, random_numbers, random_symbols):
    result = str(random_letters) + str(random_numbers) + str(random_symbols)
    return result
    
final_password = concatenate_characters(random_letters, random_numbers, random_symbols)

print(final_password)

def randomize_password(final_password):

    #print(type(final_password))
    final_password = ''.join(random.sample(final_password, len(final_password)))
    print(final_password)

randomize_password(final_password)

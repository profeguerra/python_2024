'''
005. Operadores logicos
# >, <, ==, !=, <=, >=, and, or, not
'''

'''
print(5 > 3)       #T
print(3 < 5)       #T
print(10 != 9)     #T
print(not(1 == 1)) #F
print(not(False))  #T

'''

have_iphone = False
have_macbook = False

if have_iphone and have_macbook:
    print('Apple fan!')
elif have_iphone and not have_macbook:
    print('Eres un fan de Windows')
elif not have_iphone:
    print('eres usuario de android')

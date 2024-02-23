'''
002 Iterables

collection: list, tuples, set, dict, son iterables 
'''
user_dict = {
    'name': 'Luis',
    'can_drive': True,
    'phone': 3312724816
}


'''

for item in user_dict:
    print(item)

for item in user_dict.items():
    print(item)

for item in user_dict.values():
    print(item)

for item in user_dict.keys():
    print(item)
'''

for item in user_dict.items():
    key, values = item
    print(item)


for key, values in user_dict.items():
    #print(key, values)
    print(key, ":", values)
'''
002 scope (alcan)
'''

#global scope
name = 'Luis'

#print(name)

def print_name(name="Python"):
    #local scope
    return name

print(print_name())
print(print_name(name))
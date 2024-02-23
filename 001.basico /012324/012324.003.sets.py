'''
003 Sets
- los sets se forman usando { }
- los sets NO son indexables 
- no permite duplicados
- permite, int, str, boolean, float, es decir, guarda cualquier tipo de variable
'''
my_set = {1,2,3,4,5}
my_other_set = {5,6,7,8,9, 'Set', False, 6.67}
#print(type(my_set))

#print(my_set)
print(my_other_set)
#print(my_set.difference(my_other_set))

my_other_set.discard(5)
#print(my_other_set)
my_other_set.discard(8)
#print(my_other_set)



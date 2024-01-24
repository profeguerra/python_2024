'''
002. Tuplas 
- las tuplas se usan con () 
- las tuplas permiten int, string, boolean, permite cualquier tipo de valor
- las tuplas permiten duplicados
- las tuplas son indexadas e inician en el [0]
- no permite modificar o asignar
'''

my_tuple = (1,2,3,4,5,6, '7', False, 1)
#print(my_tuple)
#print(len(my_tuple))
#print(my_tuple[0])
#my_tuple[2] = 30

my_new_tuple = my_tuple[1:3]

#print(my_new_tuple)
#print(5 in my_new_tuple)
#print(2 in my_new_tuple)

print(my_tuple.count(2))
print(my_tuple.count(1))

maggie_tuple = (
    [1,2,3],
    [4,5,6], 
)

print(maggie_tuple)


other_tuple = 1, 2, 3 , 4

print(type(other_tuple))
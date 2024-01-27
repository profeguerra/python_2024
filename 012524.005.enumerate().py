'''
005 enumerate
'''

'''
course = "Learning Python"

for index, character in enumerate(course):
    #print(index, character)
    if character == 'n':
        #print(index, character)
        print(f'Index of {character} in possition {index}')
'''
        

my_courses = ['Python', 'Scrum', 'Docker', 'NGINX']

for index, course in enumerate(my_courses):
    print(index, '-', course)


find = int(input('find: '))
for index, course in enumerate(my_courses):    
    if find == index:
        print(f'Course {course} found in index {index}')
        break

find = input('course: ')
for index, course in enumerate(my_courses):    
    if find == course:
        print(f'Course {course} found in index {index}')
        break

'''
    de la lista de cursos 
    pregunte index / nombre del curso
    depliegue el nombre del curso y el indice
'''
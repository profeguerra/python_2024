'''
004. and / or
- debe ser en minusculas
- and, ambos deben ser verdaderos = True
- or, almenos uno debe de ser verdadero = True
'''

is_employee = False
is_developer = False

employee_state = 'eres de IT' if is_employee or is_developer else 'eres administrativo'

print(employee_state)
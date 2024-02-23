'''
Ejercicio 7
Escribir un programa que pregunte el 
- correo electrónico del usuario en la consola y 
- muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) 
- pero con dominio ceu.es.

'''


email = input('email: ')

print(email)

email_elements = email.split('@')
print(email_elements)

#0
#1 = dominio, pop, append = ceu.es





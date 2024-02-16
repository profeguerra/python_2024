
#file = open("test.txt", "r")
#print(file.read())

#si el archivo esta en una ubicacion diferente, necesitamos darle la ruta completa 
file = open("/home/linux/Development/Python/course_2401/python_2024/021424/test.txt")
print(file.read())

import os 

#print(os.uname())

#add text 

'''
#'a' = append 
el parametro 'a' genera el archivo si no existe
si el archivo existe, se agrega al final
'''
#file = open("paulina.txt", "a")
#file.write("Now the file has more content!")

#'r' nos permite leer el archivo 
#file = open("paulina.txt", "r")
#print(file.read())

#'w' sirve para escribir en el archivo y sobre escribe todo el contenido 
# si el archivo no existe, lo crea 
#file = open("paulina.txt", "w")
#file.write("Woops! I have deleted the content!")

#'r' nos permite leer el archivo 
#file = open("paulina.txt", "r")
#print(file.read())

#CRUD = Create, Read, Update, Delete = ABC: Altas, Bajas y Cambios 

if os.path.exists("paulina.txt"):
  print('File found!')
  input('press enter to continue... ')
  os.remove("paulina.txt")


#file.close()

#es una buena practica , cerrar el archivo al final 
file.close()
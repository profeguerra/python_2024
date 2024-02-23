'''
002 String Indexes
nos permite indexar cada uno de los caracteres de mi cadena de texto
'''

name = "Ricardo"
       #0123456

index_name = '''
print(name)
print(name[0]) #R 
print(name[1]) #i
print(name[2]) #i
print(name[3]) #i
print(name[4]) #i
print(name[5]) #i
print(name[6]) #i
'''

#[start : stop : stepover]
#print(name[0:2]) #Ri
#print(name[2:6]) #Ri

        #01345678910
phone = "3312724816"
        #        -2-1
#print(phone[0:10:2])
#print(phone[:3])
#print(phone[::2])
print(phone[-1])
print(phone[-2])
print(phone[::-1])

'''
006 is vs ==

js 1 == '1' T, 1 === '1' F
'''

print('------ == -------------')
print(True == 1)  #T
print('' == 1)    #F
print(False == 0) #T
print([] == [])   #T
print(10.0 == 10) #T 
print([1,2,3] == [1,2,3]) #T



print('------ is -------------')
print(True is 1)  #F
print('' is 1)    #F
print(False == 0) #F
print([] is [])   #F
print(10.0 is 10) #F
print([1,2,3] is [1,2,3]) #F
print(10 is 10)  #T

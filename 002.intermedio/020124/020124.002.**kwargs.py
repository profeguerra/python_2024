'''

'''

def estudiante(**kwargs):
    #dictionario 
    #print(kwargs)
    #print(type(kwargs))
    #print(len(kwargs))
    
    query = "SELECT * FROM estudiantes WHERE "

    iterative = 0
    for key, values in kwargs.items():
        query += f"{key}='{values}' "        
        query += ' AND '
        iterative += 1
        if iterative == len(kwargs):
            break
    
        print(query)


estudiante(first_name='Luis', last_name='Guerra', middle_name='Ricardo')
#estudiante(first_name='Luis')


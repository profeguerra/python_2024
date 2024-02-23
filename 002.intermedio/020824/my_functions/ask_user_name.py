def ask_user_name(question, variable_name):
    '''
    Info: esta funcion recibe una pregunta que se mostrara en la termina y el valor que ingresa el usuario, se guardara e una variable 
    \n
    input data: 
        - str: question
        - str: variable_name
    \n
    output data: 
        - str: variable_name
    '''
    variable_name = input(question)
    return variable_name
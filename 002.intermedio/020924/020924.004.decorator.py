user1 = {
    "name": "Maggie",
    "valid": True
}

user2 = {
    "name": "Ricardo",
    "valid": False
}

def authenticated(function):

    def wrapper(*args, **kwargs):

        if args[0]['valid']:

            return function(*args, **kwargs)
        
        else:
            return print('invalid user')
        
    return wrapper


@authenticated
def message_friend(user):
    print('Message has been sent to your friend')


@authenticated
def regresa(user):
    print("regresa")

#message_friend(user1)
#message_friend(user2)


regresa(user1)
regresa(user2)
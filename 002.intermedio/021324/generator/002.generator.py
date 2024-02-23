def generator():
    n = 1
    yield n

    n += 1
    yield n
    
    n += 1
    yield n

generator_example = generator()

print(next(generator_example)) #1
print(next(generator_example)) #2
print(next(generator_example)) #3


for iterador in generator():
    print(iterador)
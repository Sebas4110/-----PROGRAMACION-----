import random
def act_1():  
    def funcion1():
        for i in range (10):
            yield i
        
    def funcion2():
        for r in range (10,20):
            yield r
    def generador():
        yield from funcion1()
        yield from funcion2()

    hola = generador()

    print(next(hola))
    print(next(hola))
    print(next(hola))

    print("el resto de los datos")
    for num in hola:
        print(num)

def act_2():
    def ale():
        for i in range(7):
            yield random.randrange(1,100)
    siete = ale()
    for n in siete:
        print(n)
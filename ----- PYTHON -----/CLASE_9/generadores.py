def generador():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


# g = generador()
# print(next(g))
# print(next(g))
# print(next(g))

def generepares(limite):
    num = 1
    miLista = []
    while num <= limite:
        miLista.append(num*2)
    return miLista

print(generepares(10))
#generador
def generepares2(limite):
    num = 1
    while num <= limite:
        yield num*2
        num += 1
    return num

x = generepares2(10)
#===== EJEMPLO 1 =====
def factorial(n):
    if n < 0:
        return "No existe factorial para negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(20))

# esta funcion esta lgiada a un "if", el cual l oque hace es revisar si el numero es 0
# si no lo es, si el numero es 1 dar un resultado de "1"
# si tampoco es, se hace una multiplicacion del numero - 1 (l que seria factorial)
# se sigue asi hasta que que llegue a 1 y se retorna multiplicando, para dar el resultado final

# ===== EJEMPLO 2 =====

def agrupar_por_longitud(lista_palabras):
    resultado = {}
    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud not in resultado:
            resultado[longitud] = []
        resultado[longitud].append(palabra)
    return resultado

print(agrupar_por_longitud("externocleidomastoideo"))
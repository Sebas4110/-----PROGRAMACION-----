#===== Funciones =====
def saludo():
    print("hola mundo")

saludo()
saludo()

def saludo2(nombre):
    print(f"hola, {nombre}")

saludo2("juan")
saludo2("sebas")
saludo2("ciro")

def suma(a,b):
    print(a + b)

suma(2,3)

# ===== funcion retorno =====

def resta(a, b):
    return a - b

resultado1 = resta(10,5)
resultado2 = resta(100,45)
print("la resta 1 es: {}, la respuesta 2 es {}". format(resultado1, resultado2))
# format(), es lo mismo que interpolar (f), ya es como prefiera utilizarlo

#retorno de valores vacio

def operacion(a=None,b=None):
    if a is None:
        return " no se puede realizar la operación"
    elif b is None:
        return " no se puede realizar la operación"
    else:
        return a + b
    
print(operacion(2))

# el "None" es para decir que esta vacio y no se trabe el sistema ( se puede reemplazar)

#ejercicio de conversion de grados

def conversion(temp, unidad):
    if unidad == "K" or unidad == "k":
        c = temp + 273.15
    elif unidad == "F" or unidad == "f":
        c = (temp - 32) * 5/9
    else:
        print("debes seleccionar una unidad que sea F o K")
        return
    return f"{c}°"

unidad: str = str(input(" dime que unidad quieres convertir, farenheit o kelvin(f o k)?: "))
temp: float = float(input("dime la temperatura a convertir: "))
print("la temperatura en celsius es:", conversion(temp, unidad))

# guardar una tupla
def guardar(cad, v = 2, *algomas):
    print(cad *  v)
    for i in algomas:
        print(i)
        
guardar("hola", 3, "adios", "chao", "perro")

# la tupla (*) es un tipo de listado que sirve en las funciones para guardar datos
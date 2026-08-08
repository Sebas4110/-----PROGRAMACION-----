# ficheros read, write, append x: existencia
ruta = "prueba.txt"

def x():
# existencia del fichero
    with open(ruta, mode = "x", encoding="utf-8") as fichero:
        fichero.write("Hello world")
    
def w():
# sobre-escritura
    with open(ruta, mode = "w", encoding="utf-8") as fichero:
        fichero.write("Hello world")


def a():
# append
    with open(ruta, mode = "a", encoding="utf-8") as fichero:
        fichero.write(" ,esta cosa funciona")

#x()
#w()
#a()

def guardar_nota(nombre, nota):
    # de notas
    with open("notas_clases.txt", "a", encoding="utf-8") as fichero:
        fichero.write(f"{nombre} = {nota}\n")
    print(f"se ha guardado la nota de {nombre}")

while True:
    nombre: str = str(input("ingresa el nombre del estudiante: "))
    if nombre == "fin":
        break
    nota: float = float(input("ingresa la nota del estudiante: "))
    guardar_nota(nombre, nota)

    # "\n" significa saltar linea
    # "r" significa leer un texto
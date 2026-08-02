import random
#===es sugerible tener el "import" afuera de la función===


#range es una lista de numeros enteros en suceción aritmetica

# for i in range(10):
#     print(2**i)
def ejemplo():

    for x in range(20):
        if x % 2 == 0:
            print(x)
        else:
            print("impar")

    # iterar un lista
    x = [1,2,3,4,5,6]
    for num in x:
        print(num)

    print("comienzo")
    for i in [1,1,1]:
        print("hola",end=(" "))
    print()

    #[end =("")] es para colocar lo que quieras que siga despues de imprimir algo, ejm: si colocas (" ") va a copiar el texto seguido.

    #función len(): devuelve la longitud de una cadena

    print(len(x))# devuelve 6 a la longitud
    x = [0,3,1,2]
    for num in range(len(x)):
        print(x[num])


    #ejemplo texto y operaciones
    print("comienzo ejm 1")
    for i in [3,4,5]:
        print(f"hola, ahora i vale {i} y la potencia a la dos es: {i ** 2}")
    print("final")

    print("comienzo ejm 2")
    for i in ["alba", "benito", 27]:
        print(f"hola, ahora i vale {i}")
    print("final")

    print("comienzo ejm 3")
    for i in [0,1,2,3,4]:
        print(f"{i} * {i} = {i ** 2}")
    print("final")

    print("comienzo ejm 4")
    for i in"AMIGO":
        print(f"DAME UNA {i}")
    print("AMIGO!!")
def ejercicio():
    #ejercicio dado con funcion random
    print("comienzo")
   # sacaste_cinco = False
    cuenta_cinco = 0
    for i in range(3):
        dado = random.randrange(1,7)
        print(f"tirada {i + 1}: {dado}")
        if dado == 5:
                cuenta_cinco += 1
                #sacaste_cinco = True
    # if sacaste_cinco:
    #     print("ha sacado al menos un 5")
    # else:
    #     print("no ha sadado ningún 5")
    print(f"le ha salido en total {cuenta_cinco} cinco/s")
    print("FIN")

# (randrange)  es el rango que se le pone a un random
#ejemplo()
def ejercicio2():
    tabla_desde = 1
    tabla_hasta = 12

    for factor1 in range(tabla_desde, tabla_hasta + 1):
        print(F"    tabla de multiplicar del {factor1}: ")
        for two in range(tabla_desde, tabla_hasta+ 1):
            print(f"{factor1} X {two} = {factor1 * two}")
    print("FINAL")
ejercicio2()

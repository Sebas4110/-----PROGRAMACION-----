#actividad 1

def panaderia():
    pan: int = int(input("cuantos panes de ayer vendieron hoy?"))
    precio_p=  ((3.49* (1-0.6))*pan)
    ganancia = (precio_p)
    print(f"la ganacia total fue de {ganancia} euros")

#actividad 2

def repeticion():
    palabra: str = str(input("dime una palabra y la repetiré 10 veces: "))
    for i in range(10):
        print(f"{i + 1}. {palabra}")

#actividad 3

def edad():
    edad: int = int(input("dime tu edad: "))
    for i in range(1, edad + 1):
        print(f"{i}")
        i += 1
    print("estos son todos los años que ha cumplido")
    #en el range, el primer numero es el inicio, el segundo el final y el tercero los pasos

#actividad 4

def piramide():
    num: int = int(input("dime un numero: "))
    for i in range(1, num + 1):
        print("*" * i)
    
#actividad 5

def par():
    for i in range(0, 100 + 1, 2):
        print(i)

#actividad 6

def contraseña():
    contra = "contraseña"
    while True:
        contra2: str = str(input("ingrese contraseña: "))
        if contra == contra2:
            print("contraseña correcta, que tenga un buen dia!")
            break
        else:
            print("contraseña incorrecta, intentelo de nuevo")

#actividad 7

def diferencias():
    print("presione 0 para salir")
    while True:
        num: int = int(input("ingrese un numero: "))
        if num == 0:
            print("Que tenga un buen dia")
            break
        elif num > 0:
            print("es positivo")
        else:
            print("es negativo")
        
#actividad 8

def palabra1():
    palabra: str = str(input("ingrese una palabra:"))
    if len(palabra) < 7:
        print(f"es una palabra corta, ya que tiene {len(palabra)} letras")
    else:
        print(f"es una palabra larga, ya que tiene {len(palabra)} letras")

#actividad 9

def despegue():
    print("INICIANDO DESPEGUE/presiona enter para continuar")
    for i in range(10, -1, -1):
        input()
        print(i, end = "")
    print("\n\nDESPEGANDO!!")

#actividad 10

def tesoro():
    cofre = ["piedra", "arena", "moneda", "tesoro", "cangrejo"]
    intento = 1
    print("hay un tesoro, dime donde se ubica el tesoro (del 0 al 4): ")
    while True:
        tesoro: int = int(input(""))
        if tesoro == 3:
            print(f"acertaste, solo te tomo {intento} intento/s")
            break
        else:
            print(f"incorrecto, en esa posición estaba el/la {cofre[tesoro]}")
            intento += 1

#actividad 11

def invertido1():
    invertido = ""
    palabra: str = str(input("ingresa una palabra: "))
    for i in range(len(palabra)-1, -1, -1):
        invertido += palabra[i]
    print(invertido)

#actividad 12

def grito1():
    grito = "A"
    tope: int = int(input("cual es el tope que quieres del grito: "))
    for i in range(1, tope + 1, 1):
        print(grito)
        grito += "A"

op = int(input("ejercicio a ejecutar: "))
match op:
    case 1:
        panaderia()
    case 2:
        repeticion()
    case 3:
        edad()
    case 4:
        piramide()
    case 5:
        par()
    case 6:
        contraseña()
    case 7:
        diferencias()
    case 8:
        palabra1()
    case 9:
        despegue()
    case 10:
        tesoro()
    case 11:
        invertido1()
    case 12:
        grito1()
    case _:
        print("no es posible ejecutarlo")
    
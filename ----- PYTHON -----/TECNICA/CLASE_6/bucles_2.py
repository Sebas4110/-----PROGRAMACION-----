#===============bucle while Do=============


def ejemplo1():
    i = 1
    while i <= 3:
        print(i)
        i+=1
    print("programa terminado") 


def ejemplo2():
    dia = 0
    semana = ['lunes','martes','miercoles','jueves','viernes']
    print(semana[2])
    while dia <= 4:
        print(semana[dia])
        dia+=1

def ejemplo3():
    numero = int(input("escriba un numero positivo: "))
    while numero > 0:
        print("ha escrito un numero postivo")
        numero = int(input("escriba un numero positivo: "))
    print("gracias por su cooperación de numeros positivos", numero)


def ejemplo4():
    palabra_secreta = "python"
    contador = 0
    while True:
        palabra = input("ingrese la palabra secreta :").lower()
        contador = contador + 1
        if palabra == palabra_secreta:
            print("palabra secreta correcta")
            break
        if palabra != palabra_secreta and contador > 7:
            print("ya no tiene mas intentos, de malas")
            break

def ejemplo5():
    while True:
        letra = input("dijite la letra 'a' ")
        if letra != 'a':
            break
        print("")




op = int(input("bucles while Do: "))
match op:
    case 1:
        ejemplo1()
    case 2:
        ejemplo2()
    case 3:
        ejemplo3()
    case 4:
        ejemplo4()
    case 5:
        ejemplo5()

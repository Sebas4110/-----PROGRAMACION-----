# es una caja de errores, donde podemos controlar el flujo de ejeccuion de nuestro programa

def resta(a,b):
    return a-b

def suma(a,b):
    return a+b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
       print("no es posible dividir entre 0")
       return "operacion no valida"
    
def ejemplo1():
    while True:

        op1 = (int(input("ingrese el primer numero: ")))
        op2= (int(input("ingrese el segundo numero: ")))

        operacion = input("ingrese la operacion a realizar (suma , resta multiplicacion, division): ")

        match operacion:
            case "suma":
                print(suma(op1,op2))
            case "resta":
                print(resta(op1,op2))
            case "multiplicacion":
                print(multiplicacion(op1,op2))
            case "division":
                print(division(op1,op2))

#ejemplo1()

def ejemplo2():
    def evaluaEdad(edad):
        #excepcion agregada
        if edad < 0:
            raise TypeError("la edad no puede ser negativa")
        #raise es una excepcion pero corto
        if edad < 20:
            return "eres joven"
        elif edad < 65:
            return "eres maduro"
        elif edad < 100:
            return "cuidate"
        else:
            raise ValueError("edad no valida")
            

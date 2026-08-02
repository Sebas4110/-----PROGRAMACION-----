import math


# ===== FUNCIONES =====
# ----- detalles -----
def cierre():
    print("------------------------------------\n")


def error(mensaje: str):
    print(f"[ERROR]: {mensaje}")


def resultado(operacion, mensaje: str = "El resultado es", añadido: str = ""):
    print(f"{mensaje}: {operacion:.2f}{añadido}")


# ----- solicitudes -----
def pedirnumero():
    num1: float = float(input("Ingresar primer numero: "))
    num2: float = float(input("Ingresar segundo numero: "))
    return num1, num2


def pedirangulo():
    angulo: int = int(input("Ingresar ángulo a calcular (grados): "))
    return angulo


def medida():
    medi: str = input("¿Que medida quieres trabajar (m, km, cm, etc)?: ")
    return medi


# --- operadores Aritmetica ---
def suma(num1: int | float, num2: int | float):
    try:
        return num1 + num2
    except (ValueError, TypeError):
        print("[ERROR]: Todos deben ser valores numéricos")
        return None


def resta(num1: int | float, num2: int | float):
    try:
        return num1 - num2
    except (ValueError, TypeError):
        print("[ERROR]: Todos deben ser valores numéricos")
        return None


def multi(num1: int | float, num2: int | float):
    try:
        return num1 * num2
    except (ValueError, TypeError):
        print("[ERROR]: Todos deben ser valores numéricos")
        return None


def dividir(num1: int | float, num2: int | float, entero: bool = False):
    try:
        num1, num2 = float(num1), float(num2)  # forzamos la comprobacion del TypeError
        if entero:
            return num1 // num2
        return num1 / num2
    except (ValueError, TypeError):
        print("[ERROR]: Todos deben ser valores numéricos")
    except ZeroDivisionError:
        print("[ERROR]: El denominador debe ser diferente a cero (0)")
    return None


def potencia(base: int | float, indice: int | float = 2):
    try:
        return base**indice
    except TypeError:
        print("[ERROR]: Todos deben ser valores númericos")
    except ZeroDivisionError:
        print("[ERROR]: No es posible elevar cero aun exponente negativo")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")
        return None


def raiz(base: int | float, indice: int | float = 2):
    try:
        base, indice = float(base), float(
            indice
        )  # forzamos la comprobacion del TypeError
        if base < 0 and indice % 2 == 0:  # lanza el error y lo atrapamos abajo
            raise ValueError(
                "[ERROR]: El resultado es un número inmaginario, no es posible base negativa y indice par"
            )
        else:
            return base ** (1 / indice)
    except TypeError:
        print("[ERROR]: Todos deben ser valores númericos")
    except ZeroDivisionError:
        print("[ERROR]: El indice de la raiz no puede ser cero")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")
        return None


def factorial(tope: int):
    resultado: int = 1
    try:
        if tope < 0:
            raise ValueError("[ERROR]: La base debe ser igual o mayor a cero")
        tope = int(tope)
        if tope == 0:
            return resultado
        for x in range(2, tope + 1):
            resultado *= x
        return resultado
    except (ValueError, TypeError):
        print("[ERROR]: Debe ser un número entero")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")


# --- operadores Trigonometria ---
def tan(angulo):
    rad = math.radians(angulo)
    tan = math.tan(rad)
    return tan


def sin(angulo):
    rad = math.radians(angulo)
    sin = math.sin(rad)
    return sin


def cos(angulo):
    rad = math.radians(angulo)
    cos = math.cos(rad)
    return cos


# --- operadores geometria ---
def acirculo(r):
    return math.pi * r**2


def acuadrado(l):
    return l**2


def arectangulo(b, a):
    return b * a


def atrapecio(a, b, h):
    return (a + b) * h / 2


def atriangulo(a, b):
    return a * b / 2


# --- soluciones geometria ---
def circulo1():
    print("¿Cual es el radio del circulo?")
    radio: float = float(input(": "))
    return acirculo(radio)


def cuadrado1():
    print("¿Cual es el lado del cuadrado?")
    lado: float = float(input(": "))
    return acuadrado(lado)


def rectangulo1():
    print("cual es la base y la altura del rectangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    return arectangulo(base, altura)


def trapecio1():
    print("Cual es la base mayor,menor y altura del trapecio?")
    baseM: float = float(input("Base mayor: "))
    basem: float = float(input("Base menor: "))
    altura: float = float(input("Altura:"))
    return atrapecio(baseM, basem, altura)


def triangulo1():
    print("cual es la base y la altura del triangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    return atriangulo(base, altura)


# ====== LOBBY ======
print("==========BIENVENIDO==========")
while True:
    print("¿En que área desea trabajar?")
    print(
        "1) Aritmetica \n2) Trigonometria \n3) Geometria(no disponible) \n4) Logaritmos(no disponible)"
    )
    print("-- Presione 0 para salir")
    tipo: int = int(input(": "))
    match tipo:
        # --- Aritmetica ---
        case 1:
            print("\n¿Qué operación desea hacer?")
            print(
                "1) Suma \n2) Resta \n3) Multiplicación \n4) División \n5) Potencia \n6) Raíz \n7) Factorial"
            )
            opera: int = int(input(": "))
            match opera:
                case 1:  # suma
                    num1, num2 = pedirnumero()
                    resultado(suma(num1, num2))
                    cierre()
                case 2:  # resta
                    num1, num2 = pedirnumero()
                    resultado(resta(num1, num2))
                    cierre()
                case 3:  # multiplicacion
                    num1, num2 = pedirnumero()
                    resultado(multi(num1, num2))
                    cierre()

                case 4:  # Division
                    num1, num2 = pedirnumero()
                    resultado(dividir(num1, num2))
                    cierre()

                case 5:  # Potencia
                    num1, num2 = pedirnumero()
                    resultado(potencia(num1, num2))
                    cierre()

                case 6:  # Raiz
                    num1, num2 = pedirnumero()
                    resultado(raiz(num1, num2))
                    cierre()

                case 7:  # Factorial
                    try:
                        num_fact = int(input("Ingresar numero: "))
                        total = factorial(num_fact)
                        if total is not None:
                            resultado(total)
                    except ValueError:
                        error("Debe ser un número entero")
                    cierre()

                case _:
                    error("Operación no valida")
                    cierre()

        # --- Trigonometria ---
        case 2:
            print("\n¿Qué operación desea hacer?")
            print("1) Seno \n2) Coseno \n3) Tangente")
            opera: int = int(input(": "))
            match opera:
                case 1:
                    angulo = pedirangulo()
                    resultado(sin(angulo), "El seno del angulo es", "°")
                    cierre()
                case 2:
                    angulo = pedirangulo()
                    resultado(cos(angulo), "El coseno del angulo es", "°")
                    cierre()
                case 3:
                    angulo = pedirangulo()
                    resultado(tan(angulo), "La tangente del angulo es", "°")
                    cierre()
                case _:
                    error("Operación no valida")
                    cierre()

        # --- Geometria ---
        case 3:
            print("\nLa figura a calcular es 3D o 2D?")
            print("(Escribir '2d' o '3d')")
            forma: str = input(": ")
            print("¿Qué operación desea hacer?")
            match forma.upper():
                case "2D":
                    print("1) Área \n2) Perimetro")
                    opera: int = int(input(": "))
                    match opera:
                        # areas
                        case 1:
                            print("Escribe la figura que deseas calcular el área:")
                            print(
                                "1) Circulo \n2) Cuadrado \n3) Rectangulo \n4) Trapecio \n5) Triangulo"
                            )
                            figura: int = int(input(": "))
                            match figura:
                                case 1:
                                    resultado(circulo1(), "El área es", medida())
                                    cierre()
                                case 2:
                                    resultado(cuadrado1(), "El área es", medida())
                                    cierre()
                                case 3:
                                    resultado(rectangulo1(), "El área es", medida())
                                    cierre()
                                case 4:
                                    resultado(trapecio1(), "El área es", medida())
                                    cierre()
                                case 5:
                                    resultado(triangulo1(), "El área es", medida())
                                    cierre()
                                case _:
                                    error("Operación no valida")
                                    cierre()
                        # perimetros
                        case 2:
                            print("Escribe la figura que deseas calcular el perimetro:")
                            print(
                                "1) Circulo \n2) Cuadrado \n3) Rectangulo \n4) Trapecio \n5) Triangulo"
                            )
                            figura: int = int(input(": "))
                case _:
                    error("Dimensión inválida")
                    cierre()
        case 0:
            print("==========HASTA PRONTO==========")
            break
        case _:
            error("Área inexistente")
            cierre()


# falta:
# 1) Colocar tries (trigonometria, geometria, logaritmos)
# 2) hacer la geometria (volumen)
# 3) hacer conversion de decimales a fraccion y viceversa
# 4) suma, resta, multiplicacion y division de fracciones
# 5) usar el "for" e "in" para la calculador
# 6) Colocar textos de colores
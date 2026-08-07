"""
# operadores_logicos
# + - * / % **
# jerarquia de operaciones
# (), potencia y raiz, multi. y division, suma y resta
print(34*45+3/(34**7))

#operadores relacionales
# > < == >= <= !=
print(12>3)
print(12<3)
print(12==3)
print(12>=3)
print(12!=3)

#operadores logicos
# and y or
resultado1 = 4>3 and 10>20
print(resultado1)

resultado1 = 4>30 or 10>2
print(resultado1)

resultado1 = not 3>4 
print(resultado1)

año = 2026
mes = "febrero"
resultado1 = año == 2020 or mes == "febrero"
print(resultado1)
"""
#entrada de datos
nombre = input("ingresa nombre:")
print("Hola, ingresa al salon",nombre)

genero = input("ingresa M para Macho o F para femenina")

edad = int(input("ingresa edad:"))

if(edad>18 and genero == "F"):
    print(F"usted {nombre} puede ingresar al bar")
    print(f"su edad es{edad} y es de genero {genero}")
else:
    print("usted no puede ingresar al bar")


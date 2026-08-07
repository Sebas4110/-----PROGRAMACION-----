print("escribe tres numeros enteros distintos")
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"el orden es: {num1}, {num2}, {num3}")
elif num1 < num2 and num1 > num3 and num2 > num3:
    print(f"el orden es: {num2}, {num1}, {num3}")
elif num1 < num2 and num1 < num3 and num2 > num3:
    print(f"el orden es: {num2}, {num3}, {num1}")
elif num1 < num2 and num1 < num3 and num2 < num3:
    print(f"el orden es: {num3}, {num2}, {num1}")
elif num1 > num2 and num1 > num3 and num2 < num3:
    print(f"el orden es: {num1}, {num3}, {num2}")
elif num1 > num2 and num1 < num3 and num2 < num3:
    print(f"el orden es: {num3}, {num1}, {num2}")
else:
    print("no es posible colocar numeros iguales")
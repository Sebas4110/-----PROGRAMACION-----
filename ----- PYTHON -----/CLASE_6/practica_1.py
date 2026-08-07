total: int = 0
print("presiona '0' si desea finalizar")
while True:
    num = int(input("ingrese un numero mayor a 100 y menor que 200 (no valido 0 ni menores): "))
    if num == 0:
        print("programa finalizado")
        break
    elif not(num in range(100, 201)):
        print("no es valido ese numero")
    elif num < 0:
        print("tiene que ser mayor a cero")
    else:
        total += num
        print(f"la suma hasta ahora es {total}")
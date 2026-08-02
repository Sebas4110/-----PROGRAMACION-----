print("por valores mayores a $300, recibe un descuento del 20%")
valor = int(input("ingrese el precio de su articulo(s): "))
if valor > 300:
    descu = valor * 0.2
    print(f"con descuento del 20% te quedaria en {descu} ")
else:
    print("ese articulo no tiene descuento, por tanto se queda con el precio original")

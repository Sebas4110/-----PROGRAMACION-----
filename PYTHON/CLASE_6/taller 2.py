top : int = int(input("dame un numero y te sumare todos los numeros impares: "))
suma: int = 0
for num in range(1, top+1, 2):
    print(num)
    suma += num

print(f"la suma total de los numeros impares hasta {top} es {suma}")

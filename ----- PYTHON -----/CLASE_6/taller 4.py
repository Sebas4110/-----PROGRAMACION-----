num: int = int(input("dame un numero y te dire si es primo o no: "))
primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break

if primo and num > 1:
    print("es primo")
else:
    print("no es primo")
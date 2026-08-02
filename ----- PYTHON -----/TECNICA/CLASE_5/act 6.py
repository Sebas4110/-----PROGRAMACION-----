num = int(input("dime un numero del 0 al 99 999: "))

if num < 10:
    print(f"el numero {num} contiene 1 cifra")
elif num < 100:
    print(f"el numero {num} contiene 2 cifras")
elif num < 1000:
    print(f"el numero {num} contiene 3 cifras")
elif num < 10000:
    print(f"el numero {num} contiene 4 cifras")
elif num < 100000:
    print(f"el numero {num} contiene 5 cifras")

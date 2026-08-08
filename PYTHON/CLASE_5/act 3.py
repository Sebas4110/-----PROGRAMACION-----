horas = int(input("escribe el numero de horas que quieres convertir: "))
semanas = horas // 168
horas_r = horas % 168

if horas_r == 0:
    print(f"son en total {semanas} semanas")
else:
    dia = horas_r // 24
    rest = horas_r % 24
    if rest == 0:
        print(f"son en total {semanas} semanas y {dia} dias")
    else:
        print(f"son en total {semanas} semanas, {dia} dias y {rest} horas")
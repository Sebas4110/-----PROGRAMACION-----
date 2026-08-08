#40 o menos = 16 por hora
#mas de 40 horas = 16 por hora y 20 por hora extra

horas = int(input("dime las horas trabajadas en la semana(5 dias): "))
if horas > 120:
    print("que tan curioso que tabajaste mas de lo que se puede en una semana")
elif horas <= 40:
    pago = horas * 16
    print(f"ganaste en la semana ${pago}")
elif horas > 40:
    pago = (40*16)+(horas - 40)*20
    print(f"ganaste en la semana ${pago}")

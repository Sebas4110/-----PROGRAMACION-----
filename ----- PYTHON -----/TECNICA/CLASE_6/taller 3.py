# saldo en la cuenta = 1000
saldo_inicial: float = 1000
saldo: float = saldo_inicial
while True:
    print("=====Menú=====")
    print("1. Consultar saldo, 2. Retirar dinero, 3. Depositar dinero, 0. Salir")
    op: int = int(input("que deseas hacer?: "))
    match op:
        case 1:
            print(f"tu saldo actual es de {saldo}")
        case 2:
            rest: float = float(input("cuanto desea retirar?: "))
            if rest < saldo:
                saldo -= rest
            else:
                print("Saldo insuficiente")
        case 3:
            sum: float = float(input("cuanto desea depositar?: "))
            saldo += sum
        case 0:
            print("=====Sesión finalizada=====")
            break
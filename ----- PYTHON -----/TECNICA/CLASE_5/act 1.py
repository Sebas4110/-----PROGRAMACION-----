#num = int(input("ingrese un numero: "))
#if num % 2 == 0:
#    print(f"tu numero es {num} y es par")
#else:    
#    print(f"tu numero es {num} y es impar")


#nota = float(input("dime tu nota, para revisar si aprobaste o no: "))
#if nota < 10.5:
 #   print("ESTADO: REPROBADO")
#else:    
 #   print("ESTADO: APROBADO")

#CAJERO AUTOMATICO
#cualquier clave, saldo fijo de 500

clave: int = 9868

pin = int(input("Bienvenido, ingrese su clave de acceso: "))
if pin == clave:
    print("Bienvenido a su cajero preferido")
    dinero = int(input("cuanto desea retirar?: "))
    if dinero <= 500:
        print(f"retiro exitoso, acabo de retirar ${dinero} dolares")
        print("que tenga un feliz dia!")
    else: 
        print("saldo insuficiente, su saldo es de $500 dolares")
        print("reintentelo nuevamente más tarde")

else:
    print("clave incorrecta, reintentelo nuevamente más tarde")

    

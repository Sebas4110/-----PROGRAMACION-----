print("presiona '0' para salir")
while True:
    op = int(input("que poema quieres leer?(1 a 4): "))
    if op == 0:
        print("programa finalizado")
        break
    else:
        match op:
            case 1:
                print("La tierra estaba seca. No había ríos ni fuentes. Y brotó de tus ojos el agua, toda el agua.")
            case 2:
                print("Pequeño poema no me huyas no armes abismos entre mi alma y tú.")
            case 3:
                print("El magnífico sauce de la lluvia, caía ¡Oh la luna redonda sobre las ramas blancas!")
            case 4:
                print("De todos los monumentos construidos por el hombre mi favorito es el mar.")

def mixta():
    mixta =[18, "python", 3.14,True]
    print(mixta[2])
    #operaciones comunes
    #append: agregar
    mixta.append("naranja")
    print(mixta)
    #insertar por posicion
    mixta.insert(1, "java")
    print(mixta)
    #eliminar
    mixta.remove(3.14)
    print(mixta)
    #editar
    mixta[0] = "uno"
    print(mixta)
    #longitud
    print(len(mixta))
    

mixta()
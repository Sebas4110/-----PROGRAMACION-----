#crear un listado de su comida favorita y peliculas
def comida_fav():
    comida = []
    print("dime tu 5 alimentos favoritos")
    while len(comida) != 5:
        alim = str(input("ingresa tus alimentos favoritos: "))
        comida.append(alim)

    return comida

def peliculas_fav():
    peliculas = []
    print("dime ahora tus 5 peliculas favoritas")
    while len(peliculas) != 5:
        peli = str(input("ingresa tus peliculas favoritas: "))
        peliculas.append(peli)

    return peliculas


print(f"tus comidas favoritas son {comida_fav()}")
print(f"tus peliculas favoritas son {peliculas_fav()}")
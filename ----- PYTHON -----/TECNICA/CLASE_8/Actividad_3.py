ruta = r"D:\Phyton Sebas\TECNICA\Clase_8\biblioteca.txt"

#===== añadir poema =======
def añadir_poema():
    titulo: str = (input("ingresa el nombre del poema: "))
    autor: str = input("ingresa el nombre del autor: ")
    print("ahora escribe el poema separado por lineas (dando enter) y finaliza escribiendo 'fin' ")
    with open(ruta, "a", encoding="utf-8") as fichero:
        fichero.write(f"NOMBRE DEL POEMA: {titulo}\nNOMBRE DEL AUTOR: {autor}\n\n")
        while True:
            poema = str(input(""))
            if poema.lower() == "fin":
                fichero.write("FIN")
                print(f"se ha guardado el poema '{titulo}' del autor '{autor}'")
                fichero.write("\n------------------------------------\n")
                break
            fichero.write(f"{poema}\n")

#===== Lista titulos ======
def listar_titulos():
    print("POEMAS: ")
    with open(ruta,mode = "r", encoding="utf-8") as fichero:
        for linea in fichero:
            if linea.startswith("NOMBRE DEL POEMA: "):
                nombre: str = linea.replace("NOMBRE DEL POEMA: ","-")
                nombre = nombre.replace("\n","")
                print(nombre)

def autor():
    autor: str = input("escriba el autor que desea consultar: ")
    linea_anterior: str = ""
    with open(ruta,mode = "r", encoding="utf-8") as fichero:
        for linea in fichero:
            if linea.startswith(f"NOMBRE DEL AUTOR: {autor}"):
                obra: str = linea_anterior.replace("NOMBRE DEL POEMA: ","-")
                obra = obra.replace("\n","")
                print(obra)
            linea_anterior = linea

def contar_versos():
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    poemas = texto.split("-------------------------------")
    max_versos = 0
    poema_mas_largo = ""
    for poema in poemas:
        lineas = poema.strip().split("\n")        
        nombre = ""
        contando = False
        versos = 0
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("NOMBRE DEL POEMA:"):
                nombre = linea.replace("NOMBRE DEL POEMA:", "").strip()
            elif linea == "":
                contando = True
            elif linea == "FIN":
                break
            elif contando:
                versos += 1
        if nombre and versos > max_versos:
            max_versos = versos
            poema_mas_largo = nombre
    if poema_mas_largo:
        print(f"El poema más largo es '{poema_mas_largo}' con {max_versos} versos.")



#===== DIRECTORIO =====

print("que desea hacer? 1) añadir poema, 2) listar los titulos, 3) bucar por autor 4) verso mas largo")
op: int = int(input(""))
match op:
    case 1:
        añadir_poema()
    case 2:
        listar_titulos()
    case 3:
        autor()
    case 4:
        contar_versos()
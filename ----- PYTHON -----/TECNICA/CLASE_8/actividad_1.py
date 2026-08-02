# Nombre del archivo
archivo = "usuarios.txt"

# 1. Crear y escribir en el archivo (modo 'w' sobrescribe)
with open(archivo, "w", encoding="utf-8") as f:
    f.write("ID,Nombre,Edad\n")
    f.write("1,Ana,25\n")
    f.write("2,Carlos,30\n")

print("Archivo creado y datos iniciales guardados.\n")

# 2. Leer el archivo
print("Contenido inicial del archivo:")
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# 3. Agregar nuevos datos (modo 'a' = append)
with open(archivo, "a", encoding="utf-8") as f:
    f.write("3,Laura,28\n")

print("Nuevo usuario agregado.\n")

# 4. Leer nuevamente el archivo actualizado
print("Contenido actualizado del archivo:")
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
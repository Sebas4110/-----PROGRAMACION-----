import sqlite3

miConexion = sqlite3.connect("PrimerBase.db")

micursor = miConexion.cursor()

micursor.execute("CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER PRIMARY KEY, nombreProducto TEXT, precio INTEGER, seccion TEXT)")

# ====== Metodo comun para insertar ======

# micursor.execute("INSERT INTO producto VALUES (1,'camiseta', 15, 'deportes')")

# micursor.execute("INSERT INTO producto VALUES (2,'medias', 3, 'deportes')")

# micursor.execute("INSERT INTO producto VALUES (3,'pantaloneta', 10, 'deportes')")

# ====== Metodo complejo ( pero algo mas rapido) de insertar en tabla ======

productos = [
    (1,'camiseta', 15, 'deportes'),
    (2,'medias', 3, 'deportes'),
    (3,'pantaloneta', 10, 'deportes'),
    (4,'camisa', 20, 'casual'),
    (5,'zapatos',14, 'ejecutivos')
]

# ==== el fetchmany sirve para decir cuantos cosos voy a necesitar (si me hice entender) ====
micursor.executemany("INSERT OR IGNORE INTO producto VALUES (?,?,?,?)",productos)
# ==== actualizar ====
micursor.execute("UPDATE producto SET precio = 50 WHERE id_producto = 5")
micursor.execute("DELETE FROM producto WHERE id_producto = 5")

micursor.execute("SELECT * FROM producto")
# ==== el fetchall trae los datos del select y los vuelve tupla (cuadro de lista) ====
productos2 = micursor.fetchall()
#print(productos)

for producto1 in productos2:
    print("El id del producto es: ", producto1[0])
    print("El nombre del producto es: ", producto1[1])
    print("El precio del producto es: ", producto1[2])
    print("La sección del producto es: ", producto1[3])
    print("------------------//---------------")

# ==== CONSULTA DE CALCULO DE PRECIO ====
consulta = """
    SELECT
        MAX(precio) AS precio_maximo,
        MIN(precio) AS precio_minimo,
        COUNT(CASE WHEN precio % 2 == 0 THEN 1 END) AS cantidad_pares
    FROM producto
    
"""
micursor.execute(consulta)
resultado =micursor.fetchone()
print("-------------- REPORTE SQL -------------")
print("El precio mas alto es: ", resultado[0])
print("El precio mas bajo es: ", resultado[1])
print("Los numeros pares en los precios son: ", resultado[2])


# ==== el commit es necesario para guardar los cambios ====
miConexion.commit()
miConexion.close()

#i ===== IMPORTACIONES Y FUNCIONES =====
import sqlite3
import os
# ----- limpiar la pantalla -----
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")#nt = windows

# ----- Conectarse a la base de datos -----
conexion = sqlite3.connect("gamma.db")
cursor = conexion.cursor()

# ===== TABLAS =====
# ----- jugadores -----
cursor.execute("""CREATE TABLE IF NOT EXISTS jugadores (
    id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    vida INTEGER NOT NULL,
    dinero INTEGER NOT NULL DEFAULT 0,
    porcentaje REAL NOT NULL DEFAULT 0
    )
""")
# ----- inventario -----
cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
    id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    poder TEXT NOT NULL,
    uso TEXT NOT NULL,
    cantidad INTEGER DEFAULT 1,
    id_jugador INTEGER NOT NULL,
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_inventario)
)''')
# ----- habilidades -----
cursor.execute('''CREATE TABLE IF NOT EXISTS habilidades (
    id_habilidades INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    elemento TEXT NOT NULL,
    nivel INTEGER NOT NULL DEFAULT 1,
    desbloqueada INTEGER NOT NULL,
    elementos_compatibles TEXT NOT NULL,
    id_jugador INTEGER NOT NULL,
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
)''')

conexion.commit()

# ===== CHECKPOINT 1 =====
# ===== CRUD JUGADORES =====
# -----  C -----

def agregar_jugador():
    limpiar_pantalla()
    print("=== Agregar Jugador ===")

    nombre = str(input("Nombre del jugador: "))
    vida = int(input("Vida: "))
    dinero = int(input("Dinero: "))
    porcentaje = float(input("Porcentaje completado: "))

    cursor.execute("INSERT INTO jugadores (nombre, vida, dinero, porcentaje) VALUES (?, ?, ?, ?)",
        (nombre, vida, dinero, porcentaje))
    conexion.commit()
    print(f"\n========== Jugador '{nombre}' agregado correctamente ==========")
    input("\npresiona Enter para continuar...")

# -----  R -----

def listar_jugador():
    limpiar_pantalla()
    print("========== Lista De Jugadores ==========")

    cursor.execute("SELECT * FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} \nNombre: {jugador[1]} \nVida: {jugador[2]} \nDinero: {jugador[3]} \nPorcentaje: {jugador[4]}%")
            print("-"*40)
        input("presiona Enter para continuar...")
    else:
        print("========== No Hay Jugadores Existentes ==========")
        input("\npresiona Enter para continuar...")

# -----  U -----

def actualizar_jugador():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
            print("-"*40)
        id_jugador = int(input("¿Qué jugador desea actualizar?: "))
        limpiar_pantalla()
        cursor.execute("SELECT * FROM jugadores WHERE id_jugador = ?", (id_jugador,))
        jugadores = cursor.fetchall()
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]} | Dinero: {jugador[3]} | Porcentaje: {jugador[4]}")
            print("-"*40)
        print("========== Actualizar Jugador ==========")
        print("\n¿Qué deseas actualizar?")
        print("1. Nombre")
        print("2. Vida")
        print("3. Dinero")
        print("4. Porcentaje")
        op = int(input("\nElige una opción: "))
        match op:
            case 1:
                nuevo_valor = input("Nuevo nombre: ")
                cursor.execute("UPDATE jugadores SET nombre = ? WHERE id_jugador = ?", (nuevo_valor, id_jugador))
            case 2:
                nuevo_valor = int(input("Nueva vida: "))
                cursor.execute("UPDATE jugadores SET vida = ? WHERE id_jugador = ?", (nuevo_valor, id_jugador))
            case 3:
                nuevo_valor = int(input("Nuevo monto de dinero: "))
                cursor.execute("UPDATE jugadores SET dinero = ? WHERE id_jugador = ?", (nuevo_valor, id_jugador))
            case 4:
                nuevo_valor = float(input("Nuevo porcentaje alcanzado: "))
                cursor.execute("UPDATE jugadores SET porcentaje = ? WHERE id_jugador = ?", (nuevo_valor, id_jugador))
            case _:
                print("----- OPCIÓN NO VALIDA -----")
                print("----- INTENTELO NUEVAMENTE -----")
                input("\npresiona Enter para continuar...")
                return
        conexion.commit()
        print("\n========== Jugador Actualizado Correctamente ==========")
        input("\npresiona Enter para continuar...")
    else:
        print("\n========== No Existen Jugadores ========== ")
# -----  D -----

def eliminar_jugador():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
            print("-"*40)
        id_jugador = int(input("ID del jugador a eliminar: "))
        limpiar_pantalla()
        cursor.execute("SELECT nombre FROM jugadores WHERE id_jugador = ?", (id_jugador,))
        jugador = cursor.fetchone()
        print("========== Eliminar Jugador ==========")
        print(f"¿Estas seguro que quieres eliminar el jugador {jugador[0]} ? (si/no)")
        op = str(input(": ")).lower()
        if op == "si":
            cursor.execute("DELETE FROM inventario WHERE id_jugador = ?", (id_jugador,))
            cursor.execute("DELETE FROM habilidades WHERE id_jugador = ?", (id_jugador,))
            cursor.execute("DELETE FROM jugadores WHERE id_jugador = ?", (id_jugador,))
        else:
            print("========== Jugador No Eliminado ==========")
            input("\npresiona Enter para continuar...")
            return
        conexion.commit()
        print("========== Jugador, Sus Items Y Habilidades Eliminados Correctamente ==========")
        input("\npresiona Enter para continuar...")

# ===== CHECKPOINT 2 =====
# ===== INVENTARIO =====

# ----- C -----

def agregar_inventario():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    print("\n========== Jugador/es disponibles ==========")
    print("-"*40)
    for jugador in jugadores:
        print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
        print("-"*40)
    id_jugador = int(input("\nID del jugador elegido: "))
    limpiar_pantalla()
    print("========== Agregar Ítem al Inventario ==========")
    nombre = input("Nombre del ítem: ")
    poder = float(input("Poder del ítem (1 a 10): "))
    uso = input("¿Uso permanente o limitado? (permanente(p)/limitado(l)): ").lower()
    cantidad = int(input("cuanta cantidad de ese objeto tienes?: "))
    cursor.execute("INSERT INTO inventario (nombre, poder, uso, cantidad, id_jugador) VALUES (?, ?, ?, ?, ?)",
              (nombre, poder, uso, cantidad, id_jugador))
    conexion.commit()
    print(f"\n========== Ítem '{nombre}' Agregado Correctamente ==========")
    input("\npresiona Enter para continuar...")

# ===== R =====

def listar_inventario():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    print("\n========== Jugador/es disponibles ==========")
    print("-"*40)
    for jugador in jugadores:
        print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
        print("-"*40)
    print("¿Qué jugador desea revisar el inventario?: ")
    id_jugador = int(input(": "))
    limpiar_pantalla()
    print("========== Lista de Items ==========")
    cursor.execute("SELECT * FROM inventario WHERE id_jugador = ? ", (id_jugador,))
    items = cursor.fetchall()
    if items:
        print("-"*40)
        for item in items:
            print(f"Item #: {item[0]} \nNombre: {item[1]} \nPoder: {item[2]} \nUso: {item[3]} \nCantidad: {item[4]}")
            print("-"*40)
        input("presiona Enter para continuar...")
    else:
        print("\n========== No Hay Items Existentes ==========")
        input("\npresiona Enter para continuar...")

# ===== U =====

def actualizar_inventario():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
            print("-"*40)
        print("¿Qué jugador desea actualizar un item?: ")
        id_jugador = int(input(": "))
        limpiar_pantalla()
        cursor.execute("SELECT id_inventario, nombre, poder, uso, cantidad FROM inventario WHERE id_jugador = ? ", (id_jugador,))
        items = cursor.fetchall()
        if items:
            print("\n========== Items disponibles ==========")
            print("-"*40)
            for item in items:
                print(f"Item #: {item[0]} | Nombre: {item[1]} | Poder: {item[2]} | Uso: {item[3]} | Cantidad: {item[4]}")
            print("-"*40)
            print("========== Actualizar Item ==========")
            id_item = int(input("\n¿Qué item desea actualizar?: "))
            limpiar_pantalla()
            cursor.execute("SELECT id_inventario, nombre, poder, uso, cantidad FROM inventario WHERE id_inventario = ? ", (id_item,))
            items = cursor.fetchall()
            print("-"*40)
            for item in items:
                print(f"Item #: {item[0]} | Nombre: {item[1]} | Poder: {item[2]} | Uso: {item[3]} | Cantidad: {item[4]}")
            print("-"*40)
            print("\n¿Qué deseas actualizar?")
            print("1. Nombre")
            print("2. Poder")
            print("3. Uso")
            print("4. Cantidad")
            op = int(input("\nElige una opción: "))
            match op:
                case 1:
                    nuevo_valor = input("Nuevo nombre: ")
                    cursor.execute("UPDATE inventario SET nombre = ? WHERE id_inventario = ?", (nuevo_valor, id_item))
                case 2:
                    nuevo_valor = int(input("Nuevo poder: "))
                    cursor.execute("UPDATE inventario SET poder = ? WHERE id_inventario = ?", (nuevo_valor, id_item))
                case 3:
                    nuevo_valor = (input("Nuevo tipo de uso(limitado(l)/permantente(p)): "))
                    cursor.execute("UPDATE inventario SET uso = ? WHERE id_inventario = ?", (nuevo_valor, id_item))
                case 4:
                    nuevo_valor = float(input("Nueva cantidad: "))
                    cursor.execute("UPDATE inventario SET cantidad = ? WHERE id_inventario = ?", (nuevo_valor, id_item))
                case _:
                    print("----- OPCIÓN NO VALIDA -----")
                    print("----- INTENTELO NUEVAMENTE -----")
                    input("presiona Enter para continuar...")
                    return
            conexion.commit()
            print("\n========== Item Actualizado Correctamente ==========")
            input("\npresiona Enter para continuar...")
        else:
            print("\n========== No Existe Ningún Item ==========")
            input("\npresiona Enter para continuar...")
    else:
        print("\n========== No Existe Ningún Jugador ==========")
        input("\npresiona Enter para continuar...")

# ===== D =====

def eliminar_inventario():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
            print("-"*40)
        print("¿Qué jugador desea actualizar un item?: ")
        id_jugador = int(input(": "))
        limpiar_pantalla()
        cursor.execute("SELECT id_inventario, nombre, poder, uso, cantidad FROM inventario WHERE id_jugador = ? ", (id_jugador,))
        items = cursor.fetchall()
        if items:
            print("\n========== Item/s disponibles ==========")
            print("-"*40)
            for item in items:
                print(f"Item #: {item[0]} \nNombre: {item[1]} \nPoder: {item[2]} \nUso: {item[3]} \nCantidad: {item[4]}")
                print("-"*40)
            print("========== Eliminar Item ==========")
            id_item = int(input("¿Qué item desea eliminar?: "))
            limpiar_pantalla()
            cursor.execute("SELECT id_inventario, nombre, poder, uso, cantidad FROM inventario WHERE id_inventario = ? ", (id_item,))
            items = cursor.fetchall()
            print("-"*40)
            for item in items:
                print(f"Item #: {item[0]} \nNombre: {item[1]} \nPoder: {item[2]} \nUso: {item[3]} \nCantidad: {item[4]}")
                print("-"*40)
            cursor.execute("SELECT * FROM inventario WHERE id_inventario = ?", (id_item,))
            item = cursor.fetchone()
            print(f"¿Estas seguro que quieres eliminar el item {item[1]}? (si/no)")
            op = str(input(": ")).lower()
            if op == "si":
                cursor.execute("DELETE FROM inventario WHERE id_inventario =?", (id_item,))
            else:
                print("========== Item No Eliminado ==========")
                input("\npresiona Enter para continuar...")
                return
            conexion.commit()
            print("========== Item Eliminado Correctamente ==========")
            input("\npresiona Enter para continuar...")
        else:
            print("\n========== No Existe Ningún Item ==========")
            input("\npresiona Enter para continuar...")
    else:
        print("\n========== No Existe Ningún Jugador ==========")
        input("\npresiona Enter para continuar...")

# ===== CHECKPOINT 3 =====
# ===== C =====

def agregar_habilidad():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    print("\n========== Jugador/es disponibles ==========")
    print("-"*40)
    for jugador in jugadores:
        print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
        print("-"*40)
    id_jugador = int(input("\nID del jugador elegido: "))
    limpiar_pantalla()
    print("========== Agregar Habilidad ==========")
    nombre = input("Nombre de la habilidad: ")
    elemento = input("Elemento de la habilidad: ")
    nivel = float(input("Nivel de la habilidad: "))
    desbloqueada = input("¿Está desbloqueada? (si/no): ").lower()
    if desbloqueada == "si":
        desbloqueada = "si"
    else:
        desbloqueada = "no"
    elementos_compatibles = input("Elementos compatibles (separados por coma): ")

    cursor.execute("INSERT INTO habilidades (nombre, elemento, nivel, desbloqueada, elementos_compatibles, id_jugador) VALUES (?, ?, ?, ?, ?, ?)",
              (nombre, elemento, nivel, desbloqueada, elementos_compatibles, id_jugador))
    conexion.commit()
    print(f"\n========== Habilidad '{nombre}' Agregada correctamente ==========")
    input("\npresiona Enter para continuar...")

# ===== R =====

def listar_habilidad():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    print("\n========== Jugador/es disponibles ==========")
    print("-"*40)
    for jugador in jugadores:
        print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
        print("-"*40)
    print("¿Qué jugador desea revisar sus habilidades?")
    id_jugador = int(input(": "))
    limpiar_pantalla()
    print("========== Lista De Habilidades ==========")
    cursor.execute("SELECT * FROM habilidades WHERE ID_JUGADOR = ?", (id_jugador,))
    habilidades = cursor.fetchall()
    if habilidades:
        print("-"*40)
        for habilidad in habilidades:
            print(f"ID: {habilidad[0]} \nNombre: {habilidad[1]} \nElemento: {habilidad[2]} \nNivel: {habilidad[3]} \nDesbloqueada: {habilidad[4]} \nElementos compatibles: {habilidad[5]}")
            print("-"*40)
        input("presiona Enter para continuar...")
    else:
        print("========== No hay Habilidades Existentes ==========")
        input("presiona Enter para continuar...")

# ===== U =====

def actualizar_habilidad():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
            print("-"*40)
        print("¿Qué jugador desea actualizar una habilidad?: ")
        id_jugador = int(input(": "))
        limpiar_pantalla()
        cursor.execute("SELECT id_habilidades, nombre, elemento, nivel, desbloqueada, elementos_compatibles FROM habilidades WHERE id_jugador = ? ", (id_jugador,))
        habilidades = cursor.fetchall()
        if habilidades:
            print("\n========== Habilidad/es disponibles ==========")
            print("-"*40)
            for habilidad in habilidades:
                print(f"Habilidad #: {habilidad[0]} | Nombre: {habilidad[1]} | Elemento: {habilidad[2]} | Nivel: {habilidad[3]} | Desbloqueada: {habilidad[4]} | Elementos_compatibles: {habilidad[5]}")
                print("-"*40)
            id_poder = int(input("¿Qué habilidad desea actualizar?: "))
            limpiar_pantalla()
            cursor.execute("SELECT id_habilidades, nombre, elemento, nivel, desbloqueada, elementos_compatibles FROM habilidades WHERE id_habilidades = ? ", (id_poder,))
            habilidades = cursor.fetchall()
            print("-"*40)
            for habilidad in habilidades:
                print(f"Habilidad #: {habilidad[0]} | Nombre: {habilidad[1]} | Elemento: {habilidad[2]} | Nivel: {habilidad[3]} | Desbloqueada: {habilidad[4]} | Elementos_compatibles: {habilidad[5]}")
                print("-"*40)
            print("\n========== Actualizar Habilidad ==========")
            print("\n¿Qué deseas actualizar?")
            print("1. Nombre")
            print("2. Elemento")
            print("3. Nivel")
            print("4. Desbloqueado")
            print("5. Elementos compatibles")
            op = int(input("\nElige una opción: "))
            match op:
                case 1:
                    nuevo_valor = input("Nuevo nombre: ")
                    cursor.execute("UPDATE habilidades SET nombre = ? WHERE id_habilidades = ?", (nuevo_valor, id_poder))
                case 2:
                    nuevo_valor = input("Nuevo elemento: ")
                    cursor.execute("UPDATE habilidades SET elemento = ? WHERE id_habilidades = ?", (nuevo_valor, id_poder))
                case 3:
                    nuevo_valor = float(input("Nuevo nivel: "))
                    cursor.execute("UPDATE habilidades SET nivel = ? WHERE id_habilidades = ?", (nuevo_valor, id_poder))
                case 4:
                    nuevo_valor = input("¿Esta desbloqueado?(si/no): ").lower()
                    if nuevo_valor == "si" or nuevo_valor == "no":
                        cursor.execute("UPDATE habilidades SET desbloqueada = ? WHERE id_habilidades = ?", (nuevo_valor, id_poder))
                    else:
                        print("Respuesta no valida")
                        input("presiona Enter para continuar...")
                        return
                case 5:
                    nuevo_valor = input("Nuevos elementos compatibles: ")
                    cursor.execute("UPDATE habilidades SET elementos_compatibles = ? WHERE id_habilidades = ?", (nuevo_valor, id_poder))
                case _:
                    print("----- OPCIÓN NO VALIDA -----")
                    print("----- INTENTELO NUEVAMENTE -----")
                    input("presiona Enter para continuar...")
                    return
            conexion.commit()
            print("\n========== Habilidad Actualizada Correctamente ==========")
            input("\npresiona Enter para continuar...")
        else:
            print("\n========== No Existe Ninguna Habilidad ==========")
            input("\npresiona Enter para continuar...")
    else:
        print("\n========== No Existe Ningún Jugador ==========")
        input("\npresiona Enter para continuar...")


# ===== D =====

def eliminar_habilidad():
    limpiar_pantalla()
    cursor.execute("SELECT id_jugador, nombre, vida FROM jugadores")
    jugadores = cursor.fetchall()
    if jugadores:
        print("\n========== Jugador/es disponibles ==========")
        print("-"*40)
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Vida: {jugador[2]}")
        print("-"*40)
        print("¿Qué jugador desea eliminar una habilidad?: ")
        id_jugador = int(input(": "))
        limpiar_pantalla()
        cursor.execute("SELECT id_habilidades, nombre, elemento, nivel, desbloqueada, elementos_compatibles  FROM habilidades WHERE id_jugador = ? ", (id_jugador,))
        habilidades = cursor.fetchall()
        if habilidades:
            print("\n========== Habilidad/es disponibles ==========")
            print("-"*40)
            for habilidad in habilidades:
                print(f"Habilidad #: {habilidad[0]} | Nombre: {habilidad[1]} | Elemento: {habilidad[2]} | Nivel: {habilidad[3]} | Desbloqueada: {habilidad[4]} | Elementos_compatibles: {habilidad[5]}")
                print("-"*40)
            id_poder = int(input("¿Qué habilidad desea eliminar?: "))
            limpiar_pantalla()
            cursor.execute("SELECT id_habilidades, nombre, elemento, nivel, desbloqueada, elementos_compatibles FROM habilidades WHERE id_habilidades = ? ", (id_poder,))
            habilidades = cursor.fetchall()
            print("-"*40)
            for habilidad in habilidades:
                print(f"Habilidad #: {habilidad[0]} | Nombre: {habilidad[1]} | Elemento: {habilidad[2]} | Nivel: {habilidad[3]} | Desbloqueada: {habilidad[4]} | Elementos_compatibles: {habilidad[5]}")
                print("-"*40)
            print("========== Eliminar Habilidad ==========")
            id_poder = int(input("ID del item a eliminar: "))
            cursor.execute("SELECT * FROM habilidades WHERE id_habilidades = ?", (id_poder,))
            poder = cursor.fetchone()
            print(f"¿Estás seguro que quieres eliminar la habilidad {poder[1]}? (si/no)")
            op = str(input(": ")).lower()
            if op == "si":
                cursor.execute("DELETE FROM habilidades WHERE id_habilidades =?", (id_poder,))
            else:
                print("========== Habilidad No Eliminada ==========")
                input("presiona Enter para continuar...")
                return
            conexion.commit()
            print("========== Habilidad Eliminado Correctamente ==========")
            input("\npresiona Enter para continuar...")
        else:
            print("\n========== No Existe Ninguna Habilidad ==========")
            input("\npresiona Enter para continuar...")
    else:
        print("\n========== No Existe Ningún Jugador ==========")
        input("\npresiona Enter para continuar...")

# ===== CHECKPOINT 4 =====
# ===== MENÚ =====

def menu():
    while True:
        limpiar_pantalla()
        print("=============================")
        print("      MENÚ GAMMA         ")
        print("=============================")
        print("1. Jugadores")
        print("2. Inventario")
        print("3. Habilidades")
        print("4. Salir")

        opcion = input("\nElige una opción: ")

        match opcion:
            case "1":
                menu_jugadores()
            case "2":
                menu_inventario()
            case "3":
                menu_habilidades()
            case "4":
                print("\nCerrando Menú... ¡Hasta luego!")
                conexion.close()
                break
            case _:
                print("\nOpción no válida.")
                input("\nPresiona Enter para continuar...")

# ===== SUB-MENÚS =====
# ----- Jugadores -----

def menu_jugadores():
    while True:
        limpiar_pantalla()
        print("=============================")
        print("          JUGADORES          ")
        print("=============================")
        print("1. Agregar jugador")
        print("2. Listar jugadores")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("5. Volver")

        opcion = input("\nElige una opción: ")

        match opcion:
            case "1":
                agregar_jugador()
            case "2":
                listar_jugador()
            case "3":
                actualizar_jugador()
            case "4":
                eliminar_jugador()
            case "5":
                break
            case _:
                print("\nOpción no válida.")
                input("\nPresiona Enter para continuar...")

# ----- Inventario -----

def menu_inventario():
    while True:
        limpiar_pantalla()
        print("=============================")
        print("         INVENTARIO          ")
        print("=============================")
        print("1. Agregar ítem")
        print("2. Listar inventario")
        print("3. Actualizar ítem")
        print("4. Eliminar ítem")
        print("5. Volver")

        opcion = input("\nElige una opción: ")

        match opcion:
            case "1":
                agregar_inventario()
            case "2":
                listar_inventario()
            case "3":
                actualizar_inventario()
            case "4":
                eliminar_inventario()
            case "5":
                break
            case _:
                print("\nOpción no válida.")
                input("\nPresiona Enter para continuar...")

# ----- Habilidades -----

def menu_habilidades():
    while True:
        limpiar_pantalla()
        print("=============================")
        print("        HABILIDADES          ")
        print("=============================")
        print("1. Agregar habilidad")
        print("2. Listar habilidades")
        print("3. Actualizar habilidad")
        print("4. Eliminar habilidad")
        print("5. Volver")

        opcion = input("\nElegí una opción: ")

        match opcion:
            case "1":
                agregar_habilidad()
            case "2":
                listar_habilidad()
            case "3":
                actualizar_habilidad()
            case "4":
                eliminar_habilidad()
            case "5":
                break
            case _:
                print("\nOpción no válida.")
                input("\nPresioná Enter para continuar...")

if __name__ == "__main__":
    menu()
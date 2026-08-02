import sqlite3  # Importa la librería SQLite3 para manejar la base de datos
import os  # sistema operativo en el que se está ejecutando Python.
 
# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')  # nt:window
 
# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect("biblioteca.db")  # Crea o abre la base de datos llamada 'biblioteca.db'
c = conn.cursor()  # Crea un cursor para ejecutar comandos SQL
 
# Crear la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                anio INTEGER NOT NULL
            )''')
conn.commit()  # Guarda los cambios en la base de datos
 
def agregar_libro(titulo, autor, anio):
    """Agrega un libro a la base de datos."""
    c.execute("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", (titulo, autor, anio))  # Inserta
    conn.commit()  # Guarda los cambios
    print("\nLibro agregado correctamente.")
 
def listar_libros():
    """Muestra todos los libros registrados en la base de datos."""
    c.execute("SELECT * FROM libros")  # Consulta todos los libros
    libros = c.fetchall()  # Obtiene todos los resultados
    if libros:
        print("\nLista de libros:")
        print("="*40)
        for libro in libros:
            print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]}")
        print("="*40)
    else:
        print("\nNo hay libros registrados.")
 
def actualizar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio):
    """Actualiza los datos de un libro existente."""
    # Actualiza los datos
    c.execute("UPDATE libros SET titulo=?, autor=?, anio=? WHERE id=?", (nuevo_titulo, nuevo_autor, nuevo_anio, id_libro))
    conn.commit()  # Guarda los cambios
    print("\nLibro actualizado correctamente.")
 
def eliminar_libro(id_libro):
    """Elimina un libro de la base de datos."""
    c.execute("DELETE FROM libros WHERE id=?", (id_libro,))  # Elimina el libro con el ID especificado
    conn.commit()  # Guarda los cambios
    print("\nLibro eliminado correctamente.")
 
def menu():
    """Muestra un menú de opciones para gestionar la biblioteca."""
    while True:
        limpiar_pantalla()
        print("\n=== Biblioteca Virtual ===")  # Encabezado del menú
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ")  # Captura la opción elegida
 
        if opcion == "1":  # Agregar un nuevo libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            agregar_libro(titulo, autor, anio)
        elif opcion == "2":  # Listar todos los libros
            listar_libros()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":  # Actualizar un libro existente
            id_libro = int(input("ID del libro a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            nuevo_anio = int(input("Nuevo año: "))
            actualizar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio)
        elif opcion == "4":  # Eliminar un libro por ID
            id_libro = int(input("ID del libro a eliminar: "))
            eliminar_libro(id_libro)
        elif opcion == "5":  # Salir del programa
            print("\nSaliendo del programa... ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida, intente nuevamente.")
        input("\nPresione Enter para continuar...")
 
if __name__ == "__main__":
    menu()  # Inicia el menú
    conn.close()  # Cierra la conexión con la base de datos al finalizar
# if __name__ == "__main__":
# Permite definir funciones y clases en un archivo sin ejecutarlas automáticamente cuando se importan.
# Es útil para pruebas y scripts reutilizables.
# Evita la ejecución innecesaria de código cuando un módulo se usa en otros proyectos.
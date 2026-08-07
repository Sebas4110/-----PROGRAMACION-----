
#
def diccionario():
    alumnos = [
        {"nombre":"pedro", "edad": 20, "calificacion": 3.5},
        {"nombre":"maria", "edad": 30, "calificacion": 4.5},
        {"nombre":"pablo", "edad": 28, "calificacion": 3.7}
    ]
    print(alumnos[1]["calificacion"])
    total = sum(alumno["calificacion"] for alumno in alumnos)
    promedio = total / len(alumnos)
    print(f"el promedio es: {promedio:.1f}")

diccionario()
#listas()
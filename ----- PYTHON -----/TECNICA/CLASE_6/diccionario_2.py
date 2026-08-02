#tecnicamente esto es un diccionario
#-------------ejemplo 1-----------------
alumnos = [
        {"nombre":"pedro", "edad": 20, "calificacion": 3.5},
        {"nombre":"maria", "edad": 30, "calificacion": 4.5},
        {"nombre":"pablo", "edad": 28, "calificacion": 3.7}
    ]

escuela= {
    "alumnos": alumnos,
    "maestros": [
        {"nombre": "martin", "grado": "licenciado"},
        {"nombre": "fernando", "grado": "maestria"},
        {"nombre": "pedro", "grado": "doctorado"}
    ]
}
#debo de comprender que significa (for ---- in -----)
print("Alumnos")
for alumno in escuela["alumnos"]:
    print(f"nombre: {alumno['nombre']} edad: {alumno['edad']} calificaciones: {alumno['calificacion']}")

print("\nMaestros")
for maestro in escuela["maestros"]:
    print(f"nombre: {maestro['nombre']} grado: {maestro['grado']}")
#
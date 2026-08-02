
#Variables: es un espacio de memoria ram para almacenar datos

# forma de declarar
nombre_persona = 'mateo'
nombrepersona = 'luis'
_nombre_persona = 'mario'
hello_world = 'un paso para el hombre, un gran paso para la humanidad'

#formas incorrectas
#-person
#4personas
#nombre persona

#imprimir (print)
print(hello_world)

#tipos de variables
#(enteros, decimal, caracter)
# entero como int = negativos y positivos (NO DECIMALES)

numeroEntero1 = 12
numeroEntero2 = 45

print(numeroEntero1)
print(numeroEntero2)
print(type(numeroEntero1))

#Type significa decir que tipo de dato es

#decimales (float)
numerdecimal = 3.5
print('numero decimal: ', numerdecimal)
print(type(numerdecimal))

#complejos(complex)
numerosImaginarios = 3 + 5J
print('numero imaginario: ',numerosImaginarios)
print(type(numerosImaginarios))

#string (str)
nombrecliente = 'jose'
print('nombrecliente: ',nombrecliente)
print(type(nombrecliente))

#booleanos (bool)
cuentafacebook = True
correo_electronico = False
print('booleanos: ',cuentafacebook)
print(type(correo_electronico))

#listas ([list])
lista = [1, 'arturo', 1.3, -500]
print(lista)
print(lista[3])
print(type(lista))

if (True):
    print('hola mundo')
else:
    print('adios mundo')
    #else es el "sino" en español

#poner un campo nuevo
lista.insert(1,'gonzales')

#me faltó una cosa en 'insert' =(

# para mover como si fuera "inicio y fin" usa control+(flechas) para mayor rapidez

#tupla
tupla = (1, 2, 3, 4, 5)
print(tuple)
print(type[tuple])

print(tuple[1])

#diccionario
estudiante = {
        'nombre' : 'juan',
        "edad" :19,
        "genero":'m'
        'estado matricula'
}

print(estudiante)
print(type[estudiante])

estudiante['nombre'] = 'carlos'
print(estudiante.items())

#set set{}
conjunto = {1,2,2,3,4,4,3,7,6,5}
print(conjunto)
print(type(conjunto))

print (4 in conjunto)

def generador1():
    for i in range(101):
        yield i

for i in generador1():
   print(i)

def generador2(lista):
    for numero in lista:
        yield numero**2

numero = [1,2,3,4,5]

for total in generador2(numero):
    print(total)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(8):
    print(next(fib))

import random
import string

def generador_passwords(cantidad, longitud=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    for _ in range(cantidad):
        yield ''.join(random.choices(caracteres, k=longitud))

for pwd in generador_passwords(5):
    print(pwd) 
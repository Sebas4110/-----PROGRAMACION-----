# if = condicional

#numero = int(input("escriba un numero positivo: "));
#if numero < 0:
    #print("dije que son numeros positivos");
#print(f"has escrito en numero{numero}");      

#if else
#edad = int(input("cuantos años tiene? "))
#if edad < 18:
    #print("usted es menor de edad")
#else:
#    print("usted es mayor de edad")
 #   print("debe seguir aprendiendo")
#print("algoritmo terminado")        

#CONDICIONALES ANIDADAS
#print("este programa mezcla dos colores. \nr.Rojo a.Azul")
#primera = input("Escoja un color (r o a): ")
#if primera == "r":

#condiconal elif
edad = int(input("cuantos años tienes?"))
if edad >= 18:
    print("usted es mayor de edad")
elif edad < 0:
    print("no es posible tener edad negativa")
elif edad >= 0 and edad < 4:
    print("como entonces estás escribiendo esto con esa edad?")
else:
    print("usted es menor de edad")

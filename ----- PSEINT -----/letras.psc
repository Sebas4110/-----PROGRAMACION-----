Algoritmo letras
	definir letra como caracter
	Escribir 'ingresa una letra cualquiera'
	Leer letra
	Mientras longitud(letra) <> 1 Hacer
		Escribir "solo una letra"
		Escribir "ingresa una letra cualquiera"
		Leer letra
	FinMientras
	letra = minusculas(letra)
	Según letra Hacer
		'a':
			Escribir 'es la primera vocal'
		'e':
			Escribir 'es la segunda vocal'
		'i':
			Escribir 'es la tercera vocal'
		'o':
			Escribir 'es la cuarta vocal'
		'u':
			Escribir 'es la ultima vocal'
		De Otro Modo:
			Escribir 'esto es una consonante'
	FinSegún
FinAlgoritmo

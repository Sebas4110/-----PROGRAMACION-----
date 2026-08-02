Algoritmo precio_y_valor
	Definir precio Como Real
	Definir categoria Como Cadena
	Escribir 'ingresa un precio'
	Leer precio
	Escribir 'ahora dime a que categoria pertenece'
	Escribir 'A, B o C'
	Leer categoria
	categoria <- minusculas(categoria)
	Mientras  NO ((categoria=='a') O (categoria=='b') O (categoria=='c')) Hacer
		Escribir 'no existe esa categoria'
		Escribir 'intentelo nuevamente'
		Escribir 'A, B o C'
		Leer categoria
		categoria <- minusculas(categoria)
	FinMientras
	Según categoria Hacer
		'a':
			precio <- precio*(1-0.1)
			Escribir 'el descuento es del 10%'
		'b':
			precio <- precio*(1-0.2)
			Escribir 'el descuento es del 20%'
		'c':
			precio <- precio*(1-0.3)
			Escribir 'el descuento es del 30%'
	FinSegún
	Escribir 'el precio final será de $', precio
FinAlgoritmo

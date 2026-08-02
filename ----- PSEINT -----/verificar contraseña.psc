Algoritmo sin_titulo
	Definir minus, num, esp, mayus, len Como Lógico
	Definir long Como Entero
	Definir contra Como Cadena
	Repetir
		Escribir 'ingrese una contraseña de 8 caracteres, con mayus, numero, y caracter especial'
		Leer contra
		long <- Longitud(contra)
		minus <- FALSO
		mayus <- FALSO
		num <- FALSO
		esp <- FALSO
		Si no(long>=8) Entonces
			Escribir 'demasiado breve, tiene ', long, ' caracteres'
		FinSi
		Si minus Entonces
		
		SiNo
			Escribir 'faltan minusculas'
		FinSi
		Si mayus Entonces
		
		SiNo
			Escribir 'faltan mayusculas'
		FinSi
		Si num Entonces
		
		SiNo
			Escribir 'faltan numeros'
		FinSi
		Si esp Entonces
		
		SiNo
			Escribir 'faltan caracteres especiales'
		FinSi
	Hasta Que (minus==verdadero) Y (mayus==verdadero) Y (num==verdadero) Y (esp==verdadero)
	Escribir 'CONTRASEÑA VALIDA'
FinAlgoritmo

Funcion  datos = pedir_datos(mensaje)
	escribir mensaje
	leer datos
	mientras datos <= 0 Hacer
		escribir "El valor debe ser mayor que cero"
		escribir mensaje
		leer datos
	FinMientras
FinFuncion

	Algoritmo tabla_nutricional
	definir peso, estatura, imc Como Real
	escribir "--- SISTEMA DE EVALUACIÓN NUTRICIONAL ---"
	
	peso = pedir_datos ("ingrese su peso en kilogramos: ")
	estatura = pedir_datos ("ingrese su estatura en metros: ")
	
	
	imc = peso /(estatura ^ 2)
	escribir "tu indice de masa corporal es ", imc
	
	si imc < 18.5 Entonces
			escribir "estado: bajo peso"
	SiNo
		si imc >= 18.5 y imc < 25 Entonces
				escribir "estado: peso normal"
		SiNo
			si imc >= 25 y imc < 30 Entonces
					escribir "estado: sobrepeso"
			SiNo
					Escribir "estado: obesidad"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo

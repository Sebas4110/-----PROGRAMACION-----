funcion sum = suma(cal)
	sum = 0
	Para i = 0 Hasta 5 hacer
		sum = sum + cal[i]
	FinPara
FinFuncion

Función evaluarMateria(mate,nota)
	nota = nota/6
	Si nota>7 Entonces
			Escribir 'materia ', mate, ' nota: ', nota, ' | estado: APROBADO'
	SiNo
			Si nota>4 Y nota<7 Entonces
				Escribir 'materia ', mate, ' nota: ', nota, ' | estado: RECUPERACION'
		SiNo
				Escribir 'materia ', mate, ' nota: ', nota, ' | estado: PERDIO'
		FinSi
	FinSi	
FinFunción

Algoritmo notas

	Definir mate Como Cadena
	Escribir 'materia a evaluar'
	Leer mate
	Dimensionar calificaciones(6)
	Para i = 0 Hasta 5 Hacer
		// aleatorio entre 1.0 a 5.0
		calificaciones[i] <- aleatorio(1,10)
		escribir "Nota ", i+1, "º: ", calificaciones[i]
	FinPara
	Escribir '=== RESULTADOS FINALIZADOS ==='
	Escribir 'clic para revisar'
	Leer esperar
	// llamar subProceso de evaluacion
	
	evaluarMateria(mate,suma(calificaciones))
	
FinAlgoritmo

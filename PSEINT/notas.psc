subproceso EvaluarMateria(nombre,nota)
	si nota >= 3.5 Entonces
		escribir 'materia ', nombre, ' nota: ',nota,' | estado: GANO'
	SINO
		escribir 'materia ', nombre, ' nota: ',nota,' | estado: PERDIO'
	FinSi
FinSubProceso

Algoritmo notas
	definir cant Como Entero 
	definir prom como real
	
	escribir 'ingresa la cantidad de materias'
	leer cant
	
	dimension nombre[cant]
	dimension calificaciones[cant]
	
	para i <- 0 hasta cant-1 Hacer
		escribir 'nombre de la materia:'
		leer nombre[i]
		//aleatorio entre 1.0 a 5.0
		calificaciones[i] = aleatorio(10,50) /10
	FinPara
	escribir '=== RESULTADOS FINALIZADOS ==='
	Escribir 'clic para revisar'
	leer esperar
	
	//llamar subProceso de evaluacion
	para i <- 0 hasta cant-1 Hacer
	 evaluarMateria(nombre[i],calificaciones[i])
	FinPara
FinAlgoritmo

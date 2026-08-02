funcion duplicado =dupli(num)
	duplicado = num*2
FinFuncion

Algoritmo duplicador_de_numeros
	definir lista1, lista2 como entero
	dimension lista1[5]
	dimension lista2[5]
	para i = 0 hasta 4 Hacer
		lista1[i] = aleatorio[1,20]
	FinPara
	para i = 0 hasta 4 hacer
		lista2[i] = dupli(lista1[i])
		
	FinPara
	
	para I = 0 hasta 4 Hacer
		escribir 'original ', lista1[i]
		escribir 'duplicado ', lista2[i]
	FinPara
	
FinAlgoritmo

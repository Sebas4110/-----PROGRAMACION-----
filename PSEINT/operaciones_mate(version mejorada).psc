Función resta <- res(n1,n2)
	resta <- n1-n2
FinFunción

Función suma <- sum(n1,n2)
	suma <- n1+n2
FinFunción

Función multiplicacion <- mult(n1,n2)
	multiplicacion <- n1*n2
FinFunción

Función division <- div(n1,n2)
	division <- n1/n2
FinFunción

funcion potencia = pot(n1,n2)
	potencia = n1^n2
FinFuncion

funcion radicacion = rad(n1,n2)
	radicacion = n1^(1/n2)
FinFuncion
Algoritmo operaciones_mate
	Definir n1, n2 Como Real
	definir num como entero
	Escribir 'dime dos numeros'
	Leer n1, n2
	Escribir 'que operacion quieres hacer?'
	escribir '1: suma, 2: resta, 3: multiplicación, 4: división, 5: potenciación, 6: radicación'
	leer num
	Según num Hacer
	1: escribir 'la suma de estos dos es ', sum(n1,n2)
	2: escribir 'la resta de estos dos es', res(n1,n2)
	3: escribir 'la multiplicacion de estos dos es ', mult(n1,n2)
	4: escribir 'la division de estos dos es ', div(n1,n2)
	5: escribir 'la potencia de estos dos es ', pot(n1,n2)
	6: escribir 'la radicacion de estos dos es ', rad(n1,n2)
FinSegún
FinAlgoritmo

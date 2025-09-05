Proceso promedio_impares
	N <- 1
	Escribir "N | sum_imp | M | prom_i | N!=0  |  N%2!=0"
	Escribir "-----------------------------"
	Mientras N<>0 Hacer
		Escribir "Ingrese Valor N:"
		Leer N
		Si N<>0 Entonces
			Si N%2<>0 Entonces
				// Validación de si N es Impar
				sum_imp <- sum_imp+N
				M <- M+1
				prom_i <- sum_imp/M
			FinSi
			Escribir "El promedio de impares ingresados es: ",prom_i
		FinSi
		Escribir N, " | ", sum_imp," | ", M, " | ",prom_i," | ",N<>0," | ", N%2<>0
	FinMientras
FinProceso

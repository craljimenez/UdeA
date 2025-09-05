Proceso Sum_N_enteros
	Escribir "Ingresé valor de N:"
	Leer N
	i <- N
	sum <- 0
	Escribir "N | i | sum | i != 0"
	Escribir "-----------------------"
	Mientras i <> 0 Hacer
		sum <- sum + i
		i <- i - 1
		Escribir N," | ", i, " | ",sum," | ",i<>0
	FinMientras
	Escribir "La suma es igual a: ",sum
FinProceso

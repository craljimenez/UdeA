Proceso Sum_N_enteros
	Escribir "Ingresé valor de N:"
	Leer N
	i <- 0
	sum <- 0
	Escribir "N | i | sum | i< N"
	Escribir "-----------------------"
	Mientras i < N Hacer
		i <- i+1
		sum <- sum + i
		Escribir N," | ", i, " | ",sum," | ",i<N
	FinMientras
	Escribir "La suma es igual a: ",sum
FinProceso

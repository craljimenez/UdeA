Proceso bisiesto
	Escribir "Ingrese a�o a validar: "
	Leer anio
	Si anio % 4 == 0 Entonces
		Si anio%100==0 Entonces
			Si anio%400 == 0 Entonces
				es_bisiesto <- "S�"
			SiNo
				es_bisiesto <- "NO"
			FinSi
		SiNo
			es_bisiesto <- "s�"
		FinSi
	SiNo
		es_bisiesto <- "no"
	FinSi
	Escribir "El a�o" ,anio," ",es_bisiesto," es bisiesto"
FinProceso

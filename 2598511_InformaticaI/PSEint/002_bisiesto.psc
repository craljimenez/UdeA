Proceso bisiesto
	Escribir "Ingrese año a validar: "
	Leer anio
	Si anio % 4 == 0 Entonces
		Si anio%100==0 Entonces
			Si anio%400 == 0 Entonces
				es_bisiesto <- "SÍ"
			SiNo
				es_bisiesto <- "NO"
			FinSi
		SiNo
			es_bisiesto <- "sí"
		FinSi
	SiNo
		es_bisiesto <- "no"
	FinSi
	Escribir "El año" ,anio," ",es_bisiesto," es bisiesto"
FinProceso

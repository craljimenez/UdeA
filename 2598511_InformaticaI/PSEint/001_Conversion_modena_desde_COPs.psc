Proceso Conversion_modena_desde_COPs
	// Conversion moneda
	Escribir "Ingrese Valor en COPs: "
	Leer V
	Escribir "Ingrese Divisa Destino (USD o EUR o GBP): "
	Leer D
	Si D=="USD" Entonces
		C <- V/4021.02
		Escribir "Su conversión es: ",C," ",D
	SiNo
		Si D=="EUR" Entonces
			C <- V/4700.10
			Escribir "Su conversión es: ",C," ",D
		SiNo
			Si D=="GBP" Entonces
				C <- V/5422.42
				Escribir "Su conversión es: ",C," ", D
			SiNo
				Escribir "Error: Divisa invalida, se permite solamente USD, EUR o GBP."
			FinSi
		FinSi
	FinSi
FinProceso

lista = []

opc = 99

print("Menú de opciones para la lista de números a ingresar:\n 1: ingresar números\n 2: ordenar números\n 3: calcular el máximo\n 4: calcular el mínimo\n 5: calcular el promedio\n 0: para terminar\n")

while(opc != 0):
	opc = int(input("Ingrese una opcion\n"))
	if(opc == 1):
		lista.append(int(input("Ingrese un numero\n")))
	elif(opc == 2):
		lista.sort()
		print(lista)
	elif(opc == 3):
		print(f"El valor maximo de la lista es {max(lista)}")
	elif(opc == 4):
		print(f"El valor minimo de la lista es {min(lista)}")
	elif(opc == 5):
		prom = sum(lista)/(len(lista))
		print(f"El promedio es {prom}\n")
	elif(opc!=0)and(opc!=1)and(opc!=2)and(opc!=3)and(opc!=4)and(opc!=5):
		print("La opcion ingresada no es valida")
			
		

lis = []

lis.append(int(input("Ingrese el primer numero\n")))
lis.append(int(input("Ingrese el segundo numero\n")))

print("Menu de opciones:")
print("(1)-Sumar dos numeros")
print("(2)-Restar dos numeros")
print("(3)-Multiplicar dos numeros")
print("(4)-Dividir dos numeros")

opc = int(input("Elija la operacion a realizar\n"))

if(opc == 1):
	print(f"La suma es {sum(lis)}")
elif(opc == 2):
	print(f"La resta es {lis[0]-lis[1]}")
elif(opc == 3):
	print(f"La multiplicacion es {lis[0]*lis[1]}")
elif(opc == 4):
	print(f"La division es {lis[0]/lis[1]}")
elif(opc!=1)and(opc!=2)and(opc!=3)and(opc!=4):
	print("La opcion ingresada no es valida")
					

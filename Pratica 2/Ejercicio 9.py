import random

ran=random.randrange(50)

intentos=0

ok=False

print("Debera adivinar un numero del 1 al 50")

while(ok==False)and(intentos<=10):
	if(intentos==3):
		if(ran%2==0):
			print("El numero a adivinar es par")
		else:
			print("El numero a adivinar es impar")
	num = int(input("Ingrese un numero\n"))
	if(num==ran):
		ok=True
	elif(num<ran):
		print("El numero ingresado es menor")
	elif(num>ran):
		print("El numero ingresado es mayor")					
	intentos+=1

if(ok==True):
	print("Felicidades, has ganado el juego!")
else:
	print("Mejor suerte la proxima")

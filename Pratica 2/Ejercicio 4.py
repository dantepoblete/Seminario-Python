import random

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], [' Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]

copia = preguntas

pun = 0

while(len(copia)!=0):
	num = random.randrange(0,len(copia))
	print(copia[num][0])
	res = input("Escriba su respuesta: Si o No\n").lower()
	if(res==copia[num][1]):
		pun = pun+1
		print("Respuesta Correcta!\n")
	else:
		print("Respuesta Incorrecta\n")
	copia.pop(num)

print(f"Puntaje Final: {pun}")	



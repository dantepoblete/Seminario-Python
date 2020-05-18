import random

def repetirColores(dic):
	a=random.choice(coordenadas)
	while(a in dic.keys()):
		a=random.choice(coordenadas)
	b=random.choice(colores)
	dic[a]=b
	
def sinRepetirColores(dic):
	a=random.choice(coordenadas)
	while(a in dic.keys()):
		a=random.choice(coordenadas)
	b=random.choice(colores)
	while(b in dic.values()):
		b=random.choice(colores)
	dic[a]=b			

colores = ['azul','amarillo','rojo','blanco','negro']

coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic1 = {}

dic2 = {}

for i in coordenadas:	#Sin importar que los colores se repitan
	repetirColores(dic1)

print(dic1)

for i in coordenadas:	#Sin repetir colores
	sinRepetirColores(dic2)
	
print(dic2)		

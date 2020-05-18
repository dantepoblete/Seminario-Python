reg={}

nombre=input("Ingrese un nombre: ").lower()
while(nombre!=""):
	dic={}
	nivel=int(input(f"Ingrese el nivel alcanzado de {nombre}: "))
	dic.setdefault("nivel",nivel)
	puntaje=int(input(f"Ingrese el puntaje maximo obtenido de {nombre}: "))
	dic.setdefault("puntaje",puntaje)
	tiempo=int(input(f"Ingrese el tiempo de juego de {nombre}: "))
	dic.setdefault("tiempo",tiempo)
	reg.setdefault(nombre,dic)
	nombre=input("Ingrese un nombre: ").lower()
	while(nombre in reg.keys()):
		nombre=input(f"El nombre de usuario {nombre} ya existe en el registro, ingrese otro: ").lower()
		
print("\n")
aca=reg.items()
print(aca)		

nombre=input("Ingrese el nombre de usuario a buscar: ").lower()
print(reg[nombre])

print("\n")
		
print("Usuarios que jugaron:")		
for jugador in reg.items():
	if(jugador[1]["tiempo"]>0):
		print(jugador[0])
		
print("\n")		
		
print("El jugador con mayor puntaje es:")
print((max(reg.items(),key=lambda jugador:jugador[1]["puntaje"])))

print("\n")

nombre=input("Ingrese un nombre: ").lower()
dic={}
nivel=int(input(f"Ingrese el nivel alcanzado de {nombre}: "))
dic.setdefault("nivel",nivel)
puntaje=int(input(f"Ingrese el puntaje maximo obtenido de {nombre}: "))
dic.setdefault("puntaje",puntaje)
tiempo=int(input(f"Ingrese el tiempo de juego de {nombre}: "))
dic.setdefault("tiempo",tiempo)
reg.setdefault(nombre,dic)
if(nombre in reg.keys()):
	if(reg[nombre]["puntaje"]<dic["puntaje"]):
		reg[nombre]=dic
	print(f"Datos de {nombre} actualizados.")	
else:
	reg.setdefault(nombre,dic)	

print("\n")

print("Primeros 10 puntajes maximos:")
maximos=sorted(reg.items(),key=lambda jugador:jugador[1]["puntaje"],reverse=True)
maximos[:10]

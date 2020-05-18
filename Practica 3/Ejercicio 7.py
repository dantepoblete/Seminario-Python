def max10(**kargs):
	maximos=sorted(reg.items(),key=lambda jugador:jugador[1]["puntaje"],reverse=True)
	i=0
	for jugador in maximo:
		print(f"{i}-{jugador[1]["puntaje"]}.")
		i=i+1
	
def ordApellido(**kargs):
	apellidos=sorted(reg.items(),key=lambda jugador:jugador[1]["nombre"])
	for jugador in apellidos:
		print(jugador)
	
def ordNivel(**kargs):
	niveles=sorted(reg.items(),key=lambda jugaor:jugador[1])
	for jugador in niveles:
		print(jugador)	

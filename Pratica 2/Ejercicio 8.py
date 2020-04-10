pal = input("Ingrese una palabra\n").lower()

lis = []

prim = []

for letra in pal:
	cant = pal.count(letra)
	texto = (f"La letra {letra} aparece: {cant} veces" )
	if(texto not in lis):
		lis.append(texto)
	divisores=0
	for i in range(1,(cant+1)):
		if(cant%i == 0):
			divisores=divisores+1
	if(divisores == 2)and(letra not in prim):
		prim.append(letra)	
	
for i in lis:
	print(i)

listado = ",".join(prim)
	
print(f"Por lo tanto las letras {listado} son letras que aparecen un numero primo de veces")

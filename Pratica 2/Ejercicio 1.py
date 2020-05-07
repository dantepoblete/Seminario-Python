tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']

lower = []

greater = []

tup = ()

num = int(input("Ingrese un numero: "))

for i in tam:
	name,space,tupla = i.partition(" ")
	ent,coma,decim = tupla.partition(",")
	ent = int(ent)
	decim = int(decim)
	if(num>ent):
		lower.append(name)
		tup = (ent,decim)
		lower.append(tup)
	else:
		greater.append(name)
		tup = (ent,decim)
		greater.append(tup)
print(f"lista 1 = {greater}")	
print(f"lista 2 = {lower}")

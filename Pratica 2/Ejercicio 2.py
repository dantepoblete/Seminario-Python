tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']

ord = []

tup = ()

for i in tam:
	nom,space,num=i.partition(" ")
	ent,coma,dec = num.partition(",")
	ent = int(ent)
	dec = int(dec)
	tup=(ent,dec)
	ord.append(tup)

ord.sort()

print(f"Lista Ordenada = {ord}")	

lista = ['Auto', '123', 'Viaje', '50', '120']

lista2 = []

for i in lista:
	if(i.isdecimal()==True):
		i = int(i)
		lista2.append(i)

print(f"Lista Numerica = {lista2}")		

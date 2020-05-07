imagenes=['im1','im2','im3']

dic = {}

for i in imagenes:
	x = int(input("Ingrese la coordenada X: "))
	y = int(input("Ingrese la coordenada Y: "))
	tup = (x,y)
	while(tup in dic.values()):
		print("Coordenadas ya existentes, vuelva a ingresar los valores")
		x = int(input("Ingrese la coordenada X: "))
		y = int(input("Ingrese la coordenada Y: "))
		tup = (x,y)
	dic[i]=tup

print(dic)		

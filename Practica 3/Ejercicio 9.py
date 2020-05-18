def enumerarNombres(*args):
	i=0
	for nombre in args:
		print(f"{i}.{nombre}\n")
		i=i+1

nombres=["Dante","Nahuel","Pedro","Juan","Luciano","Ignacio","Lautaro"]
enumerarNombres(*nombres)		

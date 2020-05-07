pal = input("Ingrese una palabra\n").lower()

if(pal == pal[::-1]):
	print("Es palindromo!")
else:
	print("No es palindromo")	

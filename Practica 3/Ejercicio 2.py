def listaPalabras(dic,valor):
	dic.setdefault(len(valor),[]) #Si la clave no existe en el diccionario, creo la clave y le asigno una lista vacia
	if(valor not in dic[len(valor)]): #Si la palabra no esta en la lista, la agrego
		dic[len(valor)].append(valor)
		

frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'''

frase = frase.lower()

lis = frase.split(" ")

nue = []

dic = {}

for i in lis:
	s = i
	if((i[len(i)-1]==",") or (i[len(i)-1]==".")):
		s = str(i[:-1])	#Si tiene "." o "," se lo quito
	nue.append(s)	 

for i in nue:
	listaPalabras(dic,i)

print(dic)		
	

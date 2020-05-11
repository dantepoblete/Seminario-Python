import PySimpleGUI as sg
import os
import json
from datetime import datetime
import hangman
import reversegam
import tictactoeModificado

documento=os.getcwd()+"\datos.txt"

arch=open(documento,'a')

choices = ('Ahorcado', 'Ta-Te-Ti', 'Otello')

def leerDatos():
	with open(documento,'r')as archivo:
		datos=json.load(archivo)
	return datos	

def guardarDatos(datos):
	with open(documento,'w')as archivo:
		json.dump(datos,archivo)
		
def hayErrores(nombre,juego):
	'''Si no fue ingresado el nombre o no fue seleccionado el juego,
	devuelvo True, en caso contrario devuelvo True'''
	error=False
	if(nombre=='')or(nombre==None):
		sg.popup('No ha ingresado un nombre de jugador.')
		error=True
	if(juego==None)or(juego=='')or(juego not in choices):
		sg.popup('No ha seleccionado ningun juego.')			
		error=True
	return error
		
def actualizarDatos(nombre,juego):
	'''Si el archivo está vacio,inicializo sus datos y escribo el primer elemento,
	Si el jugador ya existe en el archivo, actualizo sus datos,
	si no existe el jugador, lo agrego a la estructura'''
	nombre=nombre.lower()
	fechaHora=datetime.now().isoformat()
	if(os.stat(documento).st_size == 0):
		dic={'Jugados':[],'Logins':1,'Ultimo Acceso':fechaHora}
		dat={nombre:dic}
		dat[nombre]['Jugados'].append(juego)
	else:
		dat=leerDatos()
		if(nombre in dat.keys()):
			dat[nombre]['Jugados'].append(juego)
			dat[nombre]['Logins']=dat[nombre]['Logins']+1
			dat[nombre]['Ultimo Acceso']=fechaHora
		else:
			dic={'Jugados':[],'Logins':1,'Ultimo Acceso':fechaHora}
			dat.setdefault(nombre,dic)
			dat[nombre]['Jugados'].append(juego)	
	guardarDatos(dat)
	sg.popup('¡Datos del jugador '+nombre+' actualizados!')		
		
def main(args):
	layout = [  [sg.Text('¡Bienvenido!¿Que desea jugar hoy?', font='Heveltica 15')],
					[sg.Text('Nombre del Jugador'),sg.Input(key='_usuario_')],
					[sg.Text('Juegos Disponibles '),sg.Combo(choices, size=(20, 20), key='_juego_')],
					[sg.Button('Jugar'), sg.Button('Salir')]  ]

	window = sg.Window('Menu de Juegos', layout)
	while True:
		event,values=window.read()
		if event=='Salir':
			break
		if (event=='Jugar')and(hayErrores(values['_usuario_'],values['_juego_'])==False):
			if values['_juego_']=='Ahorcado':
				hangman.main()
			elif values['_juego_']=='Ta-Te-Ti':
				tictactoeModificado.main()
			elif values['_juego_']=='Otello':
				reversegam.main()
			actualizarDatos(values['_usuario_'],values['_juego_'])

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))			

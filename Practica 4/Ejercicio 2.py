import PySimpleGUI as sg
import json
import os

documento='C:\Facultad\lista.txt'

def camposVacios(values):
	if(values['_jugador_']=="" or values['_puntaje_']=="" or values['_tiempo_']=="" or values['_nivel_']==""):
		return True
	else:
		return False	

def leerJugadores():
	with open(documento,'r')as archivo:
		datos=json.load(archivo)
	return datos

def cargarJugador(values):
	jugadores=leerJugadores()
	if((values['_jugador_']).lower() in jugadores.keys()):
		sg.popup('Jugador ya existente,ingrese otro.')
	else:
		dic={'Puntaje':int(values['_puntaje_']),'Tiempo':int(values['_tiempo_']),'Nivel':int(values['_nivel_'])}
		jugadores.setdefault((values['_jugador_']).lower(),dic)
		return jugadores			

def guardarJugador(jugadores):
	with open(documento,'w')as archivo:
		json.dump(jugadores,archivo)	
		
def buscarNombre():
	event, values = sg.Window('Actualizar Jugador',
                  [[sg.T('Nombre del Jugador'), sg.In(key='_nombre_')],
                  [sg.B('OK')]]).read(close=True)
	if(values['_nombre_']==""):
		sg.popup('No ha ingresado un nombre')
	else:	
		jugador = values['_nombre_']
		return jugador

def modificarDatos():
	nombre=buscarNombre()
	if(nombre!=None):
		datos=leerJugadores()
		if(nombre in datos.keys()):
			event, values = sg.Window('Actualizar Datos',
					[[sg.T('Puntaje', size=(15, 1)), sg.In(key='_puntaje_')],
					[sg.T('Tiempo', size=(15, 1)), sg.In(key='_tiempo_')],
					[sg.T('Nivel', size=(15, 1)), sg.In(key='_nivel_')],
					[sg.B('OK')]]).read(close=True)
			jugador=values              
			if((int(values['_puntaje_']))>datos[nombre]['Puntaje']):
				datos[nombre]['Puntaje']=int(values['_puntaje_'])
				datos[nombre]['Tiempo']=int(values['_tiempo_'])
				datos[nombre]['Nivel']=int(values['_nivel_'])
				guardarJugador(datos)
				sg.popup('Los datos han sido actualizados.')	
		else:
			sg.popup('El jugador no se encuentra registrado')
	else:
		sg.popup('Nombre de jugador no válido')	
				
layout = [
    [sg.Text('Ingrese los siguientes datos: ')],
    [sg.Text('Jugador', size=(15, 1)), sg.InputText(key='_jugador_')],
    [sg.Text('Puntaje', size=(15, 1)), sg.InputText(key='_puntaje_')],
    [sg.Text('Tiempo', size=(15, 1)), sg.InputText(key='_tiempo_')],
    [sg.Text('Nivel', size=(15, 1)), sg.InputText(key='_nivel_')],
    [sg.Button('Agregar'), sg.Button('Modificar Datos'), sg.Button('Salir')]
]

window = sg.Window("Ejercicio 5", layout)

archivo=open(documento,'a')

while True:
	event,values=window.read()
	if(event=='Salir'):
		break
	if(event=='Agregar'):
		if(camposVacios(values)==True):
			sg.popup('Falta completar algun dato')
		else:
			if(os.stat(documento).st_size == 0)and(camposVacios(values)==False):
				dic={'Puntaje':int(values['_puntaje_']),'Tiempo':int(values['_tiempo_']),'Nivel':int(values['_nivel_'])}
				doc={(values['_jugador_']).lower():dic}
				guardarJugador(doc)
			else:
				if(os.stat(documento).st_size != 0)and(camposVacios(values)==False):
					jugadores=cargarJugador(values)
					if(jugadores!=None):
						guardarJugador(jugadores)	
	if(event=='Modificar Datos'):
		modificarDatos()
					
window.close()				
	
	

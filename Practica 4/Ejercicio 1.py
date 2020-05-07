import PySimpleGUI as sg
from datetime import datetime
from tkinter import *
import json

layout = [
    [sg.Text('Ingrese los siguientes datos: ')],
    [sg.Text('Temperatura', size=(15, 1)), sg.InputText()],
    [sg.Text('Humedad', size=(15, 1)), sg.InputText()],
    [sg.Button('Agregar'), sg.Button('Guardar Archivo'), sg.Button('Salir')]
]

window = sg.Window("Ejercicio 1", layout)

fechaHora = datetime.now()

ventana=Tk()
ventana.title("Datos")
datos=Listbox(ventana,width=50)

while True:
	event,values=window.read()
	if (event=="Salir"):
		break		
	if (event=="Agregar"):
		if(values[0]!="" and values[1]!=""):
			datos.insert(0,values[0])
			datos.insert(1,values[1])
			datos.insert(2,fechaHora)
			datos.pack()
		else:
			sg.popup('Faltan ingresar valores')	
	if (event=="Guardar Archivo"):
		tam=datos.size()
		i=0
		archivo=open("C:\Facultad\Datos.txt","a")
		while(i<tam):
			dic={}
			dic.setdefault("Temperatura",datos.get(i))
			i+=1
			dic.setdefault("Humedad",datos.get(i))
			i+=1
			dic.setdefault("Fecha y Hora",datos.get(i))
			i+=1
			json.dump(dic,archivo)
		archivo.close()
		sg.popup("Archivo guardado con exito")
		
window.close()
datos.mainloop()

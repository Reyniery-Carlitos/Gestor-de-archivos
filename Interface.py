#-*- coding: utf-8 -*-

"""
@author: crrubio@unah.hn
@Version: 0.1.0
@Fecha: 08/07/2021
"""

from Core.UndirectedGraph import *
from Core.Create import *
from guizero import *
from os import *

class Interface():
	def __init__(self):
		pass

	def display(self):
		app = App(title="Gestor de Archivos", height=600, width=1000, bg="#ffffff")

		#Al momento de elegir el tipo de archivo
		def typeFileChoosed(choose):
			create = Create()
			
			# print(chooseTypeFile.value)
			# Si el tipo de archivo es una carpeta
			if choose == "Carpeta":
				#Funcion que manda a llamar a la clase crear folder
				def createFolder(confirm):	
					if confirm.key == "\r":
						textBox.hide()
						create.createNewFolder(textBox.value, listboxLeft.value)
						listboxLeft.append(textBox.value)
				
				#Caja para nombrar carpetas
				textBox = TextBox(listboxLeft, text="", align="bottom")
				textBox.when_key_pressed = createFolder		
	
			# Si no es una carpeta
			else:
				#Funcion que manda a llamar a la clase crear archivo
				def createFile(confirm):
					if confirm.key == "\r":
						textBox.hide()
						create.createNewFile(textBox.value, listboxLeft.value)
						listboxLeft.append(textBox.value)
				
				# Caja para nombrar archivos
				textBox = TextBox(app, text="")
				textBox.when_key_pressed = createFile

		#Elegira que creara el usuario
		def typeFile():
			# chooseTypeFile = Combo(boxPrincipalContainerListBoxLeft, align="bottom", options=["Carpeta", "Archivo"], command=typeFileChoosed)
			chooseTypeFile = ListBox(listboxLeft, align="bottom", items=["Carpeta", "Archivo"], command=typeFileChoosed, height=80, width=80)
			# chooseTypeFile.when_double_clicked = typeFileChoosed

		#Tipo de accion a realizar
		def typeActionChoose(action):
			if action == "Copiar":
				pass
			elif action == "Cortar":
				pass
			elif action == "Pegar":
				pass
			elif action == "Crear":
				typeFile()

		#Acciones al presinar click derecho sobre un archivo
		def Actions():
			chooseAction = ListBox(listboxLeft, align="bottom", items=["Copiar", "Cortar", "Pegar", "Crear"], command=typeActionChoose)

		#Caja Superior, la que contendra el buscador.
		boxContainerTopBar = Box(app,width="fill", height=50, border=0.5, align="top")
		boxContainerTopBar.set_border(1, "#e5e5e5")

		#Texto Search
		textSearch = Text(boxContainerTopBar, text="Sample Files", size=12,font="Fira Code")

		# # Caja lateral izquierda donde se contendran las rutas a los archivos.
		# boxContainerPaths = Box(app, width=200, height="fill", border=0.5, align="left")
		# boxContainerPaths.set_border(1, "#e5e5e5")

		#Caja Mayor, en la que se contendran las cajas que almacenaran los listbox y demas elementos.
		boxContainerListBox = Box(app, width="fill", height="fill", border=0.5, align="right")
		boxContainerListBox.set_border(1, "#e5e5e5")

		# Caja sub-mayor izquierda, contenida dentro de la caja que contendra los listbox
		boxInsideContainerListBoxLeft = Box(boxContainerListBox, width="fill", height="fill", align="left")

		# Caja sub-mayor Derecha, contenida dentro de la caja que contendra los listbox
		boxInsideContainerListBoxRight = Box(boxContainerListBox, width="fill", height="fill", align="right")

		#Cajas de barras de estado superior 1. - Izquierda
		boxStatusBarTopListBoxLeft = Box(boxInsideContainerListBoxLeft,width="fill", height=40, align="top")
		boxStatusBarTopListBoxLeft.set_border(1, "#e5e5e5")

		#Cajas de barras de estado superior 1. - Derecha
		boxStatusBarTopListBoxRight = Box(boxInsideContainerListBoxRight,width="fill", height=40, align="top")

		# Texto Mis Archivos - Izquierda
		titleMyFiles = Text(boxStatusBarTopListBoxLeft, text="My Files", size=11, align="left", font="Fira Code")

		# Texto Mis Archivos - Derecha
		titleMyFiles = Text(boxStatusBarTopListBoxRight, text="My Files", size=11, align="left", font="Fira Code")

		#Cajas de barras de estado superior 2. - Izquierda
		boxStatusBar2TopListBoxLeft = Box(boxInsideContainerListBoxLeft,width="fill", height=30, align="top")
		boxStatusBar2TopListBoxLeft.set_border(1, "#e5e5e5")

		#Cajas de barras de estado superior 2. - Derecha
		boxStatusBar2TopListBoxRight = Box(boxInsideContainerListBoxRight,width="fill", height=30, align="top")
		boxStatusBar2TopListBoxRight.set_border(1, "#e5e5e5")

		# Texto Nombre de archivos - Izquierda
		titleMyFiles = Text(boxStatusBar2TopListBoxLeft, text="Name", size=10, align="left", font="Fira Code")
		titleSize = Text(boxStatusBar2TopListBoxLeft, text="Size", size=10, align="right", font="Fira Code")

		# Texto Nombre de archivos - Derecha
		titleMyFiles = Text(boxStatusBar2TopListBoxRight, text="Name", size=10, align="left", font="Fira Code")
		titleSize = Text(boxStatusBar2TopListBoxRight, text="Size", size=10, align="right", font="Fira Code")

		#Caja principal de los lixtBox

		boxPrincipalContainerListBoxLeft = Box(boxInsideContainerListBoxLeft,width="fill", height="fill", align="top")

		#Caja principal de los lixtBox
		boxPrincipalContainerListBoxRight = Box(boxInsideContainerListBoxRight,width="fill", height="fill", align="top")

		#List Box
		listboxLeft = ListBox(boxPrincipalContainerListBoxLeft, items=[], height="fill", width="fill", align="top")
		listboxRight = ListBox(boxPrincipalContainerListBoxRight, items=[], height="fill", width="fill", align="top", visible=1)

		# Caja de botones
		btnBoxLeft = Box(boxPrincipalContainerListBoxLeft, align="bottom", height=40, width="fill")
		btnBoxRight = Box(boxPrincipalContainerListBoxRight, align="bottom", height=40, width="fill")

		#Click derecho y agregar archivos
		listboxLeft.when_right_button_pressed = Actions
		#listboxLeft.when_double_clicked = openFile

		#Click derecho y agregar archivos
		listboxRight.when_right_button_pressed = Actions

		#Botones
		btnCopy = PushButton(btnBoxLeft, text="Copiar", align="left")
		btnCut = PushButton(btnBoxLeft, text="Mover", align="right")
		btnDelete = PushButton(btnBoxLeft, text="Eliminar", align="left")
		# btnPaste = PushButton(btnBoxLeft, text="Pegar", align="right")
		btnCreate = PushButton(btnBoxLeft, text="Crear", align="right", command=typeFile)

		#Botones
		btnCopy = PushButton(btnBoxRight, text="Copiar", align="left")
		btnCut = PushButton(btnBoxRight, text="Mover", align="right")
		btnDelete = PushButton(btnBoxRight, text="Eliminar", align="left")
		# btnPaste = PushButton(btnBoxRight, text="Pegar", align="right")
		btnCreate = PushButton(btnBoxRight, text="Crear", align= "right", command=typeFile)
		app.display()
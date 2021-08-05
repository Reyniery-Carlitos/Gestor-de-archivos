#-*- coding: utf-8 -*-

"""
@author: crrubio@unah.edu.hn
Version: 0.1.0
Date: 08/064/2021
"""

import os
from io import *
from Core.GraphDirected import *

class Create():
	def __init__(self):
		self.graph = GraphDirected()
		self.count = 0
	# Funcion para Crear nueva carpeta
	def createNewFolder(self, nombre):
		if self.graph.add(nombre) == True:
			newFolder = os.mkdir(nombre)
			self.graph.add(nombre)

		else:
			self.count += 1
			newFolderName = (f"{nombre}-copia"+str(self.count))
			newFolder = os.mkdir(newFolderName)
			self.graph.add(newFolderName)

		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))
		print("se imprimen la cantidad de vertices del graphDirected: {}".format(len(self.graph)))
	# Funcion para crear nuevo archivo
	def createNewFile(self, nombre):
		if self.graph.add(nombre) == True:
			newFile = open(nombre, "w")
			self.graph.add(nombre)
		else:
			self.count += 1
			newFileName = (f"{nombre}-copia"+str(self.count))
			newFile = open(newFileName, "w")
			self.graph.add(newFileName)

		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))		
		print("se imprimen la cantidad de vertices del graphDirected: {}".format(len(self.graph)))

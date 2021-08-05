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
		
	# Funcion para Crear nueva carpeta
	def createNewFolder(self, nombre):
		if self.graph.add(nombre) == 1:
			newFolder = os.mkdir(nombre)
			self.graph.add(nombre)
		
		else:
			print("Warning todo salio mal xD")
		
		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))
		print("se imprimen la cantidad de vertices del graphDirected: {}".format(len(self.graph)))
	# Funcion para crear nuevo archivo
	def createNewFile(self, nombre):
		newFile = open(nombre, "w")
		self.graph.add(nombre)
		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))		
		

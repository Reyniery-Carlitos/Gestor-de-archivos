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
		self.edges = GraphDirected()
		self.count = 0

	# Funcion para Crear nueva carpeta
	def createNewFolder(self, name="", edge=None):
		if self.graph.add(name) == True:
			self.graph.add(name)
			
			# Comprobar que si no existe un a edge, entonces la edge sera la root.
			if edge == None:
				newFolder = os.mkdir(name)
			
			# De lo contrario se crearan los archivos dentro de la arista que se le especifique.
			else:
				newFolder = os.mkdir(edge + "/" + name)
				self.edges.edge(edge, name)
		else:
			self.count += 1
			newFolderName = (f"{name}-copia"+str(self.count))
			newFolder = os.mkdir(newFolderName)
			self.graph.add(newFolderName)

		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))
		print("se imprimen la cantidad de vertices del graphDirected: {}".format(len(self.graph)))
	
	# Funcion para crear nuevo archivo
	def createNewFile(self, name=""):
		if self.graph.add(name) == True:
			newFile = open(name, "w")
			self.graph.add(name)

			# Comprobar que si no existe un a edge, entonces la edge sera la root.
			if edge == "":
				newFolder = os.mkdir(name)
		
			# De lo contrario se crearan los archivos dentro de la arista que se le especifique.
			else:
				newFile = open(edge + "/" + name, "w")
				self.edges.edge(name, edge)

		else:
			self.count += 1
			newFileName = (f"{name}-copia"+str(self.count))
			newFile = open(newFileName, "w")
			self.graph.add(newFileName)

		print("se imprimen los vertices del graphDirected: {}".format(self.graph.vertexs))		
		print("se imprimen la cantidad de vertices del graphDirected: {}".format(len(self.graph)))

#-*- coding:utf-8 -*-
"""
@author ojvallecillo@unah.hn
@version 0.1.0
@fecha 2021/08/03

"""
from Core.LinkedList import LinkedList 
class Vertex:
    def __init__(self,vertexId):
        self.vertexId=vertexId
        self.edges=LinkedList()

    def __str__(self):
        return "{}".format(self.vertexId)       
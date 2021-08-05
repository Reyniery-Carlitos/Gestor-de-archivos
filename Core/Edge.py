#-*- coding:utf-8 -*-
"""
@author ojvallecillo@unah.hn
@version 0.1.0
@fecha 2021/08/03

"""

class Edge:
    def __init__(self,vertexInitial,vertexEnd,weight=1):            
        self.vertexInitial=vertexInitial
        self.vertexEnd=vertexEnd
        self.weight=weight

    def __It__(self,other):
        return self.weigth<other.weight    

    def __str__(self):
        return "{}".format(self.vertexEnd)    
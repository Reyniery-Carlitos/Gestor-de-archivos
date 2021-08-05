#-*- coding:utf-8 -*-
"""
@author ojvallecillo@unah.hn
@version 0.1.0
@fecha 2021/08/03

"""

from Core.LinkedList import LinkedList
from Core.Vertex import Vertex
from Core.Edge import Edge

class GraphDirected:
    def __init__(self):
        self.vertexs = LinkedList()
        
    def comparrisonFun(self,node,vertexId):
        vertex = node.value
        # primero averiguamos si el valor es instancia de
        # Vertex o Edge
        #para realizar la comparacion correspondiente de cada caso
        if isinstance(vertex,Vertex):
            if vertex.vertexId==vertexId:
                return True

        elif isinstance(vertex,Edge): 
            if vertex.vertexEnd==vertexId:
                return True        
        return False   

    def add(self,vertexId):
        nwVertex = Vertex(vertexId)
        #verificamos si esta vacia la lista de vertices para insertar
        if not self.vertexs.first:
            self.vertexs.push(nwVertex)
            return 1

        #buscamos el nuevo vertice y si no existe lo insertamos 
        if not self.vertexs.search(vertexId,lambda a,b:self.comparrisonFun(a,b)):
            self.vertexs.push(nwVertex)
            return True
        else:
            return False

    def edge(self,vertexOriginId,vertexDestinationId,weight=1):          
        # primero obtenemos el vertice Origen que recibimos como parametro
        vertexOrigin=self.vertexs.get(vertexOriginId,lambda a,b:self.comparrisonFun(a,b))
        #obtenemos el Vertice Destino de la lista de vertices
        vertexDestination=self.vertexs.get(vertexDestinationId,lambda a,b:self.comparrisonFun(a,b))
        #verificamos si tienen aristas
        if not vertexOrigin.edges.first:
            vertexOrigin.edges.push(Edge(vertexOrigin,vertexDestination))
            vertexDestination.edges.push(Edge(vertexDestination,vertexOrigin))
            if weight!=1:
                #obtenemos la nueva arista para asiganarle el peso (en caso de que se nos asigne uno)
                nwEdge=vertexOrigin.edges.getE(vertexDestination,lambda a,b:self.comparrisonFunEdge(a,b))
                #le asignamos el nuevo peso
                nwEdge.weight=weight
            return True

        #buscamos en las aristas del vertice origen
        # si existe el vertice destino
        if (not vertexOrigin.edges.search(vertexDestinationId,lambda a,b:self.comparrisonFun(a,b))):
            
            vertexOrigin.edges.push(Edge(vertexOrigin,vertexDestination))
            #como es dirigido el grafo tambien se debe agregar el vertice 
            #origen a las aristas del vertice destino
            vertexDestination.edges.push(Edge(vertexDestination,vertexOrigin))
            if weight!=1:
                #obtenemos la nueva arista para asiganarle el peso (en caso de que se nos asigne uno)
                nwEdge=vertexOrigin.edges.getE(vertexDestination,lambda a,b:self.comparrisonFun(a,b))
                #le asignamos el nuevo peso
                nwEdge.weight=weight
            return True
        
    #imprime la version texto del grafo en forma de diccionario
    def __str__(self):
            result="\n{"
            current=self.vertexs.first
            while current:
                vertex=current.value
                edges=vertex.edges
                result+=" '{}': \n".format(vertex)
                if edges.first!=None:
                    edge=edges.first
                    result+="\t'{}':\n".format(edge.value)
                    if edge.value.weight>0:
                            result+="\tPeso:'{}'\n".format(edge.value.weight)
                    while edge.next:
                        result+="\t'{}':\n".format(edge.next.value)
                        if edge.value.weight>0:
                            result+="\tPeso:'{}'\n".format(edge.value.weight)
                        edge=edge.next

                current=current.next
            result+="} "
            return result 
        
    def __len__(self):
            return len(self.vertexs)           

        
        
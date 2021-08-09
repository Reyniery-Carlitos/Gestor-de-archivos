#-*- coding:utf-8 -*-
"""
@author ojvallecillo@unah.hn
@version 0.1.0
@fecha 2021/08/03

"""

from Core.LinkedList import LinkedList
from Core.Vertex import Vertex
from Core.Edge import Edge

class UndirectedGraph:
    
    def __init__(self):
        self.vertexs=LinkedList()
          
    def comparrisonFun(self,node,vertexId):
        vertex=node.value
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
        nwVertex=Vertex(vertexId)
        #verificamos si esta vacia la lista de vertices para insertar
        if not self.vertexs.first:
            self.vertexs.push(nwVertex)
            return True
        #buscamos el nuevo vertice y si no existe lo insertamos 
        if not self.searchVertex(vertexId,lambda a,b:self.comparrisonFun(a,b)):
            self.vertexs.push(nwVertex)
            return True
        
    def edge(self,vertexOriginId,vertexDestinationId,weight=1):        
       
        # primero obtenemos el vertice Origen que recibimos como parametro
        vertexOrigin=self.getVertex(vertexOriginId)
        #obtenemos el Vertice Destino de la lista de vertices
        vertexDestination=self.getVertex(vertexDestinationId)
        #verificamos si tienen aristas
        if not vertexOrigin.edges.first:
            vertexOrigin.edges.push(Edge(vertexOrigin,vertexDestination))
           
            return True

        #buscamos en las aristas del vertice origen
        # si existe el vertice destino
        if (not vertexOrigin.edges.search(vertexDestinationId,lambda a,b:self.comparrisonFun(a,b))):
            
            vertexOrigin.edges.push(Edge(vertexOrigin,vertexDestination))
           
            return True

    def deleteVertex(self,vertexObjetive):
        
        if self.searchVertex(vertexObjetive,lambda a,b:self.comparrisonFun(a,b)): 
            vertexObjetive=self.getVertex(vertexObjetive,lambda a,b:self.comparrisonFun(a,b))
            vertexDelete=self.vertexs.remove(vertexObjetive)
            return vertexDelete

    def deleteEdge(self,vertexOriginId,vertexDestinationId):
        #primero obtenemos los vertices atra vez del identificador
        vertexOrigin=self.vertexs.get(vertexOriginId,lambda a,b:self.comparrisonFun(a,b))
        vertexDestination=self.vertexs.get(vertexDestinationId,lambda a,b:self.comparrisonFun(a,b))
        #posicionamos el actual en la primera arista del vertice origen
        current=vertexOrigin.edges.first
        #una variable que usaremos mas adelante la declaramos
        prev=None
        #si no hay nadie en la primera arista no hace nada
        if current==None:
            return None
        #si la primera arista existe y es la que buscamos la eliminamos    
        elif current.value.vertexEnd==vertexDestination:
            vertexOrigin.edges.first.vertexEnd=current.next
            delete=vertexOrigin.edges.remove(current.value)
            delete1=vertexDestination.edges.remove(vertexOrigin)
            return delete,delete1
        else:
            #con este ciclo recorrestas
            while current.next:
                #esta variable nos sirve para guardar el anterioi
                prev=current
                #comparamos los vertices adyacentes haasta encontrar el buscamos
                if current.value.vertexEnd==vertexDestination:
                    #hacemos la conexion de la arista anterior con la siguiente
                    prev.next=current.next
                    #eliminamos la arista
                    vertexOrigin.edges.remove(current.value)
                    vertexDestination.edges.remove(vertexOrigin)
                    
                    return True
                current=current.next
        return False    
    
    def getVertex(self,objetiveName,comparrisonFun=None):
        return self.vertexs.get(objetiveName,lambda a,b:self.comparrisonFun(a,b))

    def searchVertex(self,objetiveName,comparrisonFun=None):
        return self.vertexs.search(objetiveName,lambda a,b:self.comparrisonFun(a,b))
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

        
        
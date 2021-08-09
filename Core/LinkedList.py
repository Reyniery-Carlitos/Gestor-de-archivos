#-*- coding:utf-8-*-
"""
@author ojvallecillo@unah.hn
@version 0.1.0
@fecha 2021/08/03

"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.first=None

    def push(self,value,index=-1):
            
        if not self.first:
            self.first=Node(value)
            return True
        
            
        count=0
        current=self.first

        
        if index==count:
                current.next=self.first
                self.first=current
                return True
        prev=self.first
        current=prev.next
        while current:
                count+=1
                index+=1
                if index==count:
                    prev.next=Node(value)
                    prev.next.next=current
                
                prev=current
                current=prev.next   
        prev.next=Node(value)
        return True     
            
           
            

    def search(self,vertexId,comparrissonFun=None):
        
        if not self.first:
            return False
        else:
            
            
            current=self.first
            while current:
                
                if comparrissonFun==None and current.value==vertexId:
                #si la funcion de comparacion es nula
                # y el valor actual en el recorrido
                # es el igual al vertexId retorna verdadero
                    return True
               
                elif comparrissonFun(current,vertexId):
                # si la funcion de comparacion retorna un verdadero
                #  quiere decir que el identificado es parte del vertice
                #  el vertice ya existe  
                    return True
                
                current=current.next

            return False
        

    def get(self,vertexId,comparrisonFun=None):
        
            if not self.first:
                return None
            else:
            
                
                current=self.first
                while current:
                    #si la funcion de comparacion es nula
                    # y el valor actual en el recorrido
                    # es el igual al vertexId retorna el vertex que en este caso es el value del nodo
                    if not comparrisonFun and current.value==vertexId:
                        return current.value
                    # si la funcion de comparacion retorna un true
                    #  quiere decir que el identificado es parte del vertice
                    #  por lo tanto devuelve el vertice 
                    elif  comparrisonFun(current,vertexId):
                        return current.value    
                
                    current=current.next

                return None
            
    def remove(self,objetive):
        if not self.first:
            return None
       
        current=self.first
        aux2=None
        while current.next:
            aux2=current
            if current.value==objetive:
                aux2.next=current.next
                return True
            current=current.next

        
        return None
               
            

    def __len__(self):
        return self.length()

    def length(self):
        if not self.first:
            return 0
        else:
            count=1
            current=self.first
            while current.next:
                count+=1

                current=current.next
            return count    

    def __str__(self):
            result= "["
            current=self.first
            while current:
                    result+="{}".format(current.value)
                    if current.next:
                        result+=", "
                    current=current.next

            result+="]"
            return result
    
    def __iter__(self):
        current=self.first
        while current:
            yield current.value
            current=current.next
        
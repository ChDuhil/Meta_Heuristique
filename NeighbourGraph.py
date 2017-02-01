'''
titre: NeighbourGraph
auteur: Christophe Duhil
date: janvier 2005
description:
la class NeighbourGraph cree un graphe de voisinage connexe, chaque noeud est valuee
la class NeighbourGraph  fonctionne avec les class random et Node
'''
import sys
import Node
from random import *

class NeighbourGraph:
    '''
    creation d un graphe de voisinage ou les noeuds sont valuee
    '''
    

    def __init__(self):
        '''
        initialisation
        '''
        self.numberOfEdge=0
        self.numberOfNodes=0
        self.node = []
        

    def addNode(self,nodeId,nodeValue):
        '''
        Ajoutte un noeud dans le graph
        '''
        self.node.append(Node.Node(nodeId,nodeValue))
        self.numberOfNodes = self.numberOfNodes + 1
        
    def addEdge(self,nodeA,nodeB):
        '''
        Ajoutte un arc entre deux noeuds
        retourne True si l operation est possible et False sinon
        '''
        
        nodeB.getNeighbourList().count(nodeA.getId())
        
        if (nodeA.checkNumNeighbour()and nodeB.checkNumNeighbour()and nodeB.getNeighbourList().count(nodeA.getId())==0):
            nodeA.addNeighbour(nodeB)
            nodeB.addNeighbour(nodeA)
            self.numberOfEdge=self.numberOfEdge+1
            return True
        else:
            return False


    
    def setGraphConnexe(self,numOfNode,numOfOpt,lowNodeValue, hightNodeValue):
        '''
        cree un graph connexe de numOfNode nombre de noeuds
        la valeure associee a chaque noeud suit une loi uniforme de parametres lowNodeValue et hightNodeValue
        '''

        self.addNode(0,randint(lowNodeValue,hightNodeValue))

        for n in range(1, (numOfNode)):
            self.addNode(n,randint(lowNodeValue,hightNodeValue))
            self.addEdge(self.node[n],self.node[n-1])

        self.addEdge(self.node[0],self.node[numOfNode-1])
        
        for n in range(1,numOfOpt+1):
            self.node[numOfNode*n/(numOfOpt+1)-(numOfNode*n/(numOfOpt+1))%1].setValue(1)
            
                             
        
    def setNumOfNeighbour(self,lowNum,hightNum):
        '''
        configure le nombre de voisin des noeuds, le nombre de voisins suit une loi uniforme de parametre (lowNum, hightNum)
        '''
        for n in range(len(self.node)):
            self.node[n].setNodeMaxNeighbour(randint(lowNum,hightNum))

    def setNeighbourhoodGraph(self):
        '''
        configure le graph de voisinage suivant le nombre de voisin de chaque Noeud
        '''
        
        for n in range(len(self.node)-1):
            m=0
            while self.node[n].checkNumNeighbour()and m<(len(self.node)):
                m=randint(n+1,len(self.node)-1)
                #if not self.addEdge(self.node[n],self.node[m]):
                while m<len(self.node)and not self.addEdge(self.node[n],self.node[m]):
                    m=m+1
            

    def see(self,low,hight):
        '''
        methode pour controler le nombre max de voisins d un noeud et la liste de voisin appartenent a ce noeud
        '''
        for n in range(low,hight+1):
            print self.node[n].getMaxNeighbour()
            print self.node[n].getNeighbourList()


    def getNodeNeighbourList(self,nodeIndex):
        '''
        retourne la liste des noeuds voisin du noeud en parametre
        '''
        return self.node[nodeIndex].getNeighbourList()

    

    def getNodeValue(self,nodeIndex):
        '''
        retourne la donnee du noeud en parametre
        '''
        return self.node[nodeIndex].getValue()

    def getNumberOfNodes(self):
        '''
        retourne le nombre de noeud du graph
        '''
        return self.numberOfNodes


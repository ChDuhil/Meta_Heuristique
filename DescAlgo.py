'''
titre : NeighbourGraph
auteur: Christophe Duhil
date : janvier 2005
description:
la class DescAlgo permet de trouver un optimum local par la methode de descente directe
'''

import NeighbourGraph
from random import *

class DescAlgo:
    '''
    algorithme de recherhe de mimimum local par la methode de descente directe
    '''

    def __init__(self):  
        '''
        initialization
        '''
        self.numOfIter = {}
        self.holyGrailValue = {}
        self.holyGrailIndex = {}
        self.grailWay = []

        
    def GrailQuest(self,graph):
        '''
        fonction de recherche de minimum
        '''
        # initialisation du nombre d iteration:
        self.numOfIter=0
        # tirage au sort du premier noeud:
        self.holyGrailIndex = randint(0,graph.getNumberOfNodes()-1)
        self.holyGrailValue = graph.getNodeValue(self.holyGrailIndex)
        # insertion du premier noeud dans la liste des noeuds parcourus:
        self.grailWay.append(self.holyGrailIndex)
        # initialisation de la condition d arret de la boucle while:
        holdValue=self.holyGrailValue+1
        
        while holdValue>self.holyGrailValue:
            self.numOfIter +=1
            holdValue = self.holyGrailValue
            l = graph.getNodeNeighbourList(self.holyGrailIndex)

            for n in range(len(l)):
            
                if graph.getNodeValue(l[n])<self.holyGrailValue:
                    self.holyGrailValue=graph.getNodeValue(l[n])
                    self.holyGrailIndex=l[n]
                    
            self.grailWay.append(l[n])

    def getHolyGrailIndex(self):
        '''
        retourne l indexe du noeud optimum
        '''
        return self.holyGrailIndex

    def getHolyGrailValue(self):
        '''
        retourne la valeur de l optimum local
        '''
        return self.holyGrailValue

    def getHolyGrailNeighbour(self,g):
        '''
        retourne la la liste des noeuds voisin du noeud optimum local
        '''
        return g.getNodeNeighbourList(self.holyGrailIndex)
                    
    def getNumOfIter(self):
        '''
        retourne le nombre d iteration effectuees pour atteindre l optimum
        ''' 
        return self.numOfIter

    def getGrailWay(self):
        '''
        retourne une liste contenant le chemun parcouru jusqu a l optimum
        '''
        return self.grailWay
    
    

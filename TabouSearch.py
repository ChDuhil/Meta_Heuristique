'''
titre : TabouSearch
auteur : Christophe duhil
Date : janvier 2005
description:
Recherche d optimum par algorithme de recheche tabou applique a un graph de voisinage.
'''
import NeighbourGraph
from random import *

class TabouSearch:
    '''
    recherche d optimum par algorithme de recherche tabou applique a un graphe de voisinage.
    '''
    def __init__(self):
        '''
        initialisation
        '''
        self.numOfIter = {}
        self.holyGrailValue = {}
        self.holyGrailIndex = {}
        self.grailWay = []
        self.tabouList = []
        
    def tabouSearch(self,graph,tabouListDim,iterMax):
        '''
        fonction de recherche tabou.
        '''
        # initialisation de la methode:
        self.tabouList = []
        iterTabou = 0
        self.numOfIter=0
        # tirage d une solution initiale:
        self.holyGrailIndex = randint(0,graph.getNumberOfNodes()-1)
        bestIndex = self.holyGrailIndex
        self.holyGrailValue = graph.getNodeValue(self.holyGrailIndex)
        self.grailWay.append(self.holyGrailIndex)
        
        # insertion de la sol initiale dans la liste tabou:
        self.tabouList.append(self.holyGrailIndex)
        nonTabouList = ["init"]

        while iterTabou <= iterMax and not len(nonTabouList)==0:
            self.numOfIter +=1

            # selection des n voisins non tabous:
            nonTabouList=[]
            nonTabouList=self.nonTabouList(graph.getNodeNeighbourList(bestIndex))

            
            #evaluation des n voisins non tabou et selection du meilleur voisin:
            bestNeighbourValue = graph.getNodeValue(nonTabouList[0])
            bestIndex = nonTabouList[0]
            for n in range(len(nonTabouList)): 
                if (graph.getNodeValue(nonTabouList[n])< bestNeighbourValue):
                    bestNeighbourValue=graph.getNodeValue(nonTabouList[n])
                    bestIndex=nonTabouList[n]
        
            #mise a jour de la liste tabou:
            if bestNeighbourValue<self.holyGrailValue:
                iterTabou = 0
                self.holyGrailValue=bestNeighbourValue
                self.appendTabouList(tabouListDim,bestIndex)
                self.holyGrailIndex = bestIndex
            else:
                iterTabou += 1
                self.appendTabouList(tabouListDim,bestIndex)
                
            
            #mise  a jour de liste chemin de recherche:        
            self.grailWay.append(bestIndex)

    def nonTabouList(self,neighbourList):
        '''
        retourne la liste des voisins non tabou
        '''
        nonTabouList = []
        for n in range (len(neighbourList)):
            if self.checkTabou(neighbourList[n]):
                nonTabouList.append(neighbourList[n])
        return nonTabouList
            
        



    def appendTabouList(self, range, value):
        '''
        ajoute un noeud dans la liste des noeuds tabous
        '''
        # si le nombre de noeuds est inf a range alors le noeud est ajoute
        if len(self.tabouList)<=range:
            self.tabouList.append(value)

        # si le nombre de noeuds est inf a range alors le noeud est ajoute et le noeud le plus vieux est suprime
        else :
            del self.tabouList[0]
            self.tabouList.append(value)
            
        
    def checkTabou(self,value):
        '''
        controle la presence d une valeur dans la liste tabou
        retourne True si l element est abscent
        retourne False si l element est present
        '''
        if self.tabouList.count(value)==0:
            return True
        else:
            return False
        
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

    def getGrailWayValue(self,graph):
        '''
        retourne une liste contenant les valeurs des noeuds parcourus jusqu a l optimum
        '''
        l=[]
        for n in self.grailWay:
            l.append(graph.getNodeValue(n))
        return l
    
            

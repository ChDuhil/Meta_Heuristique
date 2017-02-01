''' generation d'un graph
creation le 8 octobre 2004
auteur : christophe Duhil

modifie le 10 novembre 2004 pour ajouter la methode setGraphConnexe

version : 1.10
'''

class GraphGenerator(Graph()):
    '''la classe GraphGenerator cree un graph de voisinage celon
    des parametres choisis par l'utilisateur'''


    # Import des fonctions de probabilites
    from random import *

    def __init__(self):
        '''
        initialisation
        '''
        self.g.__init__(self)

    def __rep__(self):
        '''
        User friendly representation
	'''
        self.g.__rep__(self)

    def add_edge(self, head_id, tail_id):
        self.g.add_edge(self, head_id, tail_id)

    # methode uniformNodeList retourne une liste de valeur suivant une loi uniforme
    def uniformNodeList(self,nbr,low,hight):
        uniformList=[]
        for n in range(nbr):
            nodeList = nodeList+[randrange(low,hight)]
        return nodeList

    # methode normalNodeListe
    def normalNodeList(nbr,low,hight):
        normalList=[]
        mu =(low+hight)/2
        sigma =(low-mu)/1,96
        for n in range(nbr):
            tps = normalvariate(mu,sigma)
            normalList = normalList+[int(tps-tps%1)]
        return normalList


    # la methode cree un graphe connexe de longueur nodeRange.
    def setGraphConnexe(self, nodeRange):
        m=1
        k=2
        for n in range(nodeRange-1):
            self.g.add_edge(m,k)
            m=m+1
            k=k+1
        
    
    # def setRandomEdege(lowRange, hightRange):
        
        
        
        
        
            

    
    
    

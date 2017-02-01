'''
generation de graphe de voisinage
creation le 18 novembre 2004
auteur christophe Duhil

version:0
'''
class NewGraph:
    '''
    Generation de graphe de voisinage
    '''

    from graphlib import Graph

    def __init__(self):
        '''
        initialisation
        '''
        self.g = Graph.Graph()

        

    def setGraphConnexe(self, nodeRange):
        '''
        la methode cree un graphe connexe de longueur nodeRange.
        '''
        m=1
        k=2
        for n in range(nodeRange-1):
            self.g.add_edge(m,k)
            m=m+1
            k=k+1
        
   
    def setGraph(self, low, hight):
        '''
        creation des arcs suivant une loi uniforme
        '''
        

    def setValue(self, low, hight):
        '''
        attribue suivant une loi uniforme les valeurs des noeuds
        '''
        
        

from time import *
import sys
import NeighbourGraph
import DescAlgo
import TabouSearch
import SimulatedAnnealing
import DescPlus

de = time()

for n in range(500):
    #Creation du graph:

    global g
    g = NeighbourGraph.NeighbourGraph()



    '''
    creation du graph connexe
    le premier nombre represente le nombre de noeud
    le deuxieme, represente le nombre d optimum
    le troisieme, represente la valeur min du noeud
    le quatrieme, represente la valeure max du noeud
    '''
    g.setGraphConnexe(360000,5,20,400)


    '''
    Configuration du nombre de voisins:
    le premier nombre represente la valeur min d arc associe au noeud
    le second, represente la valeur max associe au noeud
    '''
    g.setNumOfNeighbour(5,10)


    #Creation des arcs de voisinage:
    g.setNeighbourhoodGraph()

    td = time()
    global d
    d = DescAlgo.DescAlgo()
    d.GrailQuest(g)

    d1 = d.getHolyGrailValue()
    d2 = d.getNumOfIter()
    tf = time()
    d3 = tf-td

    td =time()
    global p
    p = DescPlus.DescPlus()
    p.descPlus(g)

    p1= p.getHolyGrailValue()
    p2= p.getNumOfIter()
    p3= tf-td
    
    td = time()
    global t
    t= TabouSearch.TabouSearch()
    t.tabouSearch(g,7,50)

    t1 = t.getHolyGrailValue()
    t2 = t.getNumOfIter()
    tf = time()
    t3 = tf-td

    td = time()
    global s
    s = SimulatedAnnealing.SimulatedAnnealing()
    s.simulatedAnnealing(g)

    s1 = s.getHolyGrailValue()
    s2 = s.getNumOfIter()
    tf = time()
    s3 = tf -td

    log = open('logEXP1.csv','a')
    print >> log,d1,",",d2,",",d3,",",p1,",",p2,",",p3,",",t1,",",t2,",",t3,",",s1,",",s2,",",s3,'\n'
    print n 
    print time()-de

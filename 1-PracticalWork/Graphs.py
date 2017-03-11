#  graf neorientat -> graf neorientat cost -> graf orientat -> graf orientat cost

from .UI import *
class graphException(Exception):
    def __init__(self, msg):
        self._message = msg

    def __str__(self):
        return self._message


#Mother Class
class UnorientedGraph():
    def __init__(self, n):
        '''
        Creates an undirected graph with n vertices (noduri) - numbered from 0 to n-1
        :param n: integer, number of vertices
        '''
        self.dictOut = {}

        for i in range(n):
            self.dictOut[i] = []

    def parseNodeOut(self, node):
        '''
        :param node: integer
        :return: a list with all the successors of the node
        '''
        return self.dictOut[node]

    def isEdge(self, x, y):
        '''
        :param x: integer
        :param y: integer
        :return:  True if the edge (x,y) exists, False othersie
        '''
        return y in self.dictOut[x]

    def addEdge(self, x, y):
        '''
        Adds the edge (x,y)
        :param x: integer
        :param y: integer
        '''
        if self.isEdge(x, y):
            raise graphException("Edge already exists")

        self.dictOut[x].append(y)
        self.dictOut[y].append(x)

    def getNumberOfVertices(self):
        '''
        :return: The number of vertices in the graph
        '''
        return len(self.dictOut)

    def getOutDegree(self, x):
        '''
        :param x: vertice
        :return: the out degree of that vertice
        '''
        return len(self.dictOut[x])


class OrientedGraph(UnorientedGraph):
    def __init__(self, n):
        '''
            Creates a directed graph with n vertices (noduri) - numbered from 0 to n-1
            :param n: integer, number of vertices
        '''
        super(UnorientedGraph, self).__init__(n)

        self.dictIn = {}

        for i in range(n):
            self.dictOut[i] = []

    def addEdge(self, x, y):
        if self.isEdge(x, y):
            raise graphException("Edge already exists")

        self.dictOut[x].append(y)
        self.dictIn[y].append(x)

    def parseNodeIn(self, node):
        return self.dictIn[node]

    def getInDegree(self, x):
        '''
        :param x: vertice
        :return: the in degree of that vertice
        '''
        return len(self.dictIn[x])

class UnorientedCostGraph(UnorientedGraph):
    def __init__(self, n):
        '''
        Creates an undirected cost graph with n vertices (noduri) - numbered from 0 to n-1
        :param n: integer, number of vertices
        '''
        super(UnorientedCostGraph, self).__init__(n)
        self.dictCost = {}

    def addEdge(self, x, y, cost):
        super(UnorientedGraph, self).addEdge(x, y)
        self.dictCost[(x,y)] = cost
        self.dictCost[(y,x)] = cost

class OrientedCostGraph(OrientedGraph):
    def __init__(self, n):
        '''
            Creates an directed cost graph with n vertices (noduri) - numbered from 0 to n-1
            :param n: integer, number of vertices
        '''
        super(OrientedGraph, self).__init__(n)
        self.dictCost = {}

    def addEdge(self, x, y, cost):
        super(OrientedGraph, self).addEdge(x, y)
        self.dictCost[(x,y)] = cost




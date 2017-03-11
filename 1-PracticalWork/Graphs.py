#  graf neorientat -> graf neorientat cost -> graf orientat -> graf orientat cost

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
        self._edges = n
        self.dictOut = {}

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

        #check if the edges actually exist
        if not x in self.dictOut.keys() or not y in self.dictOut.keys():
            return False

        return y in self.dictOut[x]

    def addEdge(self, x, y):
        '''
        Adds the edge (x,y)
        :param x: integer
        :param y: integer
        '''
        #If the vertex is not create it, do it now
        self.addVertex(x)
        self.addVertex(y)

        if self.isEdge(x, y):
            raise graphException("Edge already exists")

        self.dictOut[x].append(y)
        self.dictOut[y].append(x)

    def addVertex(self, x):
        if not x in self.dictOut.keys():
            self.dictOut[x] = []

    def getNumberOfVertices(self):
        '''
        :return: The number of vertices in the graph
        '''
        return len(self.dictOut)

    def getNumberOfEdges(self):
        '''
        :return: number of edges
        '''
        return self._edges

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
        super().__init__(n)

        self.dictIn = {}


    def addEdge(self, x, y):
        # If the vertex is not create it, do it now
        self.addVertex(x)
        self.addVertex(y)

        if self.isEdge(x, y):
            raise graphException("Edge already exists")

        self.dictOut[x].append(y)
        self.dictIn[y].append(x)


    def addVertex(self, x):
        super().addVertex(x)

        if not x in self.dictIn.keys():
            self.dictIn[x] = []

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
        super().addEdge(x, y)
        self.dictCost[(x,y)] = cost
        self.dictCost[(y,x)] = cost

    def getCost(self, x, y):
        return self.dictCost[(x,y)]

class OrientedCostGraph(OrientedGraph):
    def __init__(self, n):
        '''
            Creates an directed cost graph with n vertices (noduri) - numbered from 0 to n-1
            :param n: integer, number of vertices
        '''
        super().__init__(n)
        self.dictCost = {}

    def addEdge(self, x, y, cost):
        super().addEdge(x, y)
        self.dictCost[(x,y)] = cost

    def getCost(self, x, y):
        return self.dictCost[(x,y)]

    def __str__(self):
        res = ''

        res += str(self.getNumberOfEdges()) + ' ' + str(self.getNumberOfVertices()) + '\n'
        for i in range(1, self.getNumberOfEdges() + 1):
            # If a node is isolated
            if len(self.parseNodeOut(i)) == 0 and (len(self.parseNodeIn(i))) == 0:
                res += str(i) + ' -1\n'
                continue

            for j in self.parseNodeOut(i):
                res += str(i) + ' ' + str(j) + ' ' + str(self.getCost(i, j)) + '\n'

        return res




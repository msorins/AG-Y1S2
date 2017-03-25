#  graf neorientat -> graf neorientat cost -> graf orientat -> graf orientat cost
import copy

class graphException(Exception):
    def __init__(self, msg):
        self._message = msg

    def __str__(self):
        return self._message


#Mother Class
class UndirectedGraph():
    def __init__(self, file):
        '''
        Creates an undirected graph with n vertices (noduri) - numbered from 0 to n-1
        :param n: integer, number of vertices
        '''
        #self._edges = n
        self._file = file
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
            print(x, y)
            raise graphException("Edge already exists")

        self.dictOut[x].append(y)
        self.dictOut[y].append(x)

    def addVertex(self, x):
        if not x in self.dictOut.keys():
            self.dictOut[x] = []

    def getNumberOfVertices(self):
        '''
        :return: The number of vertices in the graph (NODURI)
        '''
        self._edges = len(self.dictOut)
        return self._edges

    def getNumberOfEdges(self):
        '''
        :return: number of edges (MUCHII)
        '''
        nr = 0
        for key in self.dictOut:
            nr += len(self.dictOut[key])
        return nr


    def getOutDegree(self, x):
        '''
        :param x: vertice
        :return: the out degree of that vertice
        '''
        return len(self.dictOut[x])

    def removeEdge(self, x, y):
        '''
        :param x: vertex
        :param y: vertex
        :return: removes that edge
        '''
        if not self.isEdge(x, y):
            raise graphException("Edge does not exist")

        self.dictOut[x].remove(y)
        self.dictOut[y].remove(x)

    def removeVertex(self, x):
        '''
        Removes vertex x
        :param x: vertex
        '''

        if not x in self.dictOut.keys():
            raise graphException("Vertex does not exist")

        auxLst = copy.deepcopy(self.dictOut[x])
        for crt in auxLst:
            self.removeEdge(x, crt)

        #Actually delete that node
        del self.dictOut[x]

    def getGraph(self):
        '''
        :return: all the graph
        '''
        return self.dictOut

    def read(self):
        nrLine = 0

        with open(self._file) as file:
            for line in file:
                nrLine += 1
                line = line.split()

                if nrLine == 1:
                    n = int(line[0])
                    m = int(line[1])
                    self.dictOut = {}
                else:
                    x = int(line[0])
                    y = int(line[1])
                    if y != -1:
                        # Normal edge (between two vertices)
                        self.addEdge(x, y)
                    else:
                        # Just one isolated vertex
                        self.addVertex(x)
        self.save()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        open(self._file, 'w').write(str(self))

    def __str__(self):
        res = ''
        nr = self.getNumberOfEdges() // 2
        res += str(self.getNumberOfVertices()) + ' ' + str(nr) + '\n'
        for node in self.dictOut:
            # If a node is isolated
            if len(self.parseNodeOut(node)) == 0:
                res += str(node) + ' -1\n'
                continue

            for j in self.parseNodeOut(node):
                if node < j:
                    res += str(node) + ' ' + str(j) + ' \n'

        return res

class DirectedGraph(UndirectedGraph):
    def __init__(self, file):
        '''
            Creates a directed graph with n vertices (noduri) - numbered from 0 to n-1
            :param n: integer, number of vertices
        '''
        super().__init__(file)

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

    def removeEdge(self, x, y):
        '''
        :param x: vertex
        :param y: vertex
        :return: removes that edge
        '''
        if not self.isEdge(x, y):
            raise graphException("Edge does not exist")

        self.dictOut[x].remove(y)
        self.dictIn[y].remove(x)

    def removeVertex(self, x):
        '''
            Removes vertex x
            :param x: vertex
        '''

        if not x in self.dictOut.keys():
            raise graphException("Vertex does not exist")

        #Go through the dictOut and delete all the edges
        auxLst = copy.deepcopy(self.dictOut[x])
        for crt in auxLst:
            self.removeEdge(x, crt)

        # Go through the dictIn and delete all the edges
        auxLst = copy.deepcopy(self.dictIn[x])
        for crt in auxLst:
            self.removeEdge(crt, x)

        # Actually delete that node
        del self.dictOut[x]

    def read(self):
        nrLine = 0

        with open(self._file) as file:
            for line in file:
                nrLine += 1
                line = line.split()

                if nrLine == 1:
                    n = int(line[0])
                    m = int(line[1])
                    self.dictOut = {}
                    self.dictIn = {}
                else:
                    x = int(line[0])
                    y = int(line[1])
                    if y != -1:
                        # Normal edge (between two vertices)
                        self.addEdge(x, y)
                    else:
                        # Just one isolated vertex
                        self.addVertex(x)
        self.save()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        open(self._file, 'w').write(str(self))

    def __str__(self):
        res = ''
        nr = self.getNumberOfEdges()
        res += str(self.getNumberOfVertices()) + ' ' + str(nr) + '\n'
        for node in self.dictOut:
            # If a node is isolated
            if len(self.parseNodeOut(node)) == 0:
                res += str(node) + ' -1\n'
                continue

            for j in self.parseNodeOut(node):
                    res += str(node) + ' ' + str(j) + ' \n'

        return res

class UndirectedCostGraph(UndirectedGraph):
    def __init__(self, file):
        '''
        Creates an undirected cost graph with n vertices (noduri) - numbered from 0 to n-1
        :param n: integer, number of vertices
        '''
        super(UndirectedCostGraph, self).__init__(file)
        self.dictCost = {}

    def addEdge(self, x, y, cost):
        super().addEdge(x, y)
        self.dictCost[(x,y)] = cost
        self.dictCost[(y,x)] = cost

    def getCost(self, x, y):
        return self.dictCost[(x,y)]

    def read(self):
        nrLine = 0

        with open(self._file) as file:
            for line in file:
                nrLine += 1
                line = line.split()

                if nrLine == 1:
                    n = int(line[0])
                    m = int(line[1])
                    self.dictOut = {}
                    self.dictOut = {}
                else:
                    x = int(line[0])
                    y = int(line[1])
                    if y != -1:
                        # Normal edge (between two vertices)
                        z = int(line[2])
                        self.addEdge(x, y, z)
                    else:
                        # Just one isolated vertex
                        self.addVertex(x)
        self.save()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        open(self._file, 'w').write(str(self))

class DirectedCostGraph(DirectedGraph):
    def __init__(self, file):
        '''
            Creates an directed cost graph with n vertices (noduri) - numbered from 0 to n-1
            :param n: integer, number of vertices
        '''
        super().__init__(file)
        self.dictCost = {}

    def addEdge(self, x, y, cost):
        super().addEdge(x, y)
        self.dictCost[(x,y)] = cost

    def getCost(self, x, y):
        return self.dictCost[(x,y)]

    def changeCost(self, x, y, cost):
        if not self.isEdge(x, y):
            raise graphException("Edge does not exist")

        self.dictCost[(x,y)] = cost

    def __str__(self):
        res = ''

        res += str(self.getNumberOfVertices()) + ' ' + str(self.getNumberOfEdges()) + '\n'
        for node in self.dictOut:
            # If a node is isolated
            if len(self.parseNodeOut(node)) == 0 and (len(self.parseNodeIn(node))) == 0:
                res += str(node) + ' -1\n'
                continue

            for j in self.parseNodeOut(node):
                res += str(node) + ' ' + str(j) + ' ' + str(self.getCost(node, j)) + '\n'

        return res

    def read(self):
        nrLine = 0

        with open(self._file) as file:
            for line in file:
                nrLine += 1
                line = line.split()

                if nrLine == 1:
                    n = int(line[0])
                    m = int(line[1])
                    self.dictIn = {}
                    self.dictOut = {}
                    self.dictCost = {}
                else:
                    x = int(line[0])
                    y = int(line[1])
                    if y != -1:
                        # Normal edge (between two vertices)
                        z = int(line[2])
                        self.addEdge(x, y, z)
                    else:
                        # Just one isolated vertex
                        self.addVertex(x)
        self.save()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        open(self._file, 'w').write(str(self))




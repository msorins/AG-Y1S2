from Graphs import DirectedCostGraph
from Graphs import DirectedGraph
from Graphs import graphException

class PracticalWork3():
    def __init__(self):
        '''
        Init function
        '''
        self._graph = DirectedCostGraph("PracticalWork3.txt")
        self._graph.read()
        self._inf = 9999999

    def FloydWarshall(self, x, y):
        '''
        :param x: vertex
        :param y: vertex
        :return: the minimum cost from vertex x to y
        '''

        #Get the list of vertexes
        vertices = self._graph.getVertices()

        #Get the maximum vertex index (in case that there are some vertices missing)
        maxVertexIndex = -1
        for vertex in vertices:
            maxVertexIndex = max(maxVertexIndex, vertex)

        #declare the cost MATRIX
        cost = [[self._inf for x in range(maxVertexIndex + 5)] for y in range(maxVertexIndex + 5)]

        #fill the values for the existing edges
        for i in self._graph.getVertices():
            for j in self._graph.parseNodeOut(i):
                cost[i][j] = self._graph.getCost(i, j)


        #now the actual algorithm
        for i in vertices:
            for j in vertices:
                for k in vertices:
                    if i != j and cost[i][k] != self._inf and cost[k][j] != self._inf:
                        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

        return cost[x][y]



class Bonus1():
    def __init__(self):
        '''
        Init function
        '''
        self._graph = DirectedCostGraph("PracticalWork3-Bonus1.txt")
        self._graph.read()
        self._inf = 9999999


    def NrOfDistinctMinimumWalks(self, x, y):
        '''
        :param x: vertex
        :param y: vertex
        :return: the number of distinct minimum walks between two vertices
        '''
        res = 0
        minCost = self._inf + 1

        #Initial cost values are INFINITE
        cost = {}
        for node in self._graph.getGraph():
            cost[node] = self._inf


        #Prepare the DFS
        cost[x] = 0
        queue = []
        queue.append(x)

        #The algorithm is here
        while len(queue):
            crtVertex = queue[0]
            queue.pop(0)

            for nextVertex in self._graph.parseNodeOut(crtVertex):

                if nextVertex == y:
                    if minCost == cost[crtVertex] + self._graph.getCost(crtVertex, nextVertex):
                        res += 1
                    if minCost > cost[crtVertex] + self._graph.getCost(crtVertex, nextVertex):
                        minCost = cost[crtVertex] + self._graph.getCost(crtVertex, nextVertex)
                        res = 1

                if cost[nextVertex] >= cost[crtVertex] + self._graph.getCost(crtVertex, nextVertex):
                    cost[nextVertex] = cost[crtVertex] + self._graph.getCost(crtVertex, nextVertex)
                    queue.append(nextVertex)

        return res

class Bonus2():
    def __init__(self):
        '''
        Init function
        '''
        self._graph = DirectedGraph("PracticalWork3-Bonus2.txt")
        self._graph.read()
        self._inf = 9999999


    def NrOfDistinctWalks(self, x, y):
        '''
        :param x: vertex
        :param y: vertex
        :return: the number of distinct minimum walks between two vertices
        '''
        res = 0
        minCost = self._inf + 1

        #Initial cost values are INFINITE
        cost = {}
        for node in self._graph.getGraph():
            cost[node] = self._inf


        #Prepare the DFS
        cost[x] = 0
        queue = []
        queue.append(x)

        #The algorithm is here
        while len(queue):
            crtVertex = queue[0]
            queue.pop(0)

            for nextVertex in self._graph.parseNodeOut(crtVertex):

                if nextVertex == y:
                    if minCost == cost[crtVertex] + 1:
                        res += 1
                    if minCost > cost[crtVertex] + 1:
                        minCost = cost[crtVertex] + 1
                        res = 1

                if cost[nextVertex] >= cost[crtVertex] + 1:
                    cost[nextVertex] = cost[crtVertex] + 1
                    queue.append(nextVertex)

        return res



class UiPracticalWork3():
    def __init__(self):
        while True:
            try:
                self.menu()
                self.parseCommands()
            except graphException as e:
                print(e)

    def menu(self):
        msg = '\n\n#########################################\n'
        msg += '1. Lowest cost walk between the given vertices (directed graph with costs)\n'
        msg += '2. Number of distinct MINIMUM walks between two vertices (directed graph with costs) \n'
        msg += '3. Number of distinct walks between two vertices (directed graph)  \n'
        msg += '######################################### \n \n'

        print(msg)

    def parseCommands(self):
        cmd = int(input("Command: "))

        if cmd == 1:
            PracticalWork3Obj = PracticalWork3()
            print("The lowest cost walk is: ", PracticalWork3Obj.FloydWarshall(int(input("First vertex: ")), int(input("Second vertex: "))))
        elif cmd == 2:
            Bonus1Obj = Bonus1()
            print("The number of MINIMUM distinct walks is: ", Bonus1Obj.NrOfDistinctMinimumWalks(int(input("First vertex: ")), int(input("Second vertex: "))))
        elif cmd == 3:
            Bonus2Obj = Bonus2()
            print("The number of distinct walks is: ", Bonus2Obj.NrOfDistinctWalks(int(input("First vertex: ")), int(input("Second vertex: "))))


Ui = UiPracticalWork3()
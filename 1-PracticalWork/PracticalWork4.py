from Graphs import DirectedCostGraph
from Graphs import graphException

class strct():
    def __init__(self, x, y, cost):
        self._x = x
        self._y = y
        self._cost = cost

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getCost(self):
        return self._cost


class PracticalWork4():
    def __init__(self):
        '''
        Init function
        '''
        self._graph = DirectedCostGraph("PracticalWork4.txt")
        self._graph.read()
        self._inf = 9999999

    def group(self, grDict, nr):
        if grDict[nr] == nr:
            return nr

        grDict[nr] = self.group(grDict, grDict[nr])

        return grDict[nr]

    def reunite(self, grDict, a, b):
        grDict[ self.group(grDict, a) ] = self.group(grDict, b)

    def Kruskal(self):
        '''
        :param x: vertex
        :param y: vertex
        :return: the minimum cost from vertex x to y
        '''

        lst = []
        gr = {}
        rasp = []

        #Get the list of vertexes
        vertices = self._graph.getVertices()

        #Transform the structure
        for vertex in vertices:
            for vertexNext in self._graph.parseNodeOut(vertex):
                lst.append(strct(vertex, vertexNext, self._graph.getCost(vertex, vertexNext)))
            gr[vertex] = vertex

        #Sort the edges structure
        lst = sorted(lst, key=lambda x: x.getCost())

        #fill the values for the existing edges
        for i in range(len(lst)):
            if self.group(gr, lst[i].getX()) != self.group(gr, lst[i].getY()):
                self.reunite(gr, lst[i].getX(), lst[i].getY() )
                rasp.append(lst[i])

        print("The minimum spanning tree is the following one: ")
        for crt in rasp:
            print( str(crt.getX()) + " - " + str(crt.getY()) )

class UiPracticalWork4():
    def __init__(self):
        while True:
            try:
                self.menu()
                self.parseCommands()
            except graphException as e:
                print(e)

    def menu(self):
        msg = '\n\n#########################################\n'
        msg += '1. Construct minimum spanning tree (Kruskal)\n'
        msg += '######################################### \n \n'

        print(msg)

    def parseCommands(self):
        cmd = int(input("Command: "))

        if cmd == 1:
            PracticalWork4Obj = PracticalWork4()
            PracticalWork4Obj.Kruskal()


Ui = UiPracticalWork4()
from Graphs import DirectedCostGraph
from Graphs import graphException

class  Ui():
    def __init__(self):
        self._graph = DirectedCostGraph("graph.txt")
        self._graph.read()


        while True:
            try:
                self.menu()
                self.parseCommands()
            except graphException as e:
                print(e)



    def menu(self):
        msg = '\n\n#########################################\n'
        msg += '0. Print graph \n'
        msg += '1. Load graph from file (graph.txt) \n'
        msg += '2. Save graph to file (graph.txt) \n'
        msg += '3. Add edge (muchie) \n'
        msg += '4. Add vertex (nod) \n'
        msg += '5. Remove edge (muchie) \n'
        msg += '6. Remove vertex (nod) \n'
        msg += '7. Get number of Vertices \n'
        msg += '8. Get number of EDGES \n'
        msg += '9. Get cost of EDGE \n'
        msg += '10. Check if edge exists (between two vertices) \n'
        msg += '11. In & Out degree of an edge \n'
        msg += '12. Outbound edges of a vertex \n'
        msg += '13. Inbound edges of a vertex \n'
        msg += '14. Modify edge information (integer) \n'
        msg += '######################################### \n \n'

        print(msg)

    def read(self):
        self._graph.read()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        self._graph.save()

    def parseCommands(self):
        cmd = int(input("Command: "))

        if cmd == 0:
            print(self._graph)
        elif cmd == 1:
            self.read()
        elif cmd == 2:
            self.save()
        elif cmd == 3:
            self.addEdge()
        elif cmd == 4:
            self.addVertex()
        elif cmd == 5:
            self.removeEdge()
        elif cmd == 6:
            self.removeVertex()
        elif cmd == 7:
            self.getNumberOfVertices()
        elif cmd == 8:
            self.getNumberOfEdges()
        elif cmd == 9:
            self.getCostOfEdge()
        elif cmd == 10:
            self.doesEdgeExist()
        elif cmd == 11:
            self.getInOutDegree()
        elif cmd == 12:
            self.outboundOfVertex()
        elif cmd == 13:
            self.inboundOfVertex()
        elif cmd == 14:
            self.modifyEdgeCost()


    def addEdge(self):
        '''
        Reads and adds an edge to the graph
        '''
        x = int(input("First vertex: "))
        y = int(input("Second vertex: "))
        z = int(input("Cost: "))

        self._graph.addEdge(x, y, z)

    def addVertex(self):
        '''
        Reads and adds a vertex to the graph
        '''
        x = int(input("Vertex: "))
        self._graph.addVertex(x)

    def removeEdge(self):
        x = int(input("First vertex: "))
        y = int(input("Second vertex: "))

        self._graph.removeEdge(x, y)

    def removeVertex(self):
        x = int(input("Vertex: "))
        self._graph.removeVertex(x)

    def getNumberOfVertices(self):
        print("Nr. of vertices: " + str(self._graph.getNumberOfVertices()))

    def getNumberOfEdges(self):
        print("Nr. of edges: " + str(self._graph.getNumberOfEdges()))

    def getCostOfEdge(self):
        x = int(input("First vertex: "))
        y = int(input("Second vertex: "))

        print("Cost of edge: ", self._graph.getCost(x, y))

    def doesEdgeExist(self):
        x = int(input("First vertex: "))
        y = int(input("Second vertex: "))

        if self._graph.isEdge(x, y):
            print("The edge exists")
        else:
            print("The edge does not exists")

    def getInOutDegree(self):
        x = int(input("Vertex: "))

        print("In degree is " + str(self._graph.getInDegree(x)) + "\n")
        print("Out degree is " + str(self._graph.getOutDegree(x)) + "\n")

    def outboundOfVertex(self):
        x = int(input("Vertex: "))

        print(self._graph.parseNodeOut(x))

    def inboundOfVertex(self):
        x = int(input("Vertex: "))

        print(self._graph.parseNodeIn(x))

    def modifyEdgeCost(self):
        x = int(input("First vertex: "))
        y = int(input("Second vertex: "))
        cost = int(input("Cost: "))

        self._graph.changeCost(x, y, cost)



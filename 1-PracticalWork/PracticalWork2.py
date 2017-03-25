from Graphs import UndirectedGraph

class PracticalWork2():
    def __init__(self):
        self._graph = UndirectedGraph()

    def getNodesByDFS(self):
        used = []
        for node in self._graph.getGraph():
            print(node + "\n")




PracticalWork2Obj = PracticalWork2()
PracticalWork2Obj.getNodesByDFS()
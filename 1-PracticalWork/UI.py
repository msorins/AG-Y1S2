from Graphs import OrientedCostGraph
class  Ui():
    def __init__(self):
        self.read()

        while True:
            self.menu()



    def menu(self):
        msg = '1. Load graph from file (graph.txt)'
        msg += '2. Save graph to file (graph.txt)'
        msg += '3. Add edge (muchie)'
        msg += '4. Add vertex (nod)'
        msg += '5. Remove edge (muchie)'
        msg += '6. Remove vertex (nod)'
        msg += '7. Get Number of Vertices'
        msg += '8. Check if edge exists (between two vertices'
        msg += '9. In & Out degree of an edge'
        msg += '10. Iterate through outbound edges of a vertex'
        msg += '11. Iterate through inbound edges of a vertex'
        msg += '12. Modify edge information (integer)'
        msg += '#########################################'

    def read(self):
        nrLine = 0

        with open('graph.txt') as file:
            for line in file:
                nrLine += 1
                line = line.split()

                if nrLine == 1:
                    n = int(line[0])
                    m = int(line[1])
                    self._graph = OrientedCostGraph(n)
                else:
                    x = int(line[0])
                    y = int(line[1])
                    if y != -1:
                        # Normal edge (between two vertices)
                        z = int(line[2])
                        self._graph.addEdge(x, y, z)
                    else:
                        # Just one isolated vertex
                        self._graph.addVertex(x)
        self.save()

    def save(self):
        '''
        Writes current graph to disk file (aka saves it)
        '''
        open('graph.txt', 'w').write(str(self._graph))

    def parseCommands(self):
        cmd = int(input("Command: "))


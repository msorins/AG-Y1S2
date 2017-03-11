from .Graphs import *

class Ui():
    def __init__(self, graph):
        self._graph = graph
        self.menu()


    def menu(self):
        msg = '1. Load graph from file (graph.txt)'
        msg += '2. Save graph to file (graph.txt)'
        msg += '3. Get Number of Vertices'
        msg += '4. Check if edge exists (between two vertices'
        msg += '5. In & Out degree of an edge'
        msg += '6. Iterate through outbound edges of a vertex'
        msg += '7. Iterate through inbound edges of a vertex'
        msg += '8. Modify edge information (integer)'

    def read(self):

        with open('graph.txt') as file:
            for line in file:
               line = line.split()
               x = line[0]
               y = line[1]
               z = line[2]


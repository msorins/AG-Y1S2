from Graphs import DirectedCostGraph
from Graphs import graphException



class PracticalWork5():
    def __init__(self):
        '''
        Init function
        '''
        self._graph = DirectedCostGraph("PracticalWork5.txt")
        self._graph.read()
        self._inf = 9999999

    def MinimumCostHamiltonian(self):

        dp = [[0 for x in range(self._graph.getNumberOfVertices() +2 )] for y in range(1 <<self._graph.getNumberOfVertices() + 2)]


        #Initial values ar infinite
        for i in range( 1 << self._graph.getNumberOfVertices() ):
            for j in self._graph.getVertices():
                dp[i][j] = self._inf

        x = self._graph.getVertices()
        x = x[0]

        dp[1][x]=0
        #Do the computation
        for i in range(1,  1 << self._graph.getNumberOfVertices() ):
            for j in self._graph.getVertices():
                if i & (1 << j):
                    for k in self._graph.parseNodeIn(j):
                        if i & (1 << k):
                            dp[i][j] = min(dp[i][j], dp[i ^ (1 << j)][k] + self._graph.getCost(k,j))

        sol = self._inf
        #First Node
        x = self._graph.getVertices()
        x = x[0]
        for i in self._graph.parseNodeIn(x):
            sol = min(sol, dp[(1 << self._graph.getNumberOfVertices()) - 1][i] + self._graph.getCost(i,x))


        if sol == self._inf:
            print("There is no solution")
        else:
            print("Cost of the mininum cost hamiltionian cycle is: ", sol)



class UiPracticalWork5():
    def __init__(self):
        while True:
            try:
                self.menu()
                self.parseCommands()
            except graphException as e:
                print(e)

    def menu(self):
        msg = '\n\n#########################################\n'
        msg += '1. Find a minimum cost Hamiltonian cycle.\n'
        msg += '######################################### \n \n'

        print(msg)

    def parseCommands(self):
        cmd = int(input("Command: "))

        if cmd == 1:
            PracticalWork4Obj = PracticalWork5()
            PracticalWork4Obj.MinimumCostHamiltonian()


Ui = UiPracticalWork5()
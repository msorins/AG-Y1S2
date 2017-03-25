from Graphs import UndirectedGraph
from Graphs import DirectedGraph
from Graphs import graphException

class PracticalWork2():
    def __init__(self):
        self._graph = UndirectedGraph("PracticalWork2.txt")
        self._graph.read()

    def getNodesByDFS(self):
        used = {}
        connectedComponents = []

        for node in self._graph.getGraph():
            used[node] = False

        for node in self._graph.getGraph():
            if used[node] == False:
                used[node] = True
                connectedComponents.append(self.DFS(node, used))

        print("There are ", len(connectedComponents), " connected components")
        crt = 0
        for i in connectedComponents:
            crt += 1
            strRes = str(crt) +': '
            for j in i:
                strRes = strRes + str(j) + " "

            strRes = strRes
            print(strRes)


    def DFS(self, node, used):
        res = []
        res.append(node)
        for nextNode in self._graph.parseNodeOut(node):
            if used[nextNode] == False:
                used[nextNode] = True
                for i in self.DFS(nextNode, used):
                    res.append(i)

        return res

class Bonus1():
    def __init__(self):
        self._graph = DirectedGraph("PracticalWork2-Bonus1.txt")
        self._graph.read()

    def stronglyConnectedComponents(self):
        fol = {}
        st = []
        ctc = []

        for node in self._graph.getGraph():
            fol[node] = False

        for node in self._graph.getGraph():
            if fol[node] == False:
                self.DFS1(node, fol, st)

        for node in self._graph.getGraph():
            fol[node] = False

        while len(st):
            node = st[-1]
            st.pop()

            if (fol[node]):
                continue

            fol[node] = True
            ctc.append(self.DFS2(node, fol))



        print("Number of strongly connected components is ", len(ctc))
        nr = 0
        for i in ctc:
            nr += 1
            strRes = str(nr) + ": "
            for j in sorted(i):
                strRes += str(j) + " "
            print(strRes)




    def DFS1(self, node, fol, st):
        for nextNode in self._graph.parseNodeOut(node):
            if fol[nextNode] == False:
                fol[nextNode] = True
                self.DFS1(nextNode, fol, st)
        st.append(node)

    def DFS2(self, node, fol):
        res = []

        res.append(node)
        for prevNode in self._graph.parseNodeIn(node):
            if fol[prevNode] == False:
                fol[prevNode] = True
                for i in self.DFS2(prevNode, fol):
                    res.append(i)

        return res

class Bonus2():
    def __init__(self):
        self._graph = UndirectedGraph("PracticalWork2-Bonus2.txt")
        self._graph.read()
        self._res = []

    def biconnectedComponents(self):
        st = []
        nivel = {}
        low = {}

        st.append(1)
        self.DFS(1, 1, st, nivel, low)

        print("Number of biconnected connected components is ", len(self._res))
        nr = 0
        for i in self._res:
            nr += 1
            strRes = str(nr) + ": "
            for j in sorted(i):
                strRes += str(j) + " "
            print(strRes)


    def DFS(self, node, k, st, nivel, low):
        nivel[node] = k
        low[node] = k

        for nextNode in sorted(self._graph.parseNodeOut(node)):
            if nextNode not in nivel:
                st.append(nextNode)
                self.DFS(nextNode, k + 1, st, nivel, low)

                low[node] = min(low[node], low[nextNode])
                if low[nextNode] >= nivel[node]:
                    self.getOut(node, nextNode, st)
            else:
                low[node] = min(low[node], nivel[nextNode])

    def getOut(self, left, right, st):
        res = []
        while st[-1] != right:
            res.append(st[-1])
            st.pop()
        st.pop()

        res.append(left)
        res.append(right)

        self._res.append(res)


class UiPracticalWork2():
    def __init__(self):
        while True:
            try:
                self.menu()
                self.parseCommands()
            except graphException as e:
                print(e)

    def menu(self):
        msg = '\n\n#########################################\n'
        msg += '1. Get connected components \n'
        msg += '2. Get strongly connected components \n'
        msg += '3. Get biconnected components \n'
        msg += '######################################### \n \n'

        print(msg)

    def parseCommands(self):
        cmd = int(input("Command: "))

        if cmd == 1:
            PracticalWork2Obj = PracticalWork2()
            PracticalWork2Obj.getNodesByDFS()
        elif cmd == 2:
            bonus1Obj = Bonus1()
            bonus1Obj.stronglyConnectedComponents()
        elif cmd == 3:
            bonus2Obj = Bonus2()
            bonus2Obj.biconnectedComponents()


Ui = UiPracticalWork2()
from Graphs import UndirectedGraph
from Graphs import DirectedGraph

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

        print("\n\n")

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

    def StronglyConnectedComponents(self):
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

        a = 3

        print("Number of strongly connected components is ", len(ctc))
        nr = 0
        for i in ctc:
            nr += 1
            strRes = str(nr) + ": "
            for j in sorted(i):
                strRes += str(j) + " "
            print(strRes)

        print("\n\n")



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

PracticalWork2Obj = PracticalWork2()
PracticalWork2Obj.getNodesByDFS()

bonus1Obj = Bonus1()
bonus1Obj.StronglyConnectedComponents()
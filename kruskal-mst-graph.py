class Vertex:
    def __init__(self, key):
        self.id = key
        self.visited =False
        self.connectedTo = {}
        self.set=[self.id]   # for kruskal
        self.dist = float("inf")

    def addNeighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def __cmp__(self, v):
        return self.dist<v.dist

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Edge:
    def __init__(self,f,t,w):
        self.front=f
        self.tail=t
        self.weight=w

    def __repr__(self):
        return '({})____{}____({})\n'.format(self.front.getId(),self.weight, self.tail.getId())


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.edgeList = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost):  # f is from node, t is to node
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.edgeList.append(Edge(self.vertList[f],self.vertList[t],cost))
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def e_sort(self,e):
            return e.weight

    def findset(self,v,disjointSet):
        for i in disjointSet:
            if v in i:
                return i

    def mstKruskal(self):
        edgeListAsc=sorted(self.edgeList,key=self.e_sort)   #list of sorted edges based on edge weight.
        MST=[]                                              #spanning tree with list of edges.
        disjointSet = []                                    #a list which contains the individual sets of all vertices.
        for i in self.vertList:
            disjointSet.append(self.vertList[i].set)

        #now,disjointSet contains=>[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

        for e in edgeListAsc:
            s1 = self.findset(e.front.getId(), disjointSet)     # here,we find the sets where the front and tail vertex...
            s2 = self.findset(e.tail.getId(), disjointSet)      #...of the current edge are present.

            if s1==s2:               #if s1 and s2 are same, both front and tail vertices are present in the same...
                continue             #...set and therefore it results in a cycle.
            if s1 != s2:                # if both sets aren't same,we append the current edge to the MST
                MST.append(e)
                if len(s1) > len(s2) or len(s1) == len(s2):                    #Here , we are combining both the sets...
                    disjointSet.remove(s2)                                    #...and removing the set which is smaller
                    self.findset(e.front.getId(), disjointSet).extend(s2)
                else:
                    disjointSet.remove(s1)
                    self.findset(e.tail.getId(), disjointSet).extend(s1)
        for i in MST:
            print(i)
        return

def main():
    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.addEdge(5, 1, 8)
    g.addEdge(1, 2, 19)
    g.addEdge(5, 0, 10)
    g.addEdge(4, 6, 11)
    g.addEdge(6, 10, 23)
    g.addEdge(10, 9, 33)
    g.addEdge(9, 8, 7)
    g.addEdge(6, 7, 6)
    g.addEdge(8, 7, 1)
    g.addEdge(9, 6, 9)
    g.addEdge(7, 10, 14)
    g.addEdge(0, 4, 15)
    g.addEdge(0, 3, 16)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 30)
    g.addEdge(4, 5, 18)
    g.addEdge(5, 2, 22)
    g.addEdge(3, 1, 17)

    print("The MST of the given graph contains the following edges:")
    g.mstKruskal()

if __name__ == "__main__":
    main()
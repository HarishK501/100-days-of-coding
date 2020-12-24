# Kosaraju's algorithm implementation

class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list
        self.vertList = set()

    def addEdge(self, u, v):
        self.vertList.add(u)
        self.vertList.add(v)
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = []
            self.graph[u].append(v)


def DFS(graph, node, path):
    '''
    graph : adjacency list
    node : vertex 
    path : traversal_list
    '''
    path.append(node)
    if node in graph.keys():
        for i in graph[node]:
            if i not in path:
                DFS(graph, i, path)


def getMotherVertex(g):
    DFSpath = []
    last = 0  # last finishing node in a DFS
    for i in range(len(g.vertList)):
        if i not in DFSpath:
            DFS(g.graph, i, DFSpath)
            last = i

    DFSpath = []
    DFS(g.graph, last, DFSpath)

    if len(DFSpath) == len(g.vertList):
        return last
    else:
        return -1


def main():

    print("\nGraph 1:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 4)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(2, 4)
    g.addEdge(3, 1)
    g.addEdge(3, 2)
    g.addEdge(4, 3)
    x = getMotherVertex(g)
    if x == -1:
        print("No mother vertex found in the graph.")
    else:
        print("The mother vertex is {}".format(x))

    print("\nGraph 2:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(3, 2)
    x = getMotherVertex(g)
    if x == -1:
        print("No mother vertex found in the graph.")
    else:
        print("The mother vertex is {}".format(x))

    print("\nGraph 3:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    x = getMotherVertex(g)
    if x == -1:
        print("No mother vertex found in the graph.")
    else:
        print("The mother vertex is {}".format(x))
    print()


if __name__ == "__main__":
    main()

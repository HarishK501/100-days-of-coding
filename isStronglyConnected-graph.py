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


def reverseEdges(graph):
    '''
    graph : adjacency list
    '''
    revGraph = Graph()
    for i in graph:
        for j in graph[i]:
            revGraph.addEdge(j, i)

    return revGraph


def isStronglyConnected(g):
    DFSpath = []
    DFS(g.graph, 0, DFSpath)

    # now DFSpath will contain nodes in DFS order
    if not len(DFSpath) == len(g.vertList):
        return "The given graph is not strongly connected"

    # reversing edges of the graph
    reversedGraph = reverseEdges(g.graph)
    # DFS on the reversed graph
    DFSpath = []
    DFS(reversedGraph.graph, 0, DFSpath)

    if not len(DFSpath) == len(reversedGraph.vertList):
        return "The given graph is not strongly connected\n"

    return "The given graph is strongly connected\n"


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
    print(isStronglyConnected(g))

    print("Graph 2:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    print(isStronglyConnected(g))
    return


if __name__ == "__main__":
    main()

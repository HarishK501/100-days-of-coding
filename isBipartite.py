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


def isBipartite(graph, color, node=0):

    if node in graph.keys():
        for i in graph[node]:
            if i not in color.keys():
                color[i] = not color[node]
                if not isBipartite(graph, color, i):
                    return False
            elif color[node] == color[i]:
                return False
    return True


def main():

    print("\nGraph 1:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 1)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(5, 6)
    g.addEdge(4, 7)
    g.addEdge(2, 3)
    g.addEdge(4, 5)
    g.addEdge(6, 7)
    print(isBipartite(g.graph, {0: True}))

    print("Graph 2:")
    g = Graph()
    g.vertList.add(0)
    g.addEdge(0, 1)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(5, 6)
    g.addEdge(4, 7)
    g.addEdge(2, 3)
    g.addEdge(4, 5)
    g.addEdge(6, 4)
    print(isBipartite(g.graph, {0: True}))
    return


if __name__ == "__main__":
    main()

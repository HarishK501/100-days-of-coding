class Graph:
    def __init__(self):
        self.graph = {}
        self.vertList = set()

    def addEdge(self, u, v):
        self.vertList.add(u)
        self.vertList.add(v)
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = []
            self.graph[u].append(v)


def trace(start, node, parentDict):
    path = ""
    while node in parentDict.keys():
        path = "➡ " + str(node) + path
        node = parentDict[node]

    return "Shortest path found: \n" + str(start) + path


def findPath(G, start, end):

    q = [start]
    cameFrom = {}
    visited = [False]*len(G.vertList)
    visited[start] = True
    while q:
        n = q.pop(0)
        if n == end:
            return trace(start, n, cameFrom)
        try:
            for i in G.graph[n]:
                if not visited[i]:
                    visited[i] = True
                    cameFrom[i] = n
                    q.append(i)
        except:
            continue
    return "No path exists"


def main():

    g = Graph()
    g.addEdge(5, 1)
    g.addEdge(1, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 6)
    g.addEdge(6, 10)
    g.addEdge(10, 9)
    g.addEdge(9, 8)
    g.addEdge(6, 7)
    g.addEdge(8, 7)
    g.addEdge(9, 6)
    g.addEdge(7, 10)
    g.addEdge(0, 4)
    g.addEdge(0, 3)
    g.addEdge(0, 2)
    g.addEdge(0, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 2)
    g.addEdge(3, 1)

    print("Type # to exit")
    while True:
        s = input("\nstart,end = ")
        if s == "#":
            break
        arr = list(map(int, s.split(',')))
        print(findPath(g, arr[0], arr[1]))


if __name__ == "__main__":
    main()


# Test graphs

    # # Graph 1

    # print("Graph 1")
    # g.addEdge(5, 2)
    # g.addEdge(5, 0)
    # g.addEdge(4, 0)
    # g.addEdge(4, 1)
    # g.addEdge(2, 3)

    # #Graph 2

    # print("Graph 2")
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(2, 3)
    # g.addEdge(1, 2)
    # g.addEdge(1, 5)
    # g.addEdge(6, 1)
    # g.addEdge(6, 5)
    # g.addEdge(5, 4)
    # g.addEdge(5, 3)

    # # Graph 3

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


def createBoard(size, ladders, snakes):
    g = Graph()
    start = 0  # before starting to move
    for i in range(start, size):
        j = 1
        while j <= 6 and i+j <= size:
            if i+j in ladders.keys():
                g.addEdge(i, ladders[i + j])
            elif i+j in snakes.keys():
                g.addEdge(i, snakes[i + j])
            else:
                g.addEdge(i, i + j)
            j += 1
    return g, start


def findMinDiceThrows(g, st, end):
    # a BFS here
    q = [st]
    cameFrom = {}
    visited = [False]*len(g.vertList)
    visited[st] = True
    while q:
        n = q.pop(0)
        if n == end:
            count = 0
            while end in cameFrom.keys():
                count += 1
                end = cameFrom[end]
            return count
        try:
            for i in g.graph[n]:
                if not visited[i]:
                    visited[i] = True
                    cameFrom[i] = n
                    q.append(i)
        except:
            continue
    return "No path exists"


if __name__ == "__main__":

    # case 1 =====================================
    print("\nCase 1:")
    ladders = {}
    snakes = {}
    # add ladders
    ladders[1] = 38
    ladders[4] = 14
    ladders[9] = 31
    ladders[21] = 42
    ladders[28] = 84
    ladders[51] = 67
    ladders[72] = 91
    ladders[80] = 99

    # add snakes
    snakes[17] = 7
    snakes[54] = 34
    snakes[62] = 19
    snakes[64] = 60
    snakes[87] = 36
    snakes[93] = 73
    snakes[95] = 75
    snakes[98] = 79

    boardSize = 100
    board, start = createBoard(boardSize, ladders, snakes)
    minThrows = findMinDiceThrows(board, start, boardSize)
    print("\nMinimim number of dice throws required =", minThrows, "\n")

    # case 2 =======================================
    print("\nCase 2:")
    ladders = {}
    snakes = {}
    # ladders
    ladders[2] = 21
    ladders[4] = 7
    ladders[10] = 25
    ladders[19] = 28

    # Snakes
    snakes[26] = 0
    snakes[20] = 8
    snakes[16] = 3
    snakes[18] = 6

    boardSize = 30
    board, start = createBoard(boardSize, ladders, snakes)
    minThrows = findMinDiceThrows(board, start, boardSize)
    print("\nMinimim number of dice throws required =", minThrows, "\n")

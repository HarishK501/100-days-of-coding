class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


class Grid:
    def __init__(self, side):
        self.grid = {}
        self.createGrid(side)

    def createGrid(self, side):
        for i in range(side):
            for j in range(side):
                self.grid[str(i)+','+str(j)] = Box(i, j)


def findMinMovesKnight(grid, start, end):
    q = [start]
    cameFrom = {}
    visited = [start]
    X = [2, 2, -2, -2, 1, 1, -1, -1]
    Y = [1, -1, -1, 1, -2, 2, 2, -2]
    while q:
        n = q.pop(0)
        n_key = str(n.x)+','+str(n.y)
        if n == end:
            count = 0
            path = ""
            while n_key in cameFrom.keys():
                count += 1
                path = "➡ " + str(grid[n_key]) + path
                n_key = cameFrom[n_key]
            print("Minimum number of moves = {}".format(count))
            print("Moves: \n" + str(start) + path)
            return
        for i in range(8):
            x1 = n.x + X[i]
            y1 = n.y + Y[i]
            key = str(x1)+','+str(y1)
            if key in grid.keys() and grid[key] not in visited:
                visited.append(grid[key])
                q.append(grid[key])
                cameFrom[key] = n_key

    return


def main():
    board = Grid(8)
    startX = 0
    startY = 0
    endX = 7
    endY = 7
    print("\n")
    findMinMovesKnight(
        board.grid,
        board.grid[str(startX)+','+str(startY)],
        board.grid[str(endX)+','+str(endY)]
    )
    return


if __name__ == "__main__":
    main()

def findLongestPath(mat, visited, startX, startY, endX, endY, curMax=0, dist=0):

    if mat[startX][startY] == 0:
        return 0

    if startX == endX and startY == endY:
        return max(curMax, dist)
    i = startX
    j = startY
    visited[i][j] = 1
    if 0 <= i+1 < len(mat) and 0 <= j < len(mat[0]) and not visited[i+1][j] and mat[i+1][j]:
        curMax = findLongestPath(mat, visited, i+1, j,
                                 endX, endY, curMax, dist+1)

    if 0 <= i-1 < len(mat) and 0 <= j < len(mat[0]) and not visited[i-1][j] and mat[i-1][j]:
        curMax = findLongestPath(mat, visited, i-1, j,
                                 endX, endY, curMax, dist+1)

    if 0 <= i < len(mat) and 0 <= j+1 < len(mat[0]) and not visited[i][j+1] and mat[i][j+1]:
        curMax = findLongestPath(mat, visited, i, j+1,
                                 endX, endY, curMax, dist+1)

    if 0 <= i < len(mat) and 0 <= j-1 < len(mat[0]) and not visited[i][j-1] and mat[i][j-1]:
        curMax = findLongestPath(mat, visited, i, j-1,
                                 endX, endY, curMax, dist+1)

    visited[i][j] = 0
    return curMax


if __name__ == '__main__':
    mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    ]
    x = len(mat)
    y = len(mat[0])
    visited = [[0 for i in range(y)] for x in range(x)]
    print("\nLongest distance =", findLongestPath(mat, visited, 0, 0, 5, 7), "\n")

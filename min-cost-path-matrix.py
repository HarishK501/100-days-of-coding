def trace(node, cameFrom):
    path = ""
    while node in cameFrom.keys():
        pos = '(' + str(node // 10) + ',' + str(node % 10) + ')'
        path = "➡ " + pos + path
        node = cameFrom[node]
    return '(0,0)' + path


def findMinCostPath(cost):
    cameFrom = {}
    lookup = [[cost[x][y]
               for y in range(len(cost[0]))] for x in range(len(cost))]

    for i in range(1, len(cost)):
        lookup[i][0] += lookup[i - 1][0]

    for j in range(1, len(cost[0])):
        lookup[0][j] += lookup[0][j - 1]

    for i in range(1, len(lookup)):
        for j in range(1, len(lookup[0])):
            a = lookup[i-1][j]
            b = lookup[i][j-1]
            c = lookup[i-1][j-1]

            if a <= b and a <= c:
                lookup[i][j] += a
                cameFrom[(i*10) + j] = ((i-1)*10)+j
            elif b <= a and b <= c:
                lookup[i][j] += b
                cameFrom[(i*10) + j] = (i*10) + j-1
            else:
                lookup[i][j] += c
                cameFrom[(i*10) + j] = ((i-1)*10) + j-1

    return lookup[i][j], trace((i*10) + j, cameFrom)


def main():
    cost = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 8, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
    print("Cost matrix:\n")
    for i in cost:
        print(i)

    arr = findMinCostPath(cost)
    print("\nLowest cost path:\n{}\n".format(arr[1]))
    print("Cost:", arr[0])
    return


if __name__ == "__main__":
    main()

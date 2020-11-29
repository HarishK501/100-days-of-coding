from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getDepth(root, node, level=0, result=[0]):
    if root:
        if root.data == node.data:
            result[0] = level
            return result[0]

        getDepth(root.left, node, level+1, result)
        getDepth(root.right, node, level+1, result)

        return result[0]


def findDistance(root, n1, n2):
    lca = findLowestCommonAncestor(root, n1, n2)
    x = getDepth(lca, n1)
    y = getDepth(lca, n2)
    return x + y


def findLowestCommonAncestor(root, u1, u2):
    if not root:
        return None
    if root.data == u1.data or root.data == u2.data:
        return root

    u = findLowestCommonAncestor(root.left, u1, u2)
    v = findLowestCommonAncestor(root.right, u1, u2)
    if u and v:
        return root
    elif u:
        return u
    elif v:
        return v
    return None


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


if __name__ == "__main__":
    vertexDict = {}
    vertexDict[1] = root = node(1)
    vertexDict[2] = root.left = node(2)
    vertexDict[3] = root.right = node(3)
    vertexDict[4] = root.left.left = node(4)
    vertexDict[5] = root.left.right = node(5)
    vertexDict[6] = root.right.left = node(6)
    vertexDict[7] = root.right.right = node(7)
    vertexDict[8] = root.left.left.left = node(8)
    vertexDict[9] = root.left.left.right = node(9)
    vertexDict[10] = root.left.right.left = node(10)
    vertexDict[11] = root.left.right.right = node(11)
    vertexDict[12] = root.right.left.left = node(12)
    vertexDict[13] = root.right.left.right = node(13)
    vertexDict[14] = root.right.right.left = node(14)
    vertexDict[15] = root.right.right.right = node(15)

    print(drawTree(root))

    print("Type # to exit")
    while True:
        u = input("\nEnter two nodes: ")
        if u == '#':
            break
        arr = list(map(int, u.split()))
        u1 = vertexDict[arr[0]]
        u2 = vertexDict[arr[1]]
        print("The distance between {} and {} is = {}".format(
            u1.data, u2.data, findDistance(root, u1, u2)))

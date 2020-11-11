from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countNodes(root):
    if root:
        return 1 + countNodes(root.left) + countNodes(root.right)
    else:
        return 0


def isMinHeap(root, i, n):
    if root:
        if i > n-1:  # checking for complete tree
            return False
        if root.left and root.left.data <= root.data:
            return False
        if root.right and root.right.data <= root.data:
            return False
        return isMinHeap(root.left, 2*i + 1, n) and isMinHeap(root.right, 2*i + 2, n)
    else:
        return True


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


if __name__ == "__main__":

    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    # root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    print("\nInput Tree:")

    print(drawTree(root))

    if isMinHeap(root, 0, countNodes(root)):
        print("The tree is a min-heap\n")
    else:
        print("The tree is not a min-heap")

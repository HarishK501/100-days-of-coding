from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def delLeaves(root):
    if root:
        if root.left or root.right:
            root.left = delLeaves(root.left)
            root.right = delLeaves(root.right)
        else:
            return None

    return root


if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    root.left.left.right = node(8)
    root.right.right.left = node(9)

    print("\nInput Tree:")

    print(drawTree(root))

    print("Output Tree:")

    print(drawTree(delLeaves(root)))

from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "{}".format(self.data)


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def inOrderSuccessor(root, key):
    global result, prev

    if root and not result:
        inOrderSuccessor(root.left, key)
        if prev:
            if prev.data == key:
                result = root

        prev = root
        inOrderSuccessor(root.right, key)

    return result


if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    print("\nInput Tree:")

    print(drawTree(root))
    print("Enter nodes for which the inorder successor should be found:")

    while True:
        result = None
        prev = None
        s = input(">> ")
        if s == "#":
            break
        n = inOrderSuccessor(root, int(s))
        if n:
            print("Inorder successor of {} is: {}".format(s, n))
        else:
            print("Node not found.")

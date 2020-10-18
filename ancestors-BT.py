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


def findAncestors(root, key):
    if root:
        if root.data == key:
            return True
        x = findAncestors(root.left, key)
        y = findAncestors(root.right, key)
        if x or y:
            print(root.data, end=" ")
            return True

    return False


if __name__ == "__main__":

    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    root.left.left.left = node(8)
    root.left.left.right = node(9)
    root.left.right.left = node(10)
    root.left.right.right = node(11)
    root.right.left.left = node(12)
    root.right.left.right = node(13)
    root.right.right.left = node(14)
    root.right.right.right = node(15)

    print("\nInput Tree:")

    print(drawTree(root))
    print("Enter the node for which the ancestors should be found:\nType # to exit.")

    while True:
        s = input("➡  ")
        if s == "#":
            break
        if int(s) == root.data:
            print("No ancestors.")
            continue
        print("Ancestors - ", end="")
        findAncestors(root, int(s))
        print()

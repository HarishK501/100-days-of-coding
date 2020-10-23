from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def findPair(root, sum):
    control1 = False
    control2 = False

    data1 = 0
    data2 = 0

    root1 = root
    root2 = root

    stack1 = []
    stack2 = []

    while True:
        # normal iterative inorder
        while not control1:
            if root1:
                stack1.append(root1)
                root1 = root1.left
            else:
                if not len(stack1) == 0:
                    root1 = stack1.pop()
                    data1 = root1.data
                    root1 = root1.right
                control1 = True

        # iterative reversed inorder
        while not control2:
            if root2:
                stack2.append(root2)
                root2 = root2.right
            else:
                if not len(stack2) == 0:
                    root2 = stack2.pop()
                    data2 = root2.data
                    root2 = root2.left
                control2 = True

        if data1 + data2 == sum:
            if not data1 == data2:
                return "The pair with the given sum is: ({},{})\n".format(data1, data2)
            else:
                control1 = False

        elif data1 + data2 < sum:
            control1 = False
        else:
            control2 = False

        if (not root1 and len(stack1) == 0) or (not root2 and len(stack2) == 0):
            return "No pair exists with the given sum\n"

    return


if __name__ == "__main__":

    root = node(10)
    root.left = node(5)
    root.right = node(15)
    root.left.left = node(2)
    root.left.right = node(7)
    root.right.left = node(13)
    # root.right.right = node(20)

    print("Input Tree:")
    print(drawTree(root))

    print("Type # to exit")

    while True:
        s = input("-> Enter sum: ")
        if s == "#":
            break

        print(findPair(root, int(s)))

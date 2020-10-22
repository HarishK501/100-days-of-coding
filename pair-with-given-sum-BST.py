from binarytree import Node

global inOrderList
inOrderList = []


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


def inOrderTraversal(root):
    global inOrderList
    if root:
        inOrderTraversal(root.left)
        inOrderList.append(root.data)
        inOrderTraversal(root.right)


def findPair(root, sum):
    global inOrderList
    inOrderTraversal(root)

    # now inOrderList will have been updated
    i = 0
    j = len(inOrderList)-1

    while not i == j:
        if inOrderList[i] + inOrderList[j] == sum:
            print("The pair with given sum is : ({}, {})".format(
                inOrderList[i], inOrderList[j]))
            break
        if inOrderList[i] + inOrderList[j] < sum:
            i += 1
        else:
            j -= 1

    if i == j:
        print("No pair with the given sum")

    return


if __name__ == "__main__":

    root = node(10)
    root.left = node(5)
    root.right = node(15)
    root.left.left = node(2)
    root.left.right = node(7)
    root.right.left = node(13)
    root.right.right = node(20)

    print("Input Tree:")
    print(drawTree(root))

    print("Type # to exit")

    while True:
        inOrderList = []
        s = input("-> Enter sum: ")
        if s == "#":
            break
        findPair(root, int(s))
        print()

# a try to do this without extra space

 # global inOrderList
    # if root1 and root2 and not inOrderList:
    #     findPair(root1.left, root2.right, sum)
    #     # if not root1.data == root2.data:
    #     print("Root1 :{} Root2: {}".format(root1.data, root2.data))
    #     if root1.data + root2.data == sum and not root1.data == root2.data and not inOrderList:
    #         print("The pair with the given sum is ({},{})".format(
    #             root1.data, root2.data))
    #         inOrderList = True
    #         # findPair(root1.right, root2.left, sum)
    #     if root1.data + root2.data < sum:
    #         findPair(root1.right, root2, sum)
    #     else:
    #         findPair(root1, root2.left, sum)

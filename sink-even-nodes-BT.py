from collections import deque
from binarytree import Node


def sink(root):
    if root is None:
        return

    if root.left and root.left.data % 2 == 1:
        temp = root.data
        root.data = root.left.data
        root.left.data = temp
        sink(root.left)

    elif root.right and root.right.data % 2 == 1:
        temp = root.data
        root.data = root.right.data
        root.right.data = temp
        sink(root.right)


def sinkEvenNodes(root):

    if root is None:
        return

    sinkEvenNodes(root.left)
    sinkEvenNodes(root.right)

    if root.data % 2 == 0:
        sink(root)

    return root


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


class node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def buildTree(s):

    if(len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    root = node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size+1

    i = 1
    while(size > 0 and i < len(ip)):

        currnode = q[0]
        q.popleft()
        size = size-1

        currVal = ip[i]

        if(currVal != "N"):

            currnode.left = node(int(currVal))

            q.append(currnode.left)
            size = size+1

        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        if(currVal != "N"):
            currnode.right = node(int(currVal))
            q.append(currnode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input("No. of test cases: "))
    for _ in range(1, t+1):
        print("Case {}:".format(_))
        s = input("Tree: ")
        root = buildTree(s)
        print("Input tree: {}".format(drawTree(root)))
        print("Result: {}".format(drawTree(sinkEvenNodes(root))))

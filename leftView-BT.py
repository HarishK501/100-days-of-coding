from collections import deque
from binarytree import Node


def leftView(root):
    q = [root]
    leftViewList = [root.data]
    while q:
        nodeCount = len(q)
        while nodeCount > 0:
            curNode = q.pop(0)
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)
            nodeCount = nodeCount - 1
        if len(q):
            leftViewList.append(q[0].data)
    print("Left view: ")
    for i in range(len(leftViewList) - 1):
        print(leftViewList[i], end=" - ")
    print(leftViewList[len(leftViewList) - 1])
    return


class node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input("No. of test cases: "))
    for _ in range(0, t):
        s = input("\nTree: ")
        root = buildTree(s)
        print("Input tree:")
        print(drawTree(root))
        leftView(root)

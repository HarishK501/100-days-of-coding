from collections import deque
from binarytree import Node


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def diagonalTreversal(root):
    q = []
    nullNode = node(-1)
    print("➡ ", end=" ")

    q.extend([root, nullNode])
    # print(q)
    while len(q):
        n = q.pop(0)
        if n == nullNode:
            if len(q):
                q.append(nullNode)
                print("\n➡ ", end=" ")
            else:
                print()
        else:
            while n:
                print(n.data, end=" ")
                if n.left:
                    q.append(n.left)
                n = n.right
    return


class node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    # def __eq__(self, obj):
    #     return self.data == obj.data and self.right == obj.right and self.left == obj.left

    def __repr__(self):
        return str(self.data)


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
        currnode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currnode.left = node(int(currVal))

            # Push it to the queue
            q.append(currnode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currnode.right = node(int(currVal))

            # Push it to the queue
            q.append(currnode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input("No. of test cases: "))
    for _ in range(0, t):
        print("\nCase {}:".format(_+1))
        s = input("Tree: ")
        if s == "#":
            break
        root = buildTree(s)
        print("Input tree: ", drawTree(root))
        print("Diagonal traversal: ")
        diagonalTreversal(root)

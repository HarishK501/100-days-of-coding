from collections import deque
from binarytree import Node


def findLargestBST(root):
    if root:
        resL, sizeL, minL, maxL = findLargestBST(root.left)
        resR, sizeR, minR, maxR = findLargestBST(root.right)

        if (resL and resR) and root.data > maxL and root.data < minR:
            return True, sizeL+sizeR+1, min(root.data, min(minL, minR)), max(root.data, max(maxL, maxR))

        else:
            return False, max(sizeL, sizeR), 0, 0

    else:
        return True, 0, float('inf'), -float('inf')


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
        s = input("Tree: ")
        root = buildTree(s)
        print(drawTree(root))
        print("Size of the largest BST =", findLargestBST(root)[1])

# Tree 1
# 25 18 50 19 20 35 60 N 15 18 25 20 40 55 70 N N N N N N N 25

# Tree 2
# 10 15 8 12 20 5 2

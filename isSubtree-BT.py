
#  A subtree S of a tree T is a tree consisting of a node in T and all of its descendants in T.

from collections import deque
from binarytree import Node


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def computeFF(pattern):
    arr = [0] * len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i:i+1] == pattern[j:j+1]:
            i += 1
            arr[j] = i
            j += 1
        elif i == 0:
            arr[j] = 0
            j += 1
        else:
            i = arr[i-1]
    return arr


def KMP(text, pattern):
    ff = computeFF(pattern)  # ff-failure function
    i = 0
    j = 0
    indexList = []
    while i < len(text):
        if text[i:i+1] == pattern[j:j+1] and j == len(pattern) - 1:
            indexList.append(i-j)
            j = ff[j-1]
        elif text[i:i+1] == pattern[j:j+1]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                continue
            if ff[j] == 0:
                j = 0
            else:
                j = ff[j-1]

    if len(indexList):
        return True
    else:
        return False


def postOrder(root, flag=0, res=[]):
    if root:
        postOrder(root.left, 1, res)
        postOrder(root.right, 2, res)
        res.append(root.data)
        if flag == 0:
            return res
    else:
        if flag == 1:
            res.append('L')
        elif flag == 2:
            res.append('R')


def isSubtree(root1, root2):
    post1 = "".join(str(i)+" " for i in postOrder(root1, res=[]))
    post2 = "".join(str(i)+" " for i in postOrder(root2, res=[]))

    if KMP(post1, post2):
        return True
    return False


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
    n = len(ip)  # number of nodes

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
    return root, n


if __name__ == "__main__":
    t = int(input("No. of test cases: "))
    for _ in range(0, t):
        print("\nCase-{}:".format(_+1))
        s1 = input("Tree 1: ")
        if s1 == "#":
            break
        s2 = input("Tree 2: ")
        root1, n1 = buildTree(s1)
        root2, n2 = buildTree(s2)
        print("Input tree 1: {}".format(drawTree(root1)))
        print("Input tree 2: {}".format(drawTree(root2)))
        (root1, root2, a, b) = (root1, root2, 1, 2) if n1 > n2 else (
            root2, root1, 2, 1)
        if isSubtree(root1, root2):
            print("Tree-{} is subtree of Tree-{}".format(b, a))
        else:
            print("Tree-{} is NOT a subtree of Tree-{}".format(b, a))


# Case-1:
# Tree 1: 10 4 6 N 30
# Tree 2: 26 10 3 4 6 N 3 N 30

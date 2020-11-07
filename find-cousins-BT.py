from collections import deque
from binarytree import Node


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def getNode(root, node, parent=-1, level=0):
    if root:
        if root.data == node:
            return node, parent, level
        parent = root.data
        result = getNode(root.left, node, parent, level+1)
        if result:
            return result
        result = getNode(root.right, node, parent, level+1)
        if result:
            return result
    return


def findCousins(root, nodeData, parent=-1, level=0):
    '''
    nodeData[0]: value of node whose cousins are to be found
    nodeData[1]: parent of that node
    nodeData[2]: level of that node
    '''
    if root:
        if level == nodeData[2]:
            if not parent == nodeData[1]:
                print(root.data, end=" ")
                return
        parent = root.data
        findCousins(root.left, nodeData, parent, level+1)
        findCousins(root.right, nodeData, parent, level+1)

    return


class node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
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
        print("Case {}:".format(_+1))
        s1 = input("Tree: ")
        root = buildTree(s1)
        print("Input tree: {}".format(drawTree(root)))
        snodeData = int(input("Enter a node: "))
        n, p, l = getNode(root, snodeData)
        if not n:
            print("Node not found.")
        else:
            print("Cousin nodes of {} are:\n- ".format(snodeData), end="")
            findCousins(root, [n, p, l])
            print("\n")

from collections import deque
from binarytree import Node


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def isIdentical(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        if root1.data == root2.data:
            return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return False


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
        s1 = input("Tree-1: ")
        root1 = buildTree(s1)
        s2 = input("Tree-2: ")
        root2 = buildTree(s2)
        print("Input tree 1: {}".format(drawTree(root1)))
        print("Input tree 2: {}".format(drawTree(root2)))
        if isIdentical(root1, root2):
            print("The trees are identical")
        else:
            print("The trees are not identical")
# } Driver Code Ends

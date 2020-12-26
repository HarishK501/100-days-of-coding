from collections import deque
from binarytree import Node


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def getKthAncestor(root, inp):
    '''
    root = root of the binary tree
    inp = input values provided in the form of dictionary (immutable)

    inp {
        'node': target node,
        'k': value of k
    }
    '''
    if root is None:
        return None
    elif root.data == inp['node'] or getKthAncestor(root.left, inp) or getKthAncestor(root.right, inp):
        if inp['k'] > 0:
            inp['k'] -= 1
            return root

        elif inp['k'] == 0:
            inp['node'] = root.data
            return None


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
        arr = list(map(int, s.split()))
        root = buildTree(s)
        print(drawTree(root))
        n = int(input("Enter node: "))
        while n not in arr:
            n = int(input("Node not found.\nEnter a valid node: "))
        k = int(input("Enter k value: "))
        param = {'node': n, 'k': k}
        getKthAncestor(root, param)
        if not n == param['node']:
            print("The k'th ancestor of {} is {}".format(n, param['node']))
        else:
            print("No kth ancestor found for {} where k={}.".format(n, k))

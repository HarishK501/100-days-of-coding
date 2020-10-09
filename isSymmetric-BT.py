from binarytree import Node

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isSymmetric(root1, root2):

    if root1 is None and root2 is None:
        return True

    elif root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return isSymmetric(root1.left, root2.right) and isSymmetric(root1.right, root2.left)
    
    return False

def drawTree(v):
        if v==None:
            return None
        r = Node(v.data)
        r.left=drawTree(v.left)
        r.right=drawTree(v.right)
        return r

if __name__ == "__main__":

    # symmetric tree
    # root = node(1)
    # root.left = node(2)
    # root.right = node(2)
    # root.left.left = node(4)
    # root.left.right = node(3)
    # root.right.left = node(3)
    # root.right.right = node(4)

    # not a symmetric tree
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    print("\nInput Tree:")

    print(drawTree(root))

    if isSymmetric(root, root):
        print("The tree is symmetric\n")
    else:
        print("The tree is not symmetric")

    
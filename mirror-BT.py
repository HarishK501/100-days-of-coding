from binarytree import Node

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def mirror(v):
    if v is None:
        return None
    mnode = v
    temp = mnode.left
    mnode.left = mirror(v.right)
    mnode.right = mirror(temp)
    return mnode

def drawTree(v):
        if v==None:
            return None
        r = Node(v.data)
        r.left=drawTree(v.left)
        r.right=drawTree(v.right)
        return r

if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    root.left.left.left = node(8)
    root.left.left.right = node(9)
    root.left.right.left = node(10)
    root.left.right.right = node(11)
    root.right.left.left = node(12)
    root.right.left.right = node(13)
    root.right.right.left = node(14)
    root.right.right.right = node(15)

    print("Original Tree:")

    print(drawTree(root))

    print("Mirror Tree:")
    print(drawTree(mirror(root)))

    
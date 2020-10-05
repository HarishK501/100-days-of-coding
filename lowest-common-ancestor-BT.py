class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findLowestCommonAncestor(root, u1, u2):

    if not root:
        return None
    if root.data == u1.data or root.data == u2.data:
        return root.data
    
    u = findLowestCommonAncestor(root.left, u1, u2)
    v = findLowestCommonAncestor(root.right, u1, u2)
    if u and v:
        return root.data
    elif u:
        return u
    elif v:
        return v
    return None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # u1 = root.left.right.left    #10
    # u2 = root.left.right.right   #11

    # u1 = root.left.left.right    #9  
    # u2 = root.right.left         #6

    # u1 = root.right              #3
    # u2 = root.right.right.right  #15

    u1 = root.left.left.left     #8
    u2 = root.right.right.right  #15

    print("The Lowest common ancestor of ",u1.data," and ",u2.data," is: ", end ="")
    print(findLowestCommonAncestor(root, u1, u2))

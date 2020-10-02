class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def spiralLevelOrderTraversal(root):
    q = []
    traversal_subList = []
    traversalList = []
    q.append(root)
    i = 1
    my_flag = 0
    while q:
        n = q.pop(0)
        if n:     
            traversal_subList.append(n.data)
            if len(traversal_subList) == i:
                if my_flag == 0:
                    traversalList.extend(traversal_subList)
                    my_flag = 1
                else:
                    traversalList.extend(reversed(traversal_subList))
                    my_flag = 0
                i = i * 2
                traversal_subList = []
            q.append(n.left)
            q.append(n.right)
        else:
            traversal_subList.append(None)
    return traversalList

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

    result = spiralLevelOrderTraversal(root)
    print("\nSpiral Level Order Traversal:")
    for i in range(len(result)-1):
        print(result[i],end=" --> ")
    print(result[(len(result) - 1)])
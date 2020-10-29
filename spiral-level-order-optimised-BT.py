from binarytree import Node


class node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def spiralOrderTraversal(root):
    if root is None:
        return
    q = [root]
    flag = True
    while q:
        nodeCount = len(q)
        if flag:
            while nodeCount > 0:
                curNode = q.pop(0)
                print(curNode.data, end='➡ ')
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
                nodeCount = nodeCount - 1
        else:
            while nodeCount > 0:
                curNode = q.pop()
                print(curNode.data, end='➡ ')
                if curNode.right:
                    q.insert(0, curNode.right)
                if curNode.left:
                    q.insert(0, curNode.left)
                nodeCount = nodeCount - 1
        flag = not flag


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


if __name__ == '__main__':

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
    print("Input tree: ")
    print(drawTree(root))
    print("Spiral level ordered traversal:")
    spiralOrderTraversal(root)

from binarytree import Node


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def fullNodeInorderSuccessor(root):
    resultNode = root.right
    while resultNode.left:
        resultNode = resultNode.left
    return resultNode


def deleteNodeBST(root, data):
    if root:
        if root.data == data:
            if not root.left:
                tmp = root.right
                root = None
                return tmp   # here if root.right also does not exist, then the node to be deleted is a leaf node. So None will be returned here

            elif not root.right:
                tmp = root.left
                root = None
                return tmp

            # if the node to be deleted contains both child nodes
            else:

                tmp = fullNodeInorderSuccessor(root)
                root.data = tmp.data
                root.right = deleteNodeBST(root.right, tmp.data)

        elif root.data > data:
            root.left = deleteNodeBST(root.left, data)

        else:
            root.right = deleteNodeBST(root.right, data)

    return root


def insertNodeBST(root, data):
    if not root:
        root = node(data)

    elif data < root.data:
        root.left = insertNodeBST(root.left, data)

    else:
        root.right = insertNodeBST(root.right, data)

    return root


def main():

    root = node(50)
    insertNodeBST(root, 25)
    insertNodeBST(root, 75)
    insertNodeBST(root, 12)
    insertNodeBST(root, 36)
    insertNodeBST(root, 60)
    insertNodeBST(root, 84)

    print("\nInput tree: \n", drawTree(root))

    print("Type # to exit")
    while True:
        n = input("\nEnter node to be deleted: ")
        if n == "#":
            break
        root = deleteNodeBST(root, int(n))
        print("Tree after deleting {}".format(n))
        print(drawTree(root))

    return


if __name__ == "__main__":
    main()

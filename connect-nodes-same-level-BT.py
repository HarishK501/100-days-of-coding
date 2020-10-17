from binarytree import Node

# Linked List


class SinglyLinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)


def print_list(head):
    while head is not None:
        print(head, end="➡ ")
        head = head.next
    print("NULL")
    return


def getNode(head, data):
    while head is not None:
        if head.data == data:
            return head
        else:
            head = head.next
    return None


# Tree


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "{}".format(self.data)


def drawTree(v):
    if v == None:
        return None
    r = Node(v.data)
    r.left = drawTree(v.left)
    r.right = drawTree(v.right)
    return r


def connectNodesAtSameLevel(root):
    # level order approach

    q = []
    head = curNode = None
    linkedLists = []
    count = 0
    q.append(root)
    i = 1
    while q:
        n = q.pop(0)
        if n:
            if not head:

                head = SinglyLinkedListNode(n, None)
                curNode = head
            else:
                curNode.next = SinglyLinkedListNode(n, None)
                curNode = curNode.next

        count += 1
        if count == i:

            if head.data:
                linkedLists.append(head)
            i = i * 2
            head = None
            count = 0

        if n:
            q.append(n.left)
            q.append(n.right)

    return linkedLists


# Driver code


if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    # root.right.right = node(7)

    root.left.left.left = node(8)
    root.left.left.right = node(9)
    root.left.right.left = node(10)
    root.left.right.right = node(11)
    root.right.left.left = node(12)
    root.right.left.right = node(13)
    # root.right.right.left = node(14)
    # root.right.right.right = node(15)

    print("Input tree:")
    print(drawTree(root))
    print("Connected nodes: ")
    for i in connectNodesAtSameLevel(root):
        print_list(i)

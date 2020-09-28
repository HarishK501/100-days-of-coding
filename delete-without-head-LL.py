class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)

def print_list(head):
    while head is not None and head.data is not None:
        print(head, end="->")
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

def deleteNode(node):
    if node.next:
        node.data = node.next.data
        node.next = node.next.next
    else:
        node.data = None
    return


#Linked list
# 1-> 2-> 3-> 4-> 5
n5 = Node(5, None)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)
print("Original list:")
print_list(head)

n = int(input("Enter the node to be deleted: "))
delNode = getNode(head, n) 

print("List after deleting a node:")
deleteNode(delNode)
print_list(head)



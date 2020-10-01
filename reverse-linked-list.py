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

def reverse(head):
    prevNode = None
    curNode = nextNode = head.next
    head.next = prevNode
    prevNode = head
    while curNode is not None:
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode
    return prevNode

def main():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    print("Original list:")
    print_list(head)
    print("Reversed list:")
    print_list(reverse(head))
if __name__ == "__main__":
    main()




    
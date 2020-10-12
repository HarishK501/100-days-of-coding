class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)


def print_list(head):
    while head is not None and head.data:
        print(head, end=" -> ")
        head = head.next
    print("NULL")
    return


def deleteMiddle(head):
    p = head
    q = head
    while q:
        try:
            q = q.next.next
            p = p.next
        except:
            q = None

    # now p is the node which we have to delete
    try:
        p.data = p.next.data
        p.next = p.next.next
    except:
        p.data = None

    return head


def main():
    # head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
    # head = Node(1, None)
    head = Node(4, Node(5, Node(6, None)))
    print("Input Linked list:")
    print_list(head)

    print("\nAfter deleting middle element:\nList: ")
    print_list(deleteMiddle(head))


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)

def print_list(head):
    while head is not None:
        print(head, end=" -> ")
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

def mergeLists(head1, head2):    

    if not head1:
        return head2
    elif not head2:
        return head1
    
    if head1.data <= head2.data:
        head = Node(head1.data, None)
        head1 = head1.next
    else:
        head = Node(head2.data, None)
        head2 = head2.next
    startNode = head

    while head1 or head2:
        if head.next:
            head = head.next
        if not head1:
            head.next = head2
            break
        elif not head2:
            head.next = head1
            break
        if head1.data <= head2.data:
            head.next = Node(head1.data, None)
            head1 = head1.next
        else:
            head.next = Node(head2.data, None)
            head2 = head2.next
        
    return startNode


head1 = Node(1, Node(3, Node(5, Node(7, Node(9, None)))))
head2 = Node(2, Node(4, Node(6, Node(8, Node(10, None)))))

head = mergeLists(head1, head2)
print("Merged Linked List:")
print_list(head)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)


def detectCycle(head):
    p = head  # slow pointer
    q = head  # fast pointer
    while q:
        try:
            q = q.next.next
            p = p.next
        except:
            q = None
        if p == q:  # at any point, if both these pointers meet, then there exists a cycle in the graph
            return True

    return False


def main():
    # input 1
    print("\nList 1:")
    head = Node(1, None)
    a = Node(2, None)
    head.next = a
    a.next = Node(3, Node(4, Node(5, a)))

    if detectCycle(head):
        print("Cycle is present in the list.")
    else:
        print("No cycle is present in the list.")

    # input 2
    print("List 2:")
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))

    if detectCycle(head):
        print("Cycle is present in the list.")
    else:
        print("No cycle is present in the list.")


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)


def print_list(head):
    while head is not None and head.data:
        print(head, end=" ➡  ")
        head = head.next
    print("NULL")
    return


def deleteNodes(head, m, n):
    if head is None or head.next is None:
        return head
    prev = None
    root = head
    curNode = head

    for _ in range(0, m):
        if curNode:
            prev = curNode
            curNode = curNode.next
        else:
            break

    for _ in range(0, n):
        if curNode:
            curNode = curNode.next
        else:
            break

    prev.next = curNode

    deleteNodes(curNode, m, n)
    return root


def main():
    print("Type # to exit")
    i = 1
    while True:
        head = Node(1, Node(
            2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, None))))))))))
        print("\nTest {}:\nOriginal list:".format(i))
        print_list(head)
        s = input("m,n: ")
        if s == "#":
            break
        arr = list(map(int, s.split(',')))
        head = deleteNodes(head, arr[0], arr[1])
        print("Result: ")
        print_list(head)
        i += 1

    return


if __name__ == "__main__":
    main()

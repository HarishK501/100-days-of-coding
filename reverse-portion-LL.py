class Node:
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


def reversePortion(head, k):
    prev = None
    curNode = head
    while curNode and not k < 0:
        nextNode = curNode.next
        curNode.next = prev
        prev = curNode
        curNode = nextNode
        k -= 1
    if not k < 0:
        print("Index Error: out of range")
        return prev
    head.next = curNode

    return prev


def reverse(head, m, n):
    curNode = head
    prev = None
    if m < 0:
        print("Index error: m should be greater than 0")
        return head
    elif n < 0:
        print("Index error: n should be greater than 0")
        return head
    elif m > n:
        print("Index error: n should be greater than m")
        return head

    k = n-m
    if m == 0:
        return reversePortion(head, k)

    while not m == 0:
        prev = curNode
        curNode = curNode.next
        m -= 1

    prev.next = reversePortion(curNode, k)
    if prev.next:
        return head


def main():
    print("Reversing portion of a linked list")
    head = Node(
        11, Node(23, Node(35, Node(44, Node(52, Node(60, Node(77, None)))))))
    print("Original list:\n")
    print_list(head)
    print("\nEnter m and n:(space separated)\nm-start     n-end\n(Type # to exit)")
    while True:
        s = input("> ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        head = reverse(head, arr[0]-1, arr[1]-1)
        print("List: ", end="")
        print_list(head)


if __name__ == "__main__":
    main()

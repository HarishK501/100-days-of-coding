class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
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
    while curNode and k > 0:
        nextNode = curNode.next
        curNode.next = prev
        prev = curNode
        curNode = nextNode
        k -= 1

    return prev, curNode


def reverseAlternativeNodes(head, k):
    curNode = head
    prev = None

    while curNode:
        last = curNode  # the first node will become the last after reversing
        front, curNode = reversePortion(curNode, k)

        if not prev:
            head = front
        else:
            prev.next = front

        last.next = curNode

        # skipping next k nodes
        tmp_K = k
        prevX = None
        while curNode and tmp_K > 0:
            prevX = curNode
            curNode = curNode.next
            tmp_K -= 1
        prev = prevX

    return head


def main():
    print("Reversing alternating groups of k nodes of a linked list")
    head = Node(
        1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, None))))))))
    print("\nOriginal list:")
    print_list(head)

    while True:
        s = input("\nEnter k: ")
        if s == "#":
            break
        head = reverseAlternativeNodes(head, int(s))
        print("List: ", end="")
        print_list(head)

    return "\nThank You\n"


if __name__ == "__main__":
    print(main())

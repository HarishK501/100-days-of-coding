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


def isPalindrome(head):

    stack = []
    # traverse till mid

    p = head
    q = head
    flag = ''
    while q:
        stack.append(p)
        q = q.next
        if not q:
            # linked list contains odd number of elements
            flag = 'odd'
            break
        else:
            flag = 'even'
            q = q.next
        p = p.next

    if flag == 'odd':
        stack.pop()
        p = p.next
    while stack and p:
        if not p.data == stack.pop().data:
            print("The linked list is not a palindrome.")
            return
        else:
            p = p.next

    print("The linked list is a Palindrome ! ")

    return


def main():
    # linked list 1
    head = Node(11, Node(22, Node(33, Node(22, Node(11, None)))))
    print_list(head)
    isPalindrome(head)

    print("\n")

    # linked list 2
    head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    print_list(head)
    isPalindrome(head)

    print("\n")

    # linked list 3
    head = Node(10, Node(20, Node(30, Node(20, Node(10, None)))))
    print_list(head)
    isPalindrome(head)

    print("\n")


if __name__ == "__main__":
    main()

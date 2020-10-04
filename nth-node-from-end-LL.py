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

k = None
result = None

def printNthNodeFromLastUtil(head):
    global k, result
    if head:
        printNthNodeFromLastUtil(head.next)
        if not result:
            if k > 0:
                k = k-1
            else:
                result = head.data
        
    return None


def printNthNodeFromLast(head, n):
    global k, result
    k = n
    result = None
    printNthNodeFromLastUtil(head)
    return result
    

#Linked list
# 1-> 2-> 3-> 4-> 5
def main():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    print("List:")
    print_list(head)

    n = int(input("Enter the position of node from end: "))
    x = printNthNodeFromLast(head, n)
    if x:
        print("The node at the nth position from the end is: ", result, "\n")

    else:
        print("Invalid input\n")

if __name__ == "__main__":
    main()



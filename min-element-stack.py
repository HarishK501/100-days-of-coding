class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, num):
        if not len(self.stack) == self.size:
            if num in self.stack:
                print("Duplicate entry. Not pushed")
                return False
            self.stack.append(num)
            return True
        else:
            print("Stack Full Exception. {} not pushed.".format(num))
            return False

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Stack Empty Exception")
            return None

    def top(self):
        try:
            return self.stack[len(self.stack)-1]
        except:
            # print("Stack Empty Exception")
            return None

    def printStack(self):
        print(self.stack)


def main():
    # finding min element

    n = int(input("Enter size of stack: "))
    S = Stack(n)
    minStack = Stack(n)
    print("Enter your queries:\n➡ push <int>\t➡ pop\t➡ getMin")
    print("(Type # to exit)")
    while True:
        s = input(" ➡  ")
        if s == '#':
            break
        arr = list(map(str, s.split()))
        if arr[0] == 'push':
            arr[1] = int(arr[1])
            if S.push(arr[1]):
                print("Stack: ", end="")
                S.printStack()
                x = minStack.top()
                if not x:
                    minStack.push(arr[1])
                elif x > arr[1]:
                    minStack.push(arr[1])

        elif arr[0] == 'pop':
            if minStack.top() and S.top() == minStack.top():
                minStack.pop()
            print(S.pop())
            print("Stack: ", end="")
            S.printStack()

        elif arr[0] == 'getMin':
            print(minStack.top())

        else:
            print("Function undefined...")


if __name__ == "__main__":
    main()

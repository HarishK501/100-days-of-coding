class TwoStacks:
    def __init__(self, n):
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.arr[self.top1+1] = data
            self.top1 += 1

        else:
            print("Stack Full exception")
            print("Element not inserted")

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.arr[self.top2-1] = data
            self.top2 -= 1

        else:
            print("Stack Full exception")
            print("Element not inserted")

    def getTop1(self):
        if 0 <= self.top1:
            return self.arr[self.top1]
        else:
            print("Invalid operation")
            return -1

    def getTop2(self):
        if self.top2 < len(self.arr):
            return self.arr[self.top2]
        else:
            print("Invalid operation")
            return -1

    def pop1(self):
        x = self.getTop1()
        if x != -1:
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else:
            print("Stack Empty exception")

    def pop2(self):
        x = self.getTop2()
        if x != -1:
            self.arr[self.top2] = None
            self.top2 += 1
            return x
        else:
            print("Stack Empty exception")

    def printStack1(self):
        print(list(reversed(self.arr[0:self.top1+1])))

    def printStack2(self):
        print(self.arr[self.top2:len(self.arr)])

    def printArray(self):
        print(self.arr)


def main():
    n = int(input("Enter array size: "))
    ts = TwoStacks(n)
    print("\nOperations:")
    print("Stack 1:\tStack 2:\npush1 x\t\tpush2 x\npop1\t\tpop2\ngetTop1\t\tgetTop2\nprintS1\t\tprintS2\nprintArray\n")

    print("Type # to exit")
    while True:
        s = input(" ➡  ")
        if s == '#':
            break
        arr = list(map(str, s.split()))
        if arr[0] == 'push1':
            ts.push1(int(arr[1]))
        elif arr[0] == 'pop1':
            print(ts.pop1())
        elif arr[0] == 'push2':
            ts.push2(int(arr[1]))
        elif arr[0] == 'pop2':
            print(ts.pop2())
        elif arr[0] == 'getTop1':
            print(ts.getTop1())
        elif arr[0] == 'getTop2':
            print(ts.getTop2())
        elif arr[0] == 'printS1':
            ts.printStack1()
        elif arr[0] == 'printS2':
            ts.printStack2()
        elif arr[0] == 'printArray':
            ts.printArray()
        else:
            print("Undefined operation")

    return


if __name__ == "__main__":
    main()

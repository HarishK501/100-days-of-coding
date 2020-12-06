from stackADT import Stack


def sortStack(S, call=1, tmp=0):
    if call == 1:
        if not S.isEmpty():
            tmp = S.pop()
            sortStack(S)
            call = 2

    if call == 2:
        if S.isEmpty() or S.top() < tmp:
            S.push(tmp)
        else:
            tmp1 = S.pop()
            sortStack(S, call=2, tmp=tmp)
            S.push(tmp1)

    return S


def main():
    s = Stack(10)
    s.push(10)

    s.push(30)
    s.push(20)
    s.push(70)
    s.push(50)

    print("Type # to exit")
    print("Operations:\n1.push\t2.pop\t3.sort")

    print("\nInitial Stack:")
    s.printStack()
    while True:
        i = input("\n➡  ")
        if i == "#":
            break
        arr = list(map(str, i.split()))

        if arr[0] == 'pop':
            print(s.pop())
            s.printStack()
        elif arr[0] == 'push':
            s.push(int(arr[1]))
            s.printStack()
        elif arr[0] == 'sort':
            s = sortStack(s)
            s.printStack()
        else:
            print("Unknown operation.")

    return '\nThank You\n'


if __name__ == "__main__":
    print(main())

from stackADT import Stack


def reverseStack(S, call=1, tmp=0):
    if call == 1:
        if not S.isEmpty():
            tmp = S.pop()
            reverseStack(S)
            call = 2

    if call == 2:
        if S.isEmpty():
            S.push(tmp)
        else:
            tmp1 = S.pop()
            reverseStack(S, call=2, tmp=tmp)
            S.push(tmp1)

    return S


def main():
    s = Stack(10)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(70)
    s.push(50)

    print("\nInput Stack:")
    s.printStack()
    print()
    print("Reversed Stack")
    Sr = reverseStack(s)
    Sr.printStack()
    print()
    return


if __name__ == "__main__":
    main()

from stackADT import Stack


def sortStack(S):
    myStack = Stack(len(S.stack))
    while not S.isEmpty():
        curr = S.pop()

        while (not myStack.isEmpty()) and myStack.top() > curr:
            S.push(myStack.pop())

        myStack.push(curr)
    return myStack.stack


def main():
    # Input Stack 1
    st = Stack(10)
    st.push(34)
    st.push(3)
    st.push(31)
    st.push(40)
    st.push(23)
    print("\nStack 1: {}".format(st.stack))
    print("Sorted stack: {}".format(sortStack(st)))

    # Input Stack 2
    st = Stack(90)
    st.push(80)
    st.push(70)
    st.push(60)
    st.push(50)
    st.push(20)
    print("\nStack 2: {}".format(st.stack))
    print("Sorted stack: {}\n".format(sortStack(st)))
    return


if __name__ == "__main__":
    main()

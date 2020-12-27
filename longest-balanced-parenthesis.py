from stackADT import Stack


def getLBPlength(S):  # Longest Balanced Parenthesis(LBP)
    stk = Stack(len(S)+1)
    stk.push(-1)
    popCount = maxLen = 0
    for i in range(len(S)):
        if S[i] == '(':
            stk.push(i)
        else:
            if not stk.isEmpty():
                stk.pop()
                if stk.isEmpty():
                    stk.push(i)
                else:
                    popCount = i - stk.top()  # the important logic
                    maxLen = max(maxLen, popCount)
            # else:
            #     popCount = 0
    return maxLen


def main():
    print("Program to find the length of the longest balanced parenthesis")
    print("Enter '#' to exit")
    while True:
        s = input("\n ➡  ")
        if s == "#":
            break
        print(" Result:", getLBPlength(s))

    return


if __name__ == "__main__":
    main()


# s = ")())(()()()()"
# s = "()()()()()"
# s = "((((()"

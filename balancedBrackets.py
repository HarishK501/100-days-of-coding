def isBalanced(s):
    open_set = ['{', '[', '(']
    close_set = ['}', ']', ')']
    stack = []
    for i in s:
        if i in open_set:
            stack.append(i)
        elif i in close_set:
            if len(stack) == 0:
                return 'Not valid'
            x = stack.pop()
            if open_set.index(x) != close_set.index(i):
                return 'Not valid'
    if len(stack) == 0:
        return 'Valid'
    else:
        return 'Not valid'


def main():
    print("Program to check whether given string of brackets is valid.")
    print("Enter the string containing brackets\nType # to exit")
    while True:
        s = input("➡ ")
        if s == '#':
            break
        print("Result: " + isBalanced(s) + '\n')


if __name__ == "__main__":
    main()

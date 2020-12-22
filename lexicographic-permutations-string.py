from itertools import permutations


# function to calculate the factorial of a number
def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)


# using library functions
def findPermutations_Lib(S):
    result = sorted("".join(c) for c in permutations(S))
    return result


# function which returns a string which is its next permutation in the lexicographic order
def nextPermutation(s):
    s = list(s)

    i = len(s) - 2
    while i > -1 and s[i] >= s[i+1]:
        i -= 1

    j = len(s) - 1
    while j > -1 and s[j] <= s[i]:
        j -= 1

    t = s[i]
    s[i] = s[j]
    s[j] = t

    s[i+1:] = reversed(s[i+1:])
    return "".join(s)


# normal implementation
def findPermutations(S):
    S = list(S)
    S.sort()
    S = "".join(S)
    n = fact(len(S))
    result = [S]
    for _ in range(n-1):
        S = nextPermutation(S)
        if S not in result:  # to handle duplicates in given input string
            result.append(S)
        else:
            break

    return result


def main():
    print("Type # to exit")
    while True:
        s = input("\nEnter a string: ")
        if s == "#":
            break
        i = 1
        for res in findPermutations(s):
            print(i, '\t', res)
            i += 1

    return "\nThank You \n"


if __name__ == "__main__":
    print(main())

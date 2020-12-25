# approach 1 - recursive
def lis_recursive(A, i, prev):
    '''
    A = input array
    initial values:
        i = 0
        prev = -infinity
    '''
    if i == len(A):
        return 0

    exc = lis_recursive(A, i + 1, prev)

    inc = 0
    if A[i] > prev:
        inc = 1 + lis_recursive(A, i + 1, A[i])

    return max(inc, exc)


# approach 2 - dynamic programming
def lis_DP(A):
    lookup = [1] * len(A)

    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and lookup[i] < lookup[j] + 1:
                lookup[i] = lookup[j] + 1

    return max(lookup)


# approach 3 - using LCS
def longestCommonSubsequence(s1, s2):

    lcsArray = [[None]*(len(s2)+1) for i in range(len(s1)+1)]  # 2d array

    lcs = []

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                lcsArray[i][j] = 0
            elif not s1[i-1] == s2[j-1]:
                lcsArray[i][j] = max(lcsArray[i-1][j], lcsArray[i][j-1])
            else:
                lcsArray[i][j] = lcsArray[i-1][j-1] + 1

    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            lcs.insert(0, s1[i-1])
            i -= 1
            j -= 1

        elif lcsArray[i-1][j] > lcsArray[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs


def lis_LCS(A):
    return longestCommonSubsequence(A, sorted(A))


if __name__ == '__main__':

    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            print('\nThank You\n')
            break
        A = list(map(int, s.split(', ')))

        # print("Length of LIS is", lis_recursive(A, 0, float('-inf')))
        print("\nLength of LIS is", lis_DP(A))

        # printing the longest increasing subsequence
        print("Longest increasing subsequence:", lis_LCS(A))


# 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15

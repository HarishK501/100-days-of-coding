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


def main():
    print("Type # to exit")
    while True:
        s1 = input("\nEnter string 1: ")
        if s1 == "#":
            break
        s2 = input("Enter string 2: ")

        print("The longest common subsequence is '{}'".format(
            ''.join(longestCommonSubsequence(s1, s2))))
    return


if __name__ == "__main__":
    main()

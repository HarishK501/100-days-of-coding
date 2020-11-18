def shortestSuperSequence(s1, s2):

    scsArray = [[None]*(len(s2)+1) for i in range(len(s1)+1)]  # 2d array

    scs = []

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0:
                scsArray[i][j] = j
            elif j == 0:
                scsArray[i][j] = j
            elif not s1[i-1] == s2[j-1]:
                scsArray[i][j] = max(scsArray[i-1][j], scsArray[i][j-1]) + 1
            else:
                scsArray[i][j] = scsArray[i-1][j-1] + 1

    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            scs.insert(0, s1[i-1])
            i -= 1
            j -= 1

        elif scsArray[i-1][j] < scsArray[i][j-1]:
            scs.insert(0, s1[i-1])
            i -= 1
        else:
            scs.insert(0, s2[j-1])
            j -= 1

    while i > 0:
        scs.insert(0, s1[i-1])
        i -= 1

    while j > 0:
        scs.insert(0, s2[j-1])
        j -= 1

    return scs


def main():
    print("Type # to exit")
    while True:
        s1 = input("\nEnter string 1: ")
        if s1 == "#":
            break
        s2 = input("Enter string 2: ")

        print("The shortest common super-sequence is '{}'".format(
            ''.join(shortestSuperSequence(s1, s2))))
    return


if __name__ == "__main__":
    main()

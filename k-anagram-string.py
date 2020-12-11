def isKAnagram(s1, s2, k):
    count1 = {}
    count2 = {}
    if not len(s1) == len(s2):
        print("Improper input.")
        return

    for i, j in zip(s1, s2):

        if count1.get(i):
            count1[i] += 1
        else:
            count1[i] = 1

        if not count1.get(j):
            count1[j] = 0

        if count2.get(j):
            count2[j] += 1
        else:
            count2[j] = 1

        if not count2.get(i):
            count2[i] = 0

    diff = 0
    for i in count1.keys():
        if count1[i] > count2[i]:
            diff += abs(count1[i] - count2[i])

    if diff <= k:
        print("The given strings are {}-anagrams.".format(k))
    else:
        print("The given strings are NOT {}-anagrams.".format(k))

    return


if __name__ == "__main__":
    print("Type # and press \"Enter\" to exit")
    while True:
        s1 = input("\nEnter string 1: ")
        if s1 == "#":
            print("\nThank You\n")
            break
        s2 = input("Enter string 2: ")
        k = int(input("Enter k value: "))
        isKAnagram(s1, s2, k)

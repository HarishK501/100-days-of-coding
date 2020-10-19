def main():
    # # anagrams
    # s1 = "incest"
    # s2 = "insect"

    # s1 = "silent"
    # s2 = "listen"

    # # non-anagrams
    s1 = "Harry"
    s2 = "Harris"

    # find whether s1 and s2 are anagrams
    charCount = {}
    for i in s1:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1

    for i in s2:
        if i not in charCount:
            print(
                "Given strings '{}' and '{}' are not anagram of each other".format(s1, s2))
            return
        else:
            charCount[i] -= 1
            if charCount[i] == 0:
                charCount.pop(i, "No key Found")

    if charCount:
        print("Given strings '{}' and '{}' are not anagram of each other".format(s1, s2))
        return
    else:
        print("Given strings '{}' and '{}' are anagram of each other".format(s1, s2))
        return

    # print(charCount)


if __name__ == "__main__":
    main()

def isIsomorphic(s1, s2):

    if not len(s1) == len(s2):
        return False

    myMap = {}

    for i in range(len(s1)):
        # print(s1[i:i+1], s2[i:i+1])
        if s1[i:i+1] not in myMap.keys():
            myMap[s1[i:i+1]] = s2[i:i+1]
        else:
            if myMap[s1[i:i+1]] != s2[i:i+1]:
                return False

    return True


def main():
    print("Type # to exit.")
    while True:
        print()
        s1 = input("String 1 ➡  ")
        if s1 == '#':
            break
        s2 = input("String 2 ➡  ")
        if isIsomorphic(s1, s2):
            print("The strings are isomorphic. ")
        else:
            print("The strings are not isomorphic. ")
    return


if __name__ == "__main__":
    main()

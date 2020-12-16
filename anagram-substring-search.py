def searchString(S, p):
    charCount1 = {}
    for i in p:
        if i in charCount1:
            charCount1[i] += 1
        else:
            charCount1[i] = 1

    x = 0
    y = len(p)-1

    while y < len(S):
        temp = S[x:y+1]

        # now we have to check whether temp and pattern are anagrams
        charCount2 = charCount1.copy()
        for i in temp:
            if i not in charCount2:
                break
            else:
                charCount2[i] -= 1
                if charCount2[i] == 0:
                    charCount2.pop(i)

        if not charCount2:
            print("{} ({}-{})".format(temp, x, y))

        del(charCount2)
        x += 1
        y += 1


def main():
    print("Type # to exit.")
    while True:
        text = input("\nEnter text: ")
        if text == "#":
            break

        pattern = input("Enter pattern: ")
        print("Result: ")
        searchString(text, pattern)
    return "\nThank you\n"


if __name__ == "__main__":
    print(main())

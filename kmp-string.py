def computeFF(pattern):
    arr = [0] * len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i:i+1] == pattern[j:j+1]:
            i += 1
            arr[j] = i
            j += 1
        elif i == 0:
            arr[j] = 0
            j += 1
        else:
            i = arr[i-1]
    return arr


def KMP(text, pattern):
    ff = computeFF(pattern)  # ff-failure function
    i = 0
    j = 0
    indexList = []
    while i < len(text):
        if text[i:i+1] == pattern[j:j+1] and j == len(pattern) - 1:
            indexList.append(i-j)
            j = ff[j-1]
        elif text[i:i+1] == pattern[j:j+1]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                continue
            if ff[j] == 0:
                j = 0
            else:
                j = ff[j-1]

    if len(indexList):
        print("Pattern occurs at indices:", end=" ")
        for i in indexList[:len(indexList)-1]:
            print(i, end=",")
        print(indexList[len(indexList)-1])
    else:
        print("Pattern not found in text.")
    return


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter text: ")
        if s == "#":
            break
        pattern = input("Enter pattern: ")
        KMP(s, pattern)


if __name__ == "__main__":
    main()

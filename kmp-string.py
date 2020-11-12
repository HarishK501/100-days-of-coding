def computeFF(string):
    arr = [0] * len(string)
    i = 0
    j = 1
    while j < len(string):
        if string[i:i+1] == string[j:j+1]:
            i += 1
            arr[j] = i
            j += 1
        elif i == 0:
            arr[j] = 0
            j += 1
        else:
            i = arr[i-1]
    return arr


def KMP(text, string):
    ff = computeFF(string)  # ff-failure function
    i = 0
    j = 0
    indexList = []
    while i < len(text):
        if text[i:i+1] == string[j:j+1] and j == len(string) - 1:
            indexList.append(i-j)
            j = ff[j-1]
        elif text[i:i+1] == string[j:j+1]:
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
        print("String occurs at indices:", end=" ")
        for i in indexList[:len(indexList)-1]:
            print(i, end=",")
        print(indexList[len(indexList)-1])
    else:
        print("String not found in text.")
    return


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter text: ")
        if s == "#":
            break
        string = input("Enter string: ")
        KMP(s, string)


if __name__ == "__main__":
    main()

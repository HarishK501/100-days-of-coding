def getSplitPoint(arr):

    sumFromLeft = 0
    sumFromRight = 0

    for i in arr:
        sumFromLeft += i

    for i in range(len(arr)-1, -1, -1):
        sumFromRight += arr[i]
        sumFromLeft -= arr[i]
        if sumFromLeft == sumFromRight:
            return i, sumFromRight
    return -1, "The array cannot be split into two sub-arrays with same sum.\n"


def main():
    print("\nEnter array elements:\n(Type # to exit.)")
    while True:

        s = input("➡ ")
        if s == "#":
            break

        arr = list(map(int, s.split()))
        print("Input array: \n{}".format(arr))

        # split point is the index at which we have to split the array.
        splitPoint = getSplitPoint(arr)

        if splitPoint[0] == -1:
            print(splitPoint[1])
        else:
            print("The sub-arrays are: ")
            print(arr[0:splitPoint[0]])
            print(arr[splitPoint[0]:])
            print("Sum of each sub-array = {}\n".format(splitPoint[1]))

    return


if __name__ == "__main__":
    main()

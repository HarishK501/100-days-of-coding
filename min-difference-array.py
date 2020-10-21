def findMinDifference(A):
    A.sort()  # sorting done in O(nlogn)

    minDiff = float('inf')
    minDiffPairs = []
    for i in range(len(A)-1):
        if A[i+1] - A[i] < minDiff:
            minDiff = A[i+1] - A[i]
            minDiffPairs = []
        if A[i+1] - A[i] == minDiff:
            minDiffPairs.append((A[i], A[i+1]))

    print("Minimum difference = {}".format(minDiff))
    print("The pairs with minimum difference are:")
    for i in minDiffPairs:
        print(i)

    print("\n")
    return


def main():
    print("\nEnter array elements:\n(Type # to exit.)")
    while True:

        s = input("➡ ")
        if s == "#":
            break

        arr = list(map(int, s.split()))
        print("Input array: \n{}".format(arr))

        findMinDifference(arr)

    return


if __name__ == "__main__":
    main()

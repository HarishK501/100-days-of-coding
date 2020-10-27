def findMaxSumSubArray(arr):
    start = end = 0
    maxValue = -1 * float('inf')
    currentMax = 0

    for i in range(len(arr)):
        currentMax += arr[i]
        if maxValue < currentMax:
            maxValue = currentMax
            end = i
        if currentMax < 0:
            currentMax = 0
            start = i+1

    print("The maximum sum is : {}".format(maxValue))

    if start > end:
        print(
            "The sub-array with the maximum sum is [{}]".format(arr[end]))
    else:
        print(
            "The sub-array with the maximum sum is {}".format(arr[start:end+1]))
    print()
    return


def main():
    print("\nFinding the sub-array with the maximum sum...\nType # to exit\n")
    while True:
        s = input("Enter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split(',')))
        findMaxSumSubArray(arr)

    return


if __name__ == "__main__":
    main()

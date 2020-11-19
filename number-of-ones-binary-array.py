# Find number of ones in sorted binary array

def countOnes(A, low, high):
    if A[high] == 0:
        return 0

    if A[low] == 1:
        return high - low + 1

    mid = (low + high) // 2
    return countOnes(A, low, mid) + countOnes(A, mid + 1, high)


if __name__ == '__main__':

    print("Type # to exit")
    while True:
        s = input("\n➡  ")
        if s == "#":
            break

        arr = list(map(int, s.split()))
        print("Input array: {}".format(arr))
        print("Total number of 1's present = {}".format(
            countOnes(arr, 0, len(arr) - 1)))

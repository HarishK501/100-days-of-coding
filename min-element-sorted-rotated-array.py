def getMin(A):
    low = 0
    high = len(A) - 1

    while low <= high:

        mid = (low+high) // 2

        if mid - 1 >= 0:
            if A[mid-1] > A[mid]:
                return "Minimum element = {}".format(A[mid])

            elif A[mid] < A[high]:
                high = mid

            else:
                low = mid + 1

        else:
            return "Minimum element = {}".format(A[0])


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        print(getMin(arr))

    return "\nThank You\n"


if __name__ == '__main__':

    print(main())

def longestBitonicSubarray(A):

    incArr = [1] * len(A)

    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            incArr[i] = incArr[i - 1] + 1

    decArr = [1] * len(A)

    for i in range(len(A) - 2, -1, -1):
        if A[i] > A[i + 1]:
            decArr[i] = decArr[i + 1] + 1

    maxLBS = 1
    start = end = 0

    for i in range(len(A)):
        if maxLBS < incArr[i] + decArr[i] - 1:
            maxLBS = (incArr[i] + decArr[i] - 1)
            start = i - incArr[i] + 1
            end = i + decArr[i] - 1

    # print longest bitonic sublist
    print("The longest bitonic subarray is", A[start:(end+1)])


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        longestBitonicSubarray(arr)

    return "\nThank You\n"


if __name__ == '__main__':

    # A = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    # longestBitonicSubarray(A)
    print(main())

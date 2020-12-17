# naive approach - O(n^2)
def maxLengthSubarrayNaive(A, k):
    length = end = 0
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum == k:
                if length < j - i + 1:
                    length = j - i + 1
                    end = j
    print("The longest subarray with given sum is: ")
    print(A[end+1-length:end+1])
    return


# O(n) approach
def maxLengthSubarray(A, k):
    length = end = sum = 0
    sumLookup = {}

    for i in range(len(A)):
        sum += A[i]

        if sum not in sumLookup:
            sumLookup[sum] = i

        if sum == k:
            length = i+1
            end = i

        elif sum-k in sumLookup and length < i-sumLookup[sum-k]:
            length = i-sumLookup[sum-k]
            end = i

    print("The longest subarray with given sum is: ")
    print(A[end+1-length:end+1])
    return


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        k = int(input("Enter k: "))
        maxLengthSubarray(arr, k)

    return "\nThank You\n"


if __name__ == '__main__':
    print(main())

# Find the longest subarray with equal number of 0's and 1's 

def maxLengthSubarray(A):
    length = end = sum = 0
    sumLookup = {}

    for i in range(len(A)):
        sum += -1 if (A[i] == 0) else 1

        if sum not in sumLookup:
            sumLookup[sum] = i

        if sum == 0:
            length = i+1
            end = i

        elif sum in sumLookup and length < i-sumLookup[sum]:
            length = i-sumLookup[sum]
            end = i

    return A[end+1-length:end+1]


def main():
    print("The longest subarray with equal number of 0's and 1's ")
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        print("Result: ")
        x = maxLengthSubarray(arr)
        print(x if len(x) else "No such subarray...")

    return "\nThank You\n"


if __name__ == '__main__':
    print(main())

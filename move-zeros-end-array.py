def moveZerosToEnd(A):
    pivot = 0
    j = 0

    for i in range(len(A)):
        if not A[i] == pivot:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            j += 1

    return


def main():
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        if 0 in arr:
            moveZerosToEnd(arr)
            print("Result:\n", arr)
        else:
            print("No zeros found in array.")
        

    return "\nThank You\n"


if __name__ == '__main__':

    print(main())

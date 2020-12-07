# Find the element before which all the elements are smaller than it,
# and after which all are greater

def findElement(arr):
    maxLeft = [0] * len(arr)
    maxLeft[0] = -1

    i = 1
    while i < len(arr):
        # maxLeft[i] stores the maximum element in the left of arr[i]
        maxLeft[i] = max(maxLeft[i-1], arr[i-1])
        i += 1

    i -= 1
    minRightSoFar = float('inf')
    while i >= 0:
        if maxLeft[i] < arr[i] and minRightSoFar > arr[i]:
            return "➡  {}".format(arr[i])

        minRightSoFar = min(minRightSoFar, arr[i])
        i -= 1

    return "No such element"


def main():
    # arr = [1, 2, 3, 4, 5]
    print("\nProgram to find the element which is greater than all elements to its left and less than all elements to its right.\n")
    print("Type # to exit.")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        print(findElement(arr))

    return "\nThank You\n"


if __name__ == "__main__":
    print(main())

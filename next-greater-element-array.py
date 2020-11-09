from stackADT import Stack


def nextGreater(arr):
    s = Stack(len(arr))
    nextGreaterElement = {}

    s.push(arr[0])
    for i in range(1, len(arr)):
        if arr[i] in nextGreaterElement.keys():
            continue

        while len(s.stack) and arr[i] > s.top():
            n = s.pop()
            nextGreaterElement[n] = arr[i]

        s.push(arr[i])

    while len(s.stack):
        n = s.pop()
        nextGreaterElement[n] = None

    for i in arr:
        print("Next greater element of {} is {}.".format(
            i, nextGreaterElement[i]))


def main():
    print("Type # to exit")
    i = 1
    while True:
        print("\nTest {}:".format(i))
        s = input("Array: ")
        if s == "#":
            break
        arr = list(map(int, s.split(',')))
        nextGreater(arr)
        i += 1

    return


if __name__ == "__main__":
    main()

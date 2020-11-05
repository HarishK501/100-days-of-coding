# Program to find missing number in an Arithmetic Prograssion.
# O(log n)
def findMissingNumber(A):
    low = 0
    high = len(A) - 1
    if low == high:
        return "No number is missing"
    else:
        x = A[low+1] - A[low]
        y = A[high] - A[high-1]
        if x == y:
            cd = x  # common difference
            while low <= high:
                mid = (low + high) // 2
                if A[mid] != (A[mid-1]+cd):
                    return A[mid-1]+cd
                elif A[mid] != (A[(mid+1) % len(A[low:high+1])]-cd):
                    return A[mid+1]-cd
                else:
                    if (A[mid]-A[low]) // (mid-low+1) >= cd:
                        high = mid - 1
                    elif (A[high]-A[mid]) // (high-mid+1) >= cd:
                        low = mid + 1
                    else:
                        return -1
        elif x > y:
            return A[low]+y
        else:
            return A[high]-x

    cd = (A[len(A)-1]-A[0]) // len(A)
    print("cd = ", cd)
    # while low <= high:
    #     mid = (low + high) // 2

    return


def main():
    print("Type # to exit")
    while True:
        s = input("\n➡  ")
        if s == '#':
            break
        arr = list(map(int, s.split(',')))
        m = findMissingNumber(arr)
        if m == -1:
            print("No number is missing...")
            continue
        print("The missing number is {}.".format(m))


if __name__ == "__main__":
    main()

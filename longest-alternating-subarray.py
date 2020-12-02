def longestAlternatingSubarray(A):
    res = [A[0]]
    final = [A[0]]
    flag = 0 if res[0] > 0 else 1
    for i in range(1, len(A)):
        if flag == 0 and A[i] <= 0:
            res.append(A[i])
            if len(final) < len(res):
                final = res
            flag = 1
        elif flag == 1 and A[i] > 0:
            res.append(A[i])
            if len(final) < len(res):
                final = res
            flag = 0
        else:
            res = [A[i]]
            flag = 0 if res[0] > 0 else 1
    print("The longest alternating subarray is: \n{}".format(final))
    return


def main():
    print("\nType # to exit")
    while True:
        s = input("\nEnter array elements: ")
        if s == "#":
            break
        arr = list(map(int, s.split()))
        longestAlternatingSubarray(arr)
    return "\nThank you\n"


if __name__ == "__main__":
    print(main())

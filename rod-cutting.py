def rodCut(price):

    T = [0] * (len(price) + 1)

    for i in range(1, len(price) + 1):
        for j in range(i):
            T[i] = max(T[i], price[j] + T[i - j - 1])

    return T


if __name__ == '__main__':

    # length = [1, 2, 3, 4, 5, 6, 7, 8]
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print("Length\tPrice")
    for i in range(len(price)):
        print("{}\t{}".format(i+1, price[i]))

    # generate DP table
    lookup = rodCut(price)

    print("Type # to exit\n")
    while True:
        s = input("Enter rod length (<=8): ")
        if s == "#":
            break
        try:
            print("\nThe maximum value that can be obtained by cutting the rod and selling the pieces is: ",
                  lookup[int(s)], "\n")
        except:
            print("Incorrect rod length.\n")

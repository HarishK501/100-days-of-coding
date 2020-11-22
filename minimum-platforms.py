def findMinimumPlatforms(A, D):
    '''
    A - list of arrival times of trains
    D - list of departure times of trains
    '''   
    A.sort()
    D.sort()

    count = maxCount = 0
    i = j = 0

    while i < len(A):
        if A[i] < D[j]:
            count += 1
            maxCount = max(maxCount, count)
            i += 1
        else:
            count -= 1
            j += 1

    return maxCount


def main():
    print("Case 1:")
    arrival = [12.00, 12.10, 13.00, 13.20, 13.50, 15.00]
    departure = [12.30, 13.40, 13.20, 14.30, 14.00, 15.20]
    print("Train\tArrival\t\tDeparture")
    for i in range(len(arrival)):
        print("{}\t{:.2f}\t\t{:.2f}".format(i+1, arrival[i], departure[i]))
    print("\nMinimum platforms required = {}".format(
        findMinimumPlatforms(arrival, departure)))

    print()

    print("Case 2:")
    arrival = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
    departure = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
    print("Train\tArrival\t\tDeparture")
    for i in range(len(arrival)):
        print("{}\t{:.2f}\t\t{:.2f}".format(i+1, arrival[i], departure[i]))
    print("\nMinimum platforms required = {}".format(
        findMinimumPlatforms(arrival, departure)))

    return


if __name__ == "__main__":
    main()

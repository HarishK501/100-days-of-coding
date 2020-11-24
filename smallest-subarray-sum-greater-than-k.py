def smallestSubarray(A, k):
    windowSum = 0
 
    length = float('inf')
    left = right = 0
 
    while right < len(A):
        windowSum += A[right]
        while windowSum > k and left <= right:
            if length > right - left + 1:
                length = right - left + 1

            windowSum -= A[left]
            left = left + 1
        right += 1
    
    if length != float('inf'):
        begin = left - 2
        end = begin + length
        print("Smallest subarray whose sum is greater than {} is: \n{}".format(k, A[begin:end]))
    else:
        print("No sublist exists")

    return 
 
 
if __name__ == '__main__':
 
    print("Type # to exit")
    while True:
        arr = input("\nEnter array: ")
        if arr == '#':
            break
        arr = list(map(int, arr.split()))
        k = int(input("Enter k value: "))   
        smallestSubarray(arr, k)

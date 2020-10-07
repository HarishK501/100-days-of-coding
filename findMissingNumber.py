# program to find a missing number in first n natural numbers.
result = []

def findMissingNumber(arr, size):
    sum = 0
    for i in arr:
        sum += i
    first_n_sum = size*(size+1)//2
    result.append(first_n_sum-sum)

def main():
    n = int(input("No. of test cases: "))
    for _ in range(n):
        print("Test case-",_+1)
        arr = list(map(int, input("Enter array elements: ").split()))
        findMissingNumber(arr, len(arr)+1)
    print("\nResults:")
    for i in result:
        print(i)

if __name__ == "__main__":
    main()

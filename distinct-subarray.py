# Find all maximum length sub-arrays of an array having distinct elements

def distinctElementSubarray(S):

    visited = {}
    start = end = 0

    while end < len(S):

        while visited.get(S[end]):
            visited[S[start]] = False
            start = start + 1

        while end < len(S) and not visited.get(S[end]):
            visited[S[end]] = True
            end = end + 1

        print(S[start:end])


if __name__ == '__main__':
    print("Type '#' to exit.")
    while True:
        s = str(input("\nEnter array elements: "))
        if s == "#":
            break
        s = list(map(int, s.split()))
        print("\nSubarrays with distinct elements: ")
        distinctElementSubarray(s)

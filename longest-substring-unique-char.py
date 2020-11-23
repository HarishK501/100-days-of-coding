def longestUniqueSubstring(S):

    visited = {}
    begin = end = 0
    low = high = 0

    while high < len(S):
        if visited.get(S[high]):
            while S[low] != S[high]:
                visited[S[low]] = False
                low = low + 1

            low = low + 1

        else:
            visited[S[high]] = True
            if end - begin < high - low:
                begin = low
                end = high

        high = high + 1

    return S[begin:end + 1]


if __name__ == '__main__':
    print("Type '#' to exit.")
    while True:
        s = str(input("\nEnter a string: "))
        if s == "#":
            break
        print("Longest Substring with unique characters - {}".format(longestUniqueSubstring(s)))

def palindromeSubstring(s, low, high):
    while low > -1 and high < len(s) and s[low] == s[high]:
        low -= 1
        high += 1
    ps = s[low+1:high]  # ps-palindromic substring
    return ps


def longestPalindrome(s):
    max_substr = ""

    for i in range(len(s)):
        # for odd length palindromes
        substr = palindromeSubstring(s, i, i)

        if len(substr) > len(max_substr):
            max_substr = substr

        # for even length palindromes
        substr = palindromeSubstring(s, i, i+1)

        if len(substr) > len(max_substr):
            max_substr = substr
    return max_substr


def main():
    print("Type # to exit")
    while True:
        s = input("\nEnter a string: ")
        if s == "#":
            break
        print("Longest palindromic substring is: {}".format(longestPalindrome(s)))
    return


if __name__ == "__main__":
    main()

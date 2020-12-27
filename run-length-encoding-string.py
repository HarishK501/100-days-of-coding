# Convert a string-"aaaabbbccddd" to "a4b3c2d3"
def main():
    print("Type \"#\" for exit.")
    while(1):
        count = 1
        x = ""
        s1 = str(input("Enter a string: "))
        if s1 == "#":
            break
        for i,j in zip(s1,s1[1:]):
            if i == j:
                count += 1
                x += i
            else:
                x += i
                s1 = s1.replace(x, x[0:1]+str(count), 1)
                x = ''
                count = 1

        x = count-1
        if x != 0:
            s1 = s1[:-(count-1)] + str(count)
        else:
            s1 += str(count)
        print(s1)
        print()
if __name__ == "__main__":
    main()

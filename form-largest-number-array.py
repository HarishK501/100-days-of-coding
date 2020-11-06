import functools as ft


def greater(a1, a2):
    return int(str(a2)+str(a1)) - int(str(a1)+str(a2))


def formLargestNumber(arr):
    arr.sort(key=ft.cmp_to_key(greater))
    s = ""
    for i in arr:
        s += str(i)

    return s


def main():
    print("Type # to exit")
    while True:
        s = input("\n➡  ")
        if s == '#':
            break
        arr = list(map(int, s.split(',')))
        print("The largest number that can be formed is {}.".format(
            formLargestNumber(arr)
        ))


if __name__ == "__main__":
    main()


# Replace every element with the least greater element on its right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertIntoBST(root, data, successor):
    if root is None:
        return Node(data), successor

    if data < root.data:
        successor = root.data
        root.left, successor = insertIntoBST(root.left, data, successor)

    else:
        root.right, successor = insertIntoBST(root.right, data, successor)

    return root, successor


def replaceLeastGreater(arr):
    root = None
    for i in reversed(range(len(arr))):
        successor = -1
        root, successor = insertIntoBST(root, arr[i], successor)
        arr[i] = successor

    return arr


if __name__ == '__main__':

    print("Type # to exit")
    while True:
        s = input("\n➡  ")
        if s == "#":
            break

        arr = list(map(int, s.split()))
        print("Input array:\n{}".format(arr))
        print("Output: \n{}".format(replaceLeastGreater(arr)))


# 10 100 93 32 35 65 80 90 94 6
# 8 58 71 18 31 32 63 92 43 3 91 93 25 80 28

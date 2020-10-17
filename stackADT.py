class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, num):
        if not len(self.stack) == self.size:
            if num in self.stack:
                print("Duplicate entry. Not pushed")
                return False
            self.stack.append(num)
            return True
        else:
            print("Stack Full Exception. {} not pushed.".format(num))
            return False

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Stack Empty Exception")
            return None

    def top(self):
        try:
            return self.stack[len(self.stack)-1]
        except:
            # print("Stack Empty Exception")
            return None

    def printStack(self):
        print(self.stack)

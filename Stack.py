class Stack:
    STACK = []
    TOP = -1
    SIZE = 0

    def __int__(self, size=10):
        self.SIZE = size

    def push(self, element):
        self.TOP += 1
        self.SIZE += 1
        self.STACK.append(element)

    def pop(self):
        if self.SIZE == 0 or self.TOP == -1:
            pass
        self.STACK.remove(self.TOP)
        self.TOP -= 1
        self.SIZE -= 1

    def IS_EMPTY(self):
        if self.TOP == -1:
            return True
        else:
            return False

    def IS_FULL(self):
        if self.TOP is self.SIZE:
            return True
        else:

            return False

    def print_stcak(self):
        for i in range(self.SIZE):
            print(self.STACK[i])

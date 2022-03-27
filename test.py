class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        return

        # return self.stack.pop()

    def push(self, x):
        self.stack.append(x)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())


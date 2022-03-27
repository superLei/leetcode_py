class CQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack:
            return -1
        while self.stack:
            self.stack2.append(self.stack.pop())

        return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
# 使用栈a 实现队列的入，使用栈b实现队列的出
if __name__ == '__main__':
    obj = CQueue()
    param_2 = obj.deleteHead()
    obj.appendTail(5)
    obj.appendTail(2)
    print(obj.stack)
    param_3 = obj.deleteHead()
    param_4 = obj.deleteHead()
    print(obj.stack2)
    print(param_2)
    print(param_3)
    print(param_4)

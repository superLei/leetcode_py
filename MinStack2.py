class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_b = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stack_b:
            if self.stack_b[-1] >= x:
                self.stack_b.append(x)
        else:
            self.stack_b.append(x)

    def pop(self) -> None:
        p = self.stack.pop()
        if self.stack_b:
            if self.stack_b[-1] == p:
                self.stack_b.pop()
                if not self.stack_b and self.stack:
                    self.stack_b.append(p)
                    for x in self.stack:
                        if self.stack_b[-1] > x:
                            self.stack_b.append(x)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def min(self) -> int:
        if self.stack_b:
            return self.stack_b[-1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# 解题思路：使用辅助栈用来保存比较一次后的最小值集合，且栈顶一定是最小值。出栈时，需要再进行一次比较出栈后的原数据同时再写入辅助栈中。

if __name__ == "__main__":
    obj = MinStack()
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(2147483647)
    print(obj.top())
    obj.pop()
    print(obj.min())
    obj.pop()
    print(obj.min())
    obj.pop()
    obj.push(2147483647)
    print(obj.top())
    print(obj.min())
    obj.push(-2147483648)
    print(obj.top())
    print(obj.min())
    obj.pop()
    print(obj.min())

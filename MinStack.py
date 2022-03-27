class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            if x <= self.stack[len(self.stack) - 1]:
                tmp = self.stack[len(self.stack) - 1]
                self.stack[len(self.stack) - 1] = x
                self.stack.append(tmp)
            else:
                self.stack.append(x)
        else:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def min(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[0]
        else:
            return None

class MinStack(object):

    def __init__(self):
        self.s = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.s) == 0:
            new_min = val
        else:
            prev_min = self.s[-1][1]
            new_min = min(val, prev_min)
        self.s.append((val, new_min))

    def pop(self):
        """
        :rtype: None
        """
        e = self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

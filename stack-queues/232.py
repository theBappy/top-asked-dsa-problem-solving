# Amortized->O(1)
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
        self.peekEl = -1

    def push(self,x):
        if not self.input:
            self.peekEl = x
        self.input.append(x)

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        val = self.output.pop()
        return val

    def peek(self):
        if not self.output:
            return self.peekEl
        return self.output[-1]

    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0
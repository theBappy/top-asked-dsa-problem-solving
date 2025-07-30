# Tc = O(n) [push]
# Tc = O(1) [pop]
# Tc = O(1) [top]
# Tc = O(1) [isEmpty]


from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return len(self.q) == 0
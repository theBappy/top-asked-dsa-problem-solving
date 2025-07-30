# Tc = O(n)
# Sc = O(n)
from typing import List
class Solution:
    def operate(self, a: int, b: int, token: str) -> int:
        if token == '+':
            return a + b
        elif token == '-':
            return a - b
        elif token == '*':
            return a * b
        elif token == '/':
            # Perform integer division and truncate towards zero
            return int(a / b) if a * b >= 0 else -(-a // b)  # Handle truncation towards zero
        return -1  # Invalid token

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                result = self.operate(a, b, token)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]  # The result is the last element in the stack


# using lambda function
from typing import List
class Solution:
    def __init__(self):
        self.op = {
            '+' : lambda a,b: a + b,
            '-' : lambda a,b: a - b,
            '*' : lambda a,b:a * b,
            '/' : lambda a,b: int(a/b),
        }
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.op:
                b = stack.pop()
                a = stack.pop()
                result = self.op[token](a,b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]

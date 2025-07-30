class Solution:
    def isValid(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack or ch in '({[':
                stack.append(ch)
                continue
            if ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack
    


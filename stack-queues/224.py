# Tc = O(n)
# Sc = O(n)

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        number = 0
        result = 0
        sign = 1
        
        for i in range(n):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i] == '+':
                result += number * sign
                number = 0
                sign = 1
            elif s[i] == '-':
                result += number * sign
                number = 0
                sign = -1
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                number = 0
                sign = 1
            elif s[i] == ')':
                result += number * sign
                number = 0
                stack_sign = stack.pop()
                past_result = stack.pop()
                
                result *= stack_sign
                result += past_result
        
        result += number * sign
        return result


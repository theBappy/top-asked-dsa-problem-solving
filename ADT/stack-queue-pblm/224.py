class Solution:
    def calculate(self, s: str) -> int:
        st = []
        number = 0
        result = 0
        sign = 1
        for char in s:
            if char.isdigit():
                number = (number * 10) + int(char)
            elif char == '+':
                result += number * sign
                number = 0
                sign = 1
            elif char == '-':
                result += number * sign
                number = 0
                sign = -1
            elif char == '(':
                st.append(result)
                st.append(sign)
                result = 0
                number = 0
                sign = 1
            elif char == ')':
                result += number * sign
                number = 0
                stack_sign = st.pop()
                last_result = st.pop()
                result = result * stack_sign + last_result
        result += number * sign
        return result

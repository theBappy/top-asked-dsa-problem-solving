class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            if not st or ch in '({[':
                st.append(ch)
                continue

            if ch == ')':
                if st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif ch == '}':
                if st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif ch == ']':
                if st[-1] == '[':
                    st.pop()
                else:
                    return False

        return not st


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for ch in s:
            if ch == '(':
                st.append(')')
            elif ch == '{':
                st.append('}')
            elif ch == '[':
                st.append(']')
            elif not st or st[-1] != ch:
                return False
            else:
                st.pop()
        
        return not st
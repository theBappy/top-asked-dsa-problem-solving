# Meta, Microsoft, Zenefit's

# Tc = O(log(26)N) [N = is the column number] and space is same for the output string

    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            ch = chr(ord('A') + remainder)
            result.append(ch)
            columnNumber //= 26
        result.reverse()
        return ''.join(result)
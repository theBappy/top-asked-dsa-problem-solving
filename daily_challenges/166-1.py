class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        result = []
        if numerator * denominator < 0:
            result.append("-")
        absNumerator = abs(numerator)
        absDenominator = abs(denominator)

        integerDiv = absNumerator // absDenominator
        result.append(integerDiv)

        remainder = absNumerator % absDenominator
        if remainder == 0:
            return ''.join(result)
        result.append('.')

        mp = {}
        while remainder != 0:
            if remainder in mp:
                result.insert(mp[remainder], '(')
                result.append(')')
                break
            mp[remainder] = len(result)
            remainder *= 10
            digit = remainder // absDenominator
            result.append(str(digit))
            remainder %= absDenominator
        return ''.join(result)
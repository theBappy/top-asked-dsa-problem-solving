class Solution:
    def solve(self, num: int) -> int:
        divisors = 0
        total_sum = 0
        div = 1
        while div * div <= num:
            if num % div == 0:
                other = num // div
                if div == other:
                    divisors += 1
                    total_sum += div
                else:
                    divisors += 2
                    total_sum += (div + other)
            if divisors > 4:
                return 0
            div += 1
        return total_sum if divisors == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result += self.solve(num)
        return result

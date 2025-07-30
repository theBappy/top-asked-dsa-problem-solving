'''
Time Complexity: Amortized O(1) per call to next.
Space Complexity: O(N) in the worst case, where N is the number of calls to next.
'''
class Solution:
    def __init__(self):
        self.st = []
    def next(self, price: int) -> int:
        span = 1
        while self.st and self.st[-1][0] <= price:
            span += self.st.pop()[1]
        self.st.append((price, span))
        return span
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = int(1e9 + 7)
        pos_seats = [i for i, ch in enumerate(corridor) if ch == "S"]
        if len(pos_seats) % 2 != 0 or len(pos_seats) == 0:
            return 0
        result = 1
        prev = pos_seats[1]
        for i in range(2, len(pos_seats), 2):
            length = pos_seats[i] - prev
            result = (result * length) % mod
            prev = pos_seats[i] + 1
        return result

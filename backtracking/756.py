class Solution:
    def __init__(self):
        # Memoization dictionary
        # key -> boolean result
        self.dp = {}

    def solve(self, curr, mp, idx, above):
        # If only one block left, pyramid is complete
        if len(curr) == 1:
            return True

        # Create unique memo key
        key = f"{curr}_{idx}_{above}"
        if key in self.dp:
            return self.dp[key]

        # Finished building current row → move to above row
        if idx == len(curr) - 1:
            self.dp[key] = self.solve(above, mp, 0, "")
            return self.dp[key]

        # Take current adjacent pair
        pair = curr[idx:idx + 2]

        # If no allowed block can be placed above this pair
        if pair not in mp:
            self.dp[key] = False
            return False

        # Try all possible blocks above this pair
        for ch in mp[pair]:
            # DO
            if self.solve(curr, mp, idx + 1, above + ch):
                self.dp[key] = True
                return True

        # If none worked
        self.dp[key] = False
        return False
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for pattern in allowed:
            pair = pattern[:2]
            top = pattern[2]
            if pair not in mp:
                mp[pair] = []
            mp[pair].append(top)

        return self.solve(bottom, mp, 0, "")
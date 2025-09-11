class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch in "AEIOUaeiou"]
        vowels.sort()
        idx = 0
        res = list(s)

        for i, ch in enumerate(res):
            if ch in "AEIOUaeiou":
                res[i] = vowels[idx]
                idx += 1

        return "".join(res)


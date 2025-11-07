class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = 1
        i = 0
        result = []
        while i < len(target) and stream <= n:
            result.append("Push")
            if target[i] == stream:
                i += 1
            else:
                result.append("Pop")
            stream += 1
        return result
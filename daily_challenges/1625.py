class Solution:
    def rotate(self, s: str, b: int) -> str:
        s = s[::-1]
        s = s[:b][::-1] + s[b:][::-1]
        return s
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        smallestString = s
        visited = set()
        que = deque([s])
        visited.add(s)

        while que:
            curr = que.popleft()
            if curr < smallestString:
                smallestString = curr
            temp = list(curr)
            for i in range(1, len(temp), 2):
                temp[i] = str((int(temp[i]) + a) % 10)
            temp = "".join(temp)

            if temp not in visited:
                visited.add(temp)
                que.append(temp)

            rotated = self.rotate(curr, b)
            if rotated not in visited:
                visited.add(rotated)
                que.append(rotated)
        return smallestString

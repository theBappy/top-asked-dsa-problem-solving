from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bankset = set(bank)
        visited = set()
        que = deque([start])
        visited.add(start)
        
        level = 0
        
        while que:
            n = len(que)
            
            for _ in range(n):
                curr = que.popleft()
                
                if curr == end:
                    return level
                
                for ch in "ACGT":
                    for i in range(len(curr)):
                        neighbour = curr[:i] + ch + curr[i+1:]
                        
                        if neighbour not in visited and neighbour in bankset:
                            visited.add(neighbour)
                            que.append(neighbour)
            
            level += 1
        
        return -1
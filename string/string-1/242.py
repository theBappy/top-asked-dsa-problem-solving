    def generate(self, s: str) -> str:
        count = [0] * 26
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        new_s = []
        for i in range(26):
            if count[i] > 0:
                new_s.append(chr(i + ord('a')) * count[i])
        
        return ''.join(new_s)
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        
        for s in strs:
            new_s = self.generate(s)
            mp[new_s].append(s)
        
        return list(mp.values())
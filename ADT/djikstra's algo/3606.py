class Solution:
    def validateCode(self, code: str) -> bool:
        if not code:
            return False
        for ch in code:
            if not (ch.isalnum() or ch == '_'):
                return False
        return True
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        mp = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }
        temp = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in mp and self.validateCode(code[i]):
                temp.append((mp[businessLine[i]], code[i]))    

        temp.sort()
        result = [code for _, code in temp]

        return result
        
        
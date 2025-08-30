# Microsoft

# Odd count -> Alice win
# Even count -> Bob win
# [n/2] -> ceil value = odd => (n+1)/2
# [n/2] -> floor value = even => (m/2)
# Tc = O(1)
# Sc = O(1)

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
         return ((n + 1) // 2) * (m // 2) + (n // 2) * ((m + 1) // 2)
    
'''
JavaScript:
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var flowerGame = function (n, m) {
    let oddN = Math.floor((n + 1) / 2)
    let evenM = Math.floor(m / 2)
    let oddM = Math.floor((m + 1) / 2)
    let evenN = Math.floor(n / 2)

    return (oddN * evenM) + (oddM * evenN)
};

'''
# Amazon
# Bulb Switcher
# Perfect squares will be on
# Tc = O(1)
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
    
'''
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    return Math.floor(Math.sqrt(n))
};
'''
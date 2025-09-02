# Adobe, Microsoft

# Tc = O(number of digits in the given number)
class Solution:
    def __init__(self):
        self.sum = 0
    def get_count_digits(self, num):
        self.sum = 0
        count = 0
        while num:
            self.sum += num % 10
            num //= 10
            count += 1
        return count
    def add_digits(self, num):
        while self.get_count_digits(num) > 1:
            num = self.sum
        return self.sum
    
# 10^3 = 1000 = 9 * 111 + 1
# num = 9*k + Sd (Sd = sum of digits)
# Tc = O(1)

'''
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if(num === 0){
        return 0
    }
    if(num % 9 == 0){
        return 9
    }else{
        return num % 9
    }
};
'''


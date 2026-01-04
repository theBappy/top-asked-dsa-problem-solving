/**
 * @param {number[]} nums
 * @return {number}
 */
var sumFourDivisors = function (nums) {
    const solve = (num) => {
        let divisors = 0
        let sum = 0
        for (let div = 1; div * div <= num; div++) {
            if (num % div === 0) {
                let other = num / div
                if (div === other) {
                    divisors++
                    sum += div
                } else {
                    divisors += 2
                    sum += (div + other)
                }
            }
            if (divisors > 4) {
                return 0
            }
        }
        return divisors === 4 ? sum : 0
    }
    let result = 0
    for (const num of nums) {
        result += solve(num)
    }
    return result
};
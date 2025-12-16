/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function (prices) {
    let result = 1
    let count = 1
    for (let i = 1; i < prices.length; i++) {
        if (prices[i - 1] - prices[i] === 1) {
            count += 1
        } else {
            count = 1
        }
        result += count
    }
    return result
};
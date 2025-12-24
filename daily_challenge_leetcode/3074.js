/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function (apple, capacity) {
    capacity.sort((a, b) => b - a)
    let totalApple = apple.reduce((acc, val) => acc + val, 0)
    let count = 0
    let i = 0
    while (totalApple > 0) {
        totalApple -= capacity[i]
        count++
        i++
    }
    return count
};


/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function (apple, capacity) {
    let totalApples = apple.reduce((acc, val) => acc + val, 0)
    let freq = new Array(51).fill(0)
    for (const cap of capacity) {
        freq[cap]++
    }
    let count = 0
    for (let cap = 50; cap >= 1 && totalApples > 0; cap--) {
        while (freq[cap] > 0 && totalApples > 0) {
            totalApples -= cap
            freq[cap]--
            count++
        }
    }
    return count
};
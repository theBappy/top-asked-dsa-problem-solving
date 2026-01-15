/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} hBars
 * @param {number[]} vBars
 * @return {number}
 */
var maximizeSquareHoleArea = function (n, m, hBars, vBars) {
    hBars.sort((a, b) => a - b)
    vBars.sort((a, b) => a - b)

    let maxConsecutiveHBars = 1
    let maxConsecutiveVBars = 1

    let currConsecutiveHBars = 1
    for (let i = 1; i < hBars.length; i++) {
        if (hBars[i] - hBars[i - 1] === 1) {
            currConsecutiveHBars += 1
        } else {
            currConsecutiveHBars = 1
        }
        maxConsecutiveHBars = Math.max(maxConsecutiveHBars, currConsecutiveHBars)
    }
    let currConsecutiveVBars = 1
    for (let i = 1; i < vBars.length; i++) {
        if (vBars[i] - vBars[i - 1] === 1) {
            currConsecutiveVBars += 1
        } else {
            currConsecutiveVBars = 1
        }
        maxConsecutiveVBars = Math.max(maxConsecutiveVBars, currConsecutiveVBars)
    }
    const side = Math.min(maxConsecutiveHBars, maxConsecutiveVBars) + 1;
    return side * side;
};
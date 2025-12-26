/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function (customers) {
    const n = customers.length
    let minHour = 0
    let penalty = [...customers].filter(c => c === 'Y').length
    let minPenalty = penalty
    for (let i = 0; i < n; i++) {
        if (customers[i] === 'Y') {
            penalty--
        } else {
            penalty++
        }
        if (penalty < minPenalty) {
            minHour = i + 1
            minPenalty = penalty
        }
    }
    return minHour
};
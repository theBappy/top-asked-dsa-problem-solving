/**
 * @param {number[]} skill
 * @param {number[]} mana
 * @return {number}
 */
var minTime = function (skill, mana) {
    const n = skill.length
    const m = mana.length
    const finishTime = new Array(n).fill(0)
    for (let j = 0; j < m; j++) {
        finishTime[0] += mana[j] * skill[0]
        for (let i = 1; i < n; i++) {
            finishTime[i] = Math.max(finishTime[i], finishTime[i - 1]) + mana[j] * skill[i]
        }
        for (let i = n - 1; i > 0; i--) {
            finishTime[i - 1] = finishTime[i] - mana[j] * skill[i]
        }
    }
    return finishTime[n - 1]
};
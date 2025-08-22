/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(q) {
    const n = q.length
    const t = new Array(n).fill(-1)
    function solve(i){
        if(i >= n) return 0
        if(t[i] !== -1) return t[i]
        const taken = q[i][0] + solve(i + q[i][1] + 1)
        const notTaken = solve(i+1)
        t[i] = Math.max(taken, notTaken)
        return t[i]
    }
    return solve(0)

};
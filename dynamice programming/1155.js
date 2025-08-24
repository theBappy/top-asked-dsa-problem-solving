/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const m = 1e9 + 7
    const memo = new Map()

    function solve(n, target){
        if(target < 0) return 0
        if(n === 0) return target === 0 ? 1 :0
        const key = `${n},${target}`
        if(memo.has(key)) return memo.get(key)

        let ways = 0
        for(let face = 1; face <= k; face++){
            ways = (ways + solve(n-1, target - face)) % m
        }
        memo.set(key, ways)
        return ways
    }
    return solve(n, target)


};
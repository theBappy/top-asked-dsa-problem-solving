/**
 * @param {number[]} nums
 * @return {number}
 */
var numOfWays = function(nums) {
    const mod = 10**9 + 7

    const n = nums.length
    const PT = Array.from({length: n+1}, (_, i) => Array(i+1).fill(1))
    for(let i = 2; i <= n; i++){
        for(let j = 1; j < i; j++){
            PT[i][j] = (PT[i-1][j] + PT[i-1][j-1]) % mod
        }
    }
    const solve = (arr) => {
        const m = arr.length
        if(m < 3){
            return 1
        }
        const root = arr[0]
        const leftArray = arr.slice(1).filter(x => x < root)
        const rightArray = arr.slice(1).filter(x => x >= root)
        const leftWays = solve(leftArray) % mod
        const rightWays = solve(rightArray) % mod
        const waysToInterleave = PT[m-1][leftArray.length]
        return (leftWays * rightWays * waysToInterleave) % mod
    }
    return (solve(nums) -1) % mod
};
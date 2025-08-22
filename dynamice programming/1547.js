class Solution {
    constructor(){
        this.t = Array.from({length: 103}, () => Array(103).fill(-1))
    }
    solve(cuts, start, end){
        if (end - start < 2){
            return 0
        }
        if(this.t[start][end] !== -1){
            return this.t[start][end]
        }

        let result = Infinity
        for(let index = start + 1 ; index <= end - 1; index++){
            const cost = (cuts[end] - cuts[start]) + this.solve(cuts, start, index) + this.solve(cuts, index, end)
            result = Math.min(result, cost)
        }
        this.t[start][end] = result
        return result
    }

    minCosts(n, cuts){
        cuts.sort((a, b) => a - b)
        cuts = [0,...cuts, n]
        return this.solve(cuts, 0, cuts.length -1)
    }
}
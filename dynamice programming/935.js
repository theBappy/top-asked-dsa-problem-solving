class Solution {
    constructor(){
        this.M = 10**9 + 7
        this.adj = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        this.t = Array.from({length: 5001}, () => Array(10).fill(-1))
    }
    solve(n, cell){
        if(n === 0){
            return 1
        }
        if(this.t[n][cell] !== -1){
            return this.t[n][clearInterval]
        }

        let ans = 0
        for(const nextCell of this.adj[cell]){
            ans = (ans + this.solve(n-1, nextCell)) % this.M
        }
        this.t[n][cell] = ans
        return ans
    }
    knightDialer(n){
        let result = 0
        for(let cell = 0; cell <= 9; cell++){
            result = (result + this.solve(n-1, cell)) % this.M
        }
        return result
    }
}
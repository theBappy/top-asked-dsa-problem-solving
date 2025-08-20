class Solution {
    constructor() {
        this.mp = new Map();
    }

    solve(s1, s2) {
        if (s1 === s2) return true;
        if (s1.length !== s2.length) return false;

        const key = `${s1},${s2}`;
        if (this.mp.has(key)) {
            return this.mp.get(key);
        }

        let result = false;
        const n = s1.length;

        for (let i = 1; i < n; i++) {
            // Check swapped case
            const swapped = this.solve(s1.substring(0, i), s2.substring(n - i)) && 
                           this.solve(s1.substring(i), s2.substring(0, n - i));
            
            if (swapped) {
                result = true;
                break;
            }

            // Check non-swapped case
            const notSwapped = this.solve(s1.substring(0, i), s2.substring(0, i)) && 
                              this.solve(s1.substring(i), s2.substring(i));
            
            if (notSwapped) {
                result = true;
                break;
            }
        }

        this.mp.set(key, result);
        return result;
    }

    isScramble(s1, s2) {
        this.mp.clear();
        return this.solve(s1, s2);
    }
}

/*
How to use:
const sol = new Solution();
console.log(sol.isScramble("great", "rgeat")); // true
*/

class Solution {
    minWindow(s, t){
        const n = s.length
        if(t.length > n) return ""
        const mp = new Map()
        for(const ch of t){
            mp.set(ch, (mp.get(ch) || 0) + 1)
        }
        let requiredCount = t.length
        let i = 0, j = 0
        let minWindowSize = Infinity
        let start_i = 0
        while(j < n){
            const ch = s[j]
            if(mp.has(ch) && mp.get(ch) >0){
                requiredCount--
            }
            mp.set(ch, (mp.get(ch) || 0) -1)
            while(requiredCount === 0){
                const currWindowSize = j - i + 1
                if(minWindowSize > currWindowSize){
                    minWindowSize = currWindowSize
                    start_i = i         
                }
                mp.set(s[i], (mp.get(s[i]) || 0) + 1)
                if(mp.get(s[i]) > 0){
                    requiredCount++
                }
                i++
            }
            j++
        }
        return minWindowSize === Infinity ? "" : s.substring(start_i, start_i + minWindowSize)
    }
}
function trans(s){
    let temp = '#'
    for(let ch of s){
        temp += ch + '#'
    }
    return temp
}

function longestPalindrome(s){
    const t = transform(s)
    const n = t.length
    let l = 0, r = 0
    let center = 0, maxLen = 0
    const p = Array(n).fill(0)

    for(let i = 1; i < n; i++){
        let k;
        if(l > r){
            k=0
        }else{
            let j = l + (r-i)
            if(j - p[j] > l){
                p[i] = p[j]
                continue
            }else{
                k = r - i
            }
        }
        while(i - k >= 0 && i + k < n && t[i-k] === t[i+k]){
            k++
        }
        k--
        p[i] = k
        if(p[i] > maxLen){
            maxLen = p[i]
            center = i
        }
        if(i + k > r){
            l = i - k
            r = i + k
        }
    }
    const start = Math.floor((center-maxLen)/2)
    return s.slice(start, start + maxLen)
}
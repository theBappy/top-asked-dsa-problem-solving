var countSubstrings = function(s){
    let count = 0
    for(let i = 0; i < s.length ; i++){
        helper(s, i, i) // odd number length 
        helper(s, i, i+1) // even number length
    }
    return count

    function helper(s, low, high){
        while(low >= 0 && high < n && s[low] == s[high]){
            count += 1
            low -= 1
            high += 1
        }
    }
}


function longestPalindrome(s){
    const n = s.length;
    if(n === 0 ) return ''
    let start = 0, maxLen = 0
    // Traverse the input string
    for(let i = 0 ; i < n; i++){
        // THIS RUNS TWO TIMES 
        // for both odd and even length
        // palindromes. j = 0 means odd
        // and j = 1 means even length
        for(let j = 0; j <= 1; j++){
            let low = i
            let high = i + j
            while(low >= 0 && high < n && s[low] === s[high]){
                const currLen = high - low + 1
                if(currLen > maxLen){
                    maxLen = currLen
                    start = low
                }
                low--
                high++
            }
        }
    }
    return s.substring(start, start + maxLen)
}



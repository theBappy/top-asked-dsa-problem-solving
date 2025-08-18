// Approach-2
var minFlipsMonoIncr = function(s) {
    let countOfOnes = 0
    let flips = 0
    for(let ch of s){
        if(ch === '1'){
            countOfOnes++
        }else{
            flips = Math.min(countOfOnes, flips + 1)
        }
    }
    return flips
};
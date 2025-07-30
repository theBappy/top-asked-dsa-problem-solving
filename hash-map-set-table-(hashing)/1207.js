//  Tc = O(n)
//  Sc = O(n)
function uniqueOccurrences(arr) {
    // Frequency map to count occurrences of each element
    const freqMap = {};
    for (const num of arr) {
        freqMap[num] = (freqMap[num] || 0) + 1;
    }
    // Set to track unique frequencies
    const freqSet = new Set();
    for (const freq of Object.values(freqMap)) {
        if (freqSet.has(freq)) {
            return false;
        }
        freqSet.add(freq);
    }
    return true;
}


function uniqueOccurrences(arr){
    const vec = new Array(2001).fill(0)
    for(const x of arr){
        vec[x + 1000]++
    }
    vec.sort((a, b) => a - b)
    for(let i = 1; i < 2001; i++){
        if(vec[i] !== 0 && vec[i] === vec[i-1]){
            return false
        }
    }
    return true
}

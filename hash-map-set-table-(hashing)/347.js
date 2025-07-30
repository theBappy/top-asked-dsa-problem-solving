//  Tc = O(n * logk)
//  Sc = O(n)
var topKFrequentElement = function(nums, k){
    const freqMap = new Map()
    for(const num of nums){
        freqMap.set(num, (freqMap.get(num) || 0) +1)
    }
    const heap = []
    for(const [num, freq] of freqMap.entries()){
        if(heap.length < k){
            heap.push([freq, num])
            heap.sort((a, b) => a[0] - b[0])
        }else if(freq > heap[0][0]){
            heap[0] = [freq, num]
            heap.sort((a, b) => a[0] - b[0])
        }
    }
    return heap.map(item => item[1])
}
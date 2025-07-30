function increasing_monotonic_deque(arr, n){
    const q = []
    for(let i = 0; i < n; i++){
        while(q.length > 0 && q[q.length-1] > arr[i]){
            q.pop()
        }
        q.push(arr[i])
    }
    return q
}
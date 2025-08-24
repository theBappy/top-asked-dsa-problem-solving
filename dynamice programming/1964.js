/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    const n = obstacles.length
    const LIS = []
    const result = new Array(n).fill(0)
    const upperBound = (arr, x) => {
        let low = 0, high = arr.length
        while(low < high){
            const mid = Math.floor((low + high) / 2)
            if(arr[mid] <= x) low = mid+1
            else high = mid
        }
        return low
    }

    for(let i = 0; i < n; i++){
        const idx = upperBound(LIS, obstacles[i])
        if(idx === LIS.length){
            LIS.push(obstacles[i])
        }else{
            LIS[idx] = obstacles[i]
        }
        result[i] = idx + 1
    }
    return result
};
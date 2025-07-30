//  Tc = O(n)
//  Sc = O(n)
function numRabbits(answers){
    const countMap = {}
    for(const x of answers){
        countMap[x] = (countMap[x] || 0) + 1
    }
    let total = 0
    for(const [x, count] of Object.entries(countMap)){
        const groupSize = parseInt(x) + 1
        const groups = Math.ceil(count / groupSize)
        total += groups * groupSize
    }
    return total
}
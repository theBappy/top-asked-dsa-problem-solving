
var maxRunTime = function (n, batteries) {
    const possible = (mid) => {
        let target = BigInt(mid) * BigInt(n)
        let sum = 0n
        for (let b of batteries) {
            sum += BigInt(Math.min(b, mid))
            if (sum >= target) return true
        }
        return false
    }
    let total = batteries.reduce((a, b) => a + BigInt(b), 0n)
    let l = 0n
    let r = total / BigInt(n)
    let ans = 0n
    while (l <= r) {
        let mid = (l + r) / 2n
        if (possible(Number(mid))) {
            ans = mid
            l = mid + 1n
        } else {
            r = mid - 1n
        }
    }
    return Number(ans)
};
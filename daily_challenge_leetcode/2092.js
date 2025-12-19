/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function (n, meetings, firstPerson) {
    const timeMeetings = new Map()
    for (const meeting of meetings) {
        const [p1, p2, t] = meeting
        if (!timeMeetings.has(t)) {
            timeMeetings.set(t, [])
        }
        timeMeetings.get(t).push([p1, p2])
    }
    const knowsSecret = new Array(n).fill(false)
    knowsSecret[0] = true
    knowsSecret[firstPerson] = true
    for (const [t, meets] of [...timeMeetings.entries()].sort((a, b) => a[0] - b[0])) {
        const adj = new Map()
        const que = []
        const alreadyAdded = new Set()
        for (const [p1, p2] of meets) {
            if (!adj.has(p1)) adj.set(p1, [])
            if (!adj.has(p2)) adj.set(p2, [])
            adj.get(p1).push(p2)
            adj.get(p2).push(p1)
            if (knowsSecret[p1] && !alreadyAdded.has(p1)) {
                que.push(p1)
                alreadyAdded.add(p1)
            }
            if (knowsSecret[p2] && !alreadyAdded.has(p2)) {
                que.push(p2)
                alreadyAdded.add(p2)
            }
        }
        while (que.length > 0) {
            const person = que.shift()
            for (const nextPerson of adj.get(person) || []) {
                if (!knowsSecret[nextPerson]) {
                    knowsSecret[nextPerson] = true
                    que.push(nextPerson)
                }
            }
        }
    }
    const result = []
    for (let i = 0; i < n; i++) {
        if (knowsSecret[i]) {
            result.push(i)
        }
    }
    return result
};
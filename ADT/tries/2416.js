class TrieNode{
    constructor(){
        this.countPrefix = 0
        this.children = new Array(26).fill(null)
    }
}

class Solution{
    getTrieNode(){
        const newNode = new TrieNode()
        newNode.countPrefix = 0
        return newNode
    }

    insert(self, word){
        let crawl = root
        for(let ch of word){
            const idx = ch.charCodeAt(0) - 'a'.charCodeAt(0)
            if(crawl.children[idx] === null){
                crawl.children[idx] = this.getTrieNode()
            }
            crawl.children[idx].countPrefix += 1
            crawl = crawl.children[idx]
        }
    }

    getScore(self, word){
        let crawl = root
        let score = 0
        for(let ch of word){
            const idx = ch.charCodeAt(0) - 'a'.charCodeAt(0)
            score += crawl.children[idx].countPrefix
            crawl = crawl.children[idx]
        }
        return score
    }

    sumPrefixScores(words){
        const n = words.length
        const root = this.getTrieNode()

        for(let word of words){
            this.insert(word, root)
        }

        const result = new Array(n).fill(0)
        for(let i = 0; i < n; i++){
            result[i] = this.getScore(words[i], root)
        }
        return result
    }
}
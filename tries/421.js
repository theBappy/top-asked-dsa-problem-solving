class TrieNode {
    constructor() {
        this.left = null;
        this.right = null;
    }
}

class Solution {
    insert(root, num) {
        let pCrawl = root;
        for (let i = 31; i >= 0; i--) {
            const ith_bit = (num >> i) & 1;
            if (ith_bit === 0) {
                if (pCrawl.left === null) {
                    pCrawl.left = new TrieNode();
                }
                pCrawl = pCrawl.left;
            } else {
                if (pCrawl.right === null) {
                    pCrawl.right = new TrieNode();
                }
                pCrawl = pCrawl.right;
            }
        }
    }

    findMaxXor(root, num) {
        let maxXor = 0;
        let pCrawl = root;
        for (let i = 31; i >= 0; i--) {
            const ith_bit = (num >> i) & 1;
            if (ith_bit === 1) {
                if (pCrawl.left !== null) {
                    maxXor += (1 << i);
                    pCrawl = pCrawl.left;
                } else {
                    pCrawl = pCrawl.right;
                }
            } else {
                if (pCrawl.right !== null) {
                    maxXor += (1 << i);
                    pCrawl = pCrawl.right;
                } else {
                    pCrawl = pCrawl.left;
                }
            }
        }
        return maxXor;
    }

    findMaximumXor(nums) {
        const root = new TrieNode();
        for (const num of nums) {
            this.insert(root, num);
        }
        let maxResult = 0;
        for (const num of nums) {
            const temp = this.findMaxXor(root, num);
            maxResult = Math.max(maxResult, temp);
        }
        return maxResult;
    }
}
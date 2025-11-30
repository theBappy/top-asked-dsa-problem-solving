var ladderLength = function (beginWord, endWord, wordList) {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return 0;

    const queue = [[beginWord, 1]]; // store [word, steps]

    while (queue.length) {
        const [word, steps] = queue.shift();

        if (word === endWord) return steps;

        for (let i = 0; i < word.length; i++) {
            for (const ch of "abcdefghijklmnopqrstuvwxyz") {
                const next =
                    word.slice(0, i) + ch + word.slice(i + 1);

                if (wordSet.has(next)) {
                    wordSet.delete(next); // mark visited
                    queue.push([next, steps + 1]);
                }
            }
        }
    }
    return 0;
};

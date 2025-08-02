/**
 * @param {string} start
 * @param {string} end
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(start, end, bank) {
    // Create a Set from the bank array for efficient O(1) average time complexity lookups.
    const bankSet = new Set(bank);

    // Check if the end gene exists in the bank. If not, it's impossible to reach, so return -1.
    if (!bankSet.has(end)) {
        return -1;
    }

    // Initialize a queue for Breadth-First Search (BFS). Each element is an array [gene, mutations].
    // Start with the initial gene and 0 mutations.
    const queue = [[start, 0]]; 

    // Initialize a Set to keep track of visited genes to avoid cycles and redundant processing.
    const visited = new Set([start]);

    // Define the valid characters for a gene mutation.
    const geneChars = ['A', 'C', 'G', 'T'];

    // Start the BFS loop. Continue as long as there are genes in the queue to process.
    while (queue.length > 0) {
        // Dequeue the first element, which contains the current gene and its mutation count.
        const [currentGene, mutations] = queue.shift();

        // If the current gene is the target end gene, we've found the shortest path.
        // Return the number of mutations.
        if (currentGene === end) {
            return mutations;
        }

        // Iterate through each character position of the current gene.
        for (let i = 0; i < currentGene.length; i++) {
            // Store the original character at the current position.
            const originalChar = currentGene[i];

            // Iterate through the possible characters for a mutation ('A', 'C', 'G', 'T').
            for (const char of geneChars) {
                // Only consider a mutation if the new character is different from the original.
                if (char !== originalChar) {
                    // Convert the current gene string to an array to easily change a character.
                    const newGeneArray = currentGene.split('');

                    // Mutate the character at the current position.
                    newGeneArray[i] = char;

                    // Join the array back into a string to form the new gene.
                    const newGene = newGeneArray.join('');

                    // Check if the new gene is valid (in the bank) and has not been visited yet.
                    if (bankSet.has(newGene) && !visited.has(newGene)) {
                        // If it's a valid, unvisited mutation, add it to the visited set.
                        visited.add(newGene);

                        // Enqueue the new gene along with its incremented mutation count.
                        queue.push([newGene, mutations + 1]);
                    }
                }
            }
        }
    }

    // If the queue becomes empty and the end gene was never reached, it's impossible.
    // Return -1.
    return -1;
};
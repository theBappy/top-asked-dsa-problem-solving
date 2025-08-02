# Minimum Genetic Mutation
# BFS(level order traversal)
# N = length of gene in the bank
# L = length of the gene string
# O(n) might visit every gene in the bank
# neighbor generation O(L), string manipulation and set operations also O(L) [hash calculation and set lookup]
# Tc = O(N.L^2)
# Sc = O(N.L)
# Twitter

from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if end not in bank_set:
            return -1

        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            if current_gene == end:
                return mutations
            
            for i in range(len(current_gene)):
                original_char = current_gene[i]
                for char in "ACGT":
                    if char != original_char:
                        new_gene_list = list(current_gene)
                        new_gene_list[i] = char
                        new_gene = "".join(new_gene_list)
                        
                        if new_gene in bank_set and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, mutations + 1))
                            
        return -1
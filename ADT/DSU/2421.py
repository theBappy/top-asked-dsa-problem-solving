

'''
📌 Explanation of Approach

A good path has:

endpoints with the same value

all nodes along path having values ≤ endpoint value

This is solved using Union-Find in increasing order of node values.

Steps

Sort nodes by values.

Activate nodes in increasing order.

Union them only with active neighbors (ensures path values are ≤ current value).

Count how many nodes of the same value fall inside each DSU component.

For each component with k such nodes, add k choose 2 good paths:

𝑘(𝑘−1) / 2

'''


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        # DSU (Disjoint Set Union)
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # Union by rank
            px, py = find(x), find(y)
            if px == py:
                return

            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Group nodes by value using sorted map
        from collections import defaultdict

        val_to_nodes = defaultdict(list)
        for i, v in enumerate(vals):
            val_to_nodes[v].append(i)

        # Process values in sorted order
        result = n  # every node is a trivial good path
        is_active = [False] * n

        for value in sorted(val_to_nodes):
            nodes = val_to_nodes[value]

            # "Activate" nodes and union with active neighbors
            for u in nodes:
                for v in adj[u]:
                    if is_active[v]:
                        union(u, v)
                is_active[u] = True

            # Count nodes in each connected component
            comp = []
            for u in nodes:
                comp.append(find(u))

            comp.sort()

            # Count equal parents → combinations
            i = 0
            while i < len(comp):
                j = i
                count = 0
                while j < len(comp) and comp[j] == comp[i]:
                    j += 1
                    count += 1

                # number of good paths in this component
                result += count * (count - 1) // 2
                i = j

        return result

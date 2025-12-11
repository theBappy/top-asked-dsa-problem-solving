class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        # Parent array for DSU, 1-based indexing
        parent = [i for i in range(n + 1)]

        # Rank array: approximate tree height
        rank = [0] * (n + 1)

        # Find with path compression
        def find(x):
            # If x is not its own parent, recursively find root
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union by rank, returns False if union could not be made (i.e., cycle found)
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # Same root means a cycle exists
            if rootX == rootY:
                return False

            # Attach smaller rank tree under larger rank tree
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                # If equal rank, attach one to the other and increase rank
                parent[rootY] = rootX
                rank[rootX] += 1

            return True

        # Iterate through each edge
        for u, v in edges:
            # If union fails, it means this edge creates a cycle
            if not union(u, v):
                return [u, v]

        return []

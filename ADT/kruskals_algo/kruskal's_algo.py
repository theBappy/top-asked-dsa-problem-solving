

# Adj -> {{u1 ,v1, w1}, {u2, v2, w2}...}
# Sort vec basis on weight (ascending)
# Start processing from smallest edges

# Component detection by DSU
# If they are already connected, don't do anything, if not connected, connect the smalles edges
# By using DSU find parent, if parent are not same that means they are in different component so union them to make them locate in same components
# If belong to same components, somehow they connected so need to connect again


class Solution:
    def __init__(self):
        # parent[i] will store the parent of node i
        self.parent = []

        # rank[i] is used to keep tree depth small
        self.rank = []

    def find(self, x):
        """
        Finds the ultimate parent (root) of x
        Uses path compression for optimization
        """
        # If x is its own parent, it is the root
        if self.parent[x] == x:
            return x

        # Recursively find parent and compress path
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Unites the sets containing x and y
        Uses union by rank
        """
        # Find root parents
        x_parent = self.find(x)
        y_parent = self.find(y)

        # If already in same set, do nothing
        if x_parent == y_parent:
            return

        # Attach smaller rank tree under larger rank tree
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            # If ranks are equal, choose one and increase its rank
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    def kruskal(self, edges):
        """
        Applies Kruskal's algorithm on sorted edge list
        """
        mst_weight = 0

        # Traverse edges in increasing order of weight
        for u, v, wt in edges:
            # If u and v belong to different components
            if self.find(u) != self.find(v):
                # Include this edge in MST
                self.union(u, v)
                mst_weight += wt

        return mst_weight

    def spanningTree(self, V, adj):
        """
        Main function called by driver code
        """

        # Initialize DSU
        self.parent = [i for i in range(V)]
        self.rank = [0] * V

        edges = []

        # Convert adjacency list to edge list
        for u in range(V):
            for v, wt in adj[u]:
                # Avoid duplicate edges (undirected graph)
                if u < v:
                    edges.append((u, v, wt))

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Run Kruskal algorithm
        return self.kruskal(edges)

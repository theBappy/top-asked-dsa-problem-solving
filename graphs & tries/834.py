# Google
# Tc = O(N) [O(n)-> building the adjacency list, O(n)-> first dfs, O(n) -> the second DFS => O(n)+O(n)+O(n) = O(n)]
# Sc = O(N)
# result[child] = result[parent] - count[child] + (N - count[child])
'''
Sum of Distances in Tree: The Re-rooting Logic
The problem is to find the sum of distances from every node to all other nodes. Instead of doing a full search from each node (which would be slow), we can do it in two passes.

First Pass (Calculate for one node):

Pick an arbitrary node, let's say node 0, as the "root."

Do a Depth-First Search (DFS) from this root.

During this pass, we calculate two things:

result[0]: The total sum of distances for the root node (node 0) to all other nodes.

count[i]: The number of nodes in the subtree rooted at each node i. This includes node i itself.

Second Pass (Derive for all other nodes):

Now, we need to find the result for all other nodes.

The magic is in the parent-child relationship.

Let's say we have already calculated result[parent] (the sum for the parent) and we want to find result[child] (the sum for the child).

The Key Insight: When we move the "root" from the parent to the child, the distances to all other nodes change.

Nodes within the child's subtree: All these nodes are now one step closer to the new root (child). The number of these nodes is count[child].

Nodes outside the child's subtree: All these nodes are now one step farther away from the new root (child). The number of these nodes is N - count[child], where N is the total number of nodes.

The Simple Formula:

result[child] = result[parent] - count[child] + (N - count[child])

Why?

Start with result[parent].

Subtract count[child] because all the nodes in the child's subtree just got one step closer.

Add (N - count[child]) because all the other nodes in the tree just got one step farther.

This two-pass approach efficiently "re-roots" the tree from a single point to every other point, giving us the answer for all nodes in just two traversals.

'''

from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Calculates the sum of distances from each node to all other nodes in a tree.

        Args:
            n: The number of nodes in the tree.
            edges: A list of pairs representing the edges of the tree.

        Returns:
            A list where the i-th element is the sum of distances from node i
            to all other nodes.
        """
        self.N = n
        self.adj = defaultdict(list)
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        # `count` stores the number of nodes in the subtree rooted at each node.
        self.count = [0] * n
        
        # `root_result` will store the sum of distances for the root node (node 0).
        self.root_result = 0

        # First DFS pass: calculate subtree sizes and the initial sum for the root (node 0).
        self.dfsRoot(0, -1, 0)
        
        # `result` stores the final answer for each node.
        # We initialize the result for the root node using the value calculated in the first DFS.
        result = [0] * n
        result[0] = self.root_result

        # Second DFS pass: use the result from the root to calculate the results
        # for all other nodes based on a parent-child relationship.
        self.dfs(0, -1, result)

        return result

    def dfsRoot(self, curr_node: int, prev_node: int, curr_depth: int) -> None:
        """
        Performs a DFS to populate subtree sizes and calculate the initial sum for the root.
        
        This is a post-order traversal (logic is executed after visiting children).
        """
        self.root_result += curr_depth
        self.count[curr_node] = 1

        for child in self.adj[curr_node]:
            if child == prev_node:
                continue
            
            # Recurse on children.
            self.dfsRoot(child, curr_node, curr_depth + 1)
            
            # After the child's subtree is processed, update the current node's count.
            self.count[curr_node] += self.count[child]

    def dfs(self, parent_node: int, prev_node: int, result: list[int]) -> None:
        """
        Performs a DFS to update the sum of distances for all nodes.
        
        This is a pre-order traversal (logic is executed before visiting children).
        The formula is: result[child] = result[parent] - count[child] + (N - count[child]).
        """
        for child in self.adj[parent_node]:
            if child == prev_node:
                continue

            # `result[parent_node]` is the sum of distances for the parent.
            # To get `result[child]`, we adjust the parent's sum:
            # - `result[parent_node] - count[child]`: All `count[child]` nodes in the child's
            #   subtree are now one step closer to the new root (`child`).
            # - `+ (self.N - count[child])`: All `N - count[child]` nodes outside the
            #   child's subtree are now one step further away.
            result[child] = result[parent_node] - self.count[child] + (self.N - self.count[child])

            # Recurse on children to propagate the calculations.
            self.dfs(child, parent_node, result)


// DFS Approach
class Solution {
public: 
    unordered_map<Node*, Node*> mp;

    void dfs(Node* node, Node* clone_node) {
        for (Node* n : node->neighbors) {
            if (mp.find(n) == mp.end()) {
                Node* clone = new Node(n->val);
                mp[n] = clone;
                clone_node->neighbors.push_back(clone);
                dfs(n, clone);
            } else {
                clone_node->neighbors.push_back(mp[n]); 
            }
        }
    }

    Node* cloneGraph(Node* node) {
        if (!node)
            return NULL;

        // Clone the given node 
        Node* clone_node = new Node(node->val);

        // Store the mapping of the original node to the cloned node
        mp[node] = clone_node;

        // Now clone its neighbors and recursively their neighbors
        dfs(node, clone_node);
        
        // Return the cloned graph's root node
        return clone_node;
    }
};

// BFS Approach
class Solution {
public: 
    unordered_map<Node*, Node*> mp;

    void bfs(queue<Node*> q) {
        while (!q.empty()) {
            Node* node = q.front();
            q.pop();
            Node* clone_node = mp[node]; // Get the clone of the current node
            
            for (Node* n : node->neighbors) {
                if (mp.find(n) == mp.end()) {
                    Node* clone = new Node(n->val);
                    mp[n] = clone; // Map the original node to the clone
                    clone_node->neighbors.push_back(clone); // Add the clone to the neighbors
                    q.push(n); // Push the original neighbor to the queue for processing
                } else {
                    clone_node->neighbors.push_back(mp[n]); // Add the existing clone to the neighbors
                }
            }
        }
    }

    Node* cloneGraph(Node* node) {
        if (!node)
            return NULL;

        // Clone the given node 
        Node* clone_node = new Node(node->val);

        // Store the mapping of the original node to the cloned node
        mp[node] = clone_node;

        // BFS approach
        queue<Node*> q;
        q.push(node);
        bfs(q);
        
        // Return the cloned graph's root node
        return clone_node;
    }
};

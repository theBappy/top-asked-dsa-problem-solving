class Solution {
    isBipartite(graph) {
        const n = graph.length;
        const color = new Array(n).fill(-1);
        
        for (let node = 0; node < n; node++) {
            if (color[node] === -1) {
                const stack = [[node, 1]];
                
                while (stack.length > 0) {
                    const [curr_node, curr_color] = stack.pop();
                    
                    if (color[curr_node] === -1) {
                        color[curr_node] = curr_color;
                    } else {
                        if (color[curr_node] !== curr_color) {
                            return false;
                        }
                    }
                    
                    for (const n of graph[curr_node]) {
                        if (color[n] === -1) {
                            stack.push([n, 1 - curr_color]);
                        } else if (color[n] === curr_color) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
// Find Building Where Alice and Bob Can Meet

// Approach (Using Segment Tree Range Maximum Query + Binary Search)
// T.C : O(n + q*(logn)^2)
// S.C : O(n)

/* Binary search:   O(log n)
Segment query: × O(log n)
--------------------------------
Each query = O(log n × log n)
            = O((log n)²) */

/*
Build tree:         O(n)
Answer queries:     O(q · (log n)²)
-------------------------------------
Total = O(n + q · (log n)²)

*/

/*

🔥 Summary Table
Component	Complexity
Build segment tree	O(n)
Query (1 query)	O((log n)²)
All queries	O(q·(log n)²)
Space	O(n + q)
*/

class Solution
{
public:
    void buildSegmentTree(int i, int l, int r, int segmentTree[],
                          vector<int> &heights)
    {
        if (l == r)
        {
            segmentTree[i] = l;
            return; // FIX #1
        }

        int mid = l + (r - l) / 2;
        buildSegmentTree(2 * i + 1, l, mid, segmentTree, heights);
        buildSegmentTree(2 * i + 2, mid + 1, r, segmentTree, heights);

        int leftIndex = segmentTree[2 * i + 1];
        int rightIndex = segmentTree[2 * i + 2];

        segmentTree[i] =
            (heights[leftIndex] >= heights[rightIndex]) ? leftIndex : rightIndex;
    }

    int *constructST(vector<int> &heights, int n)
    {
        int *segmentTree = new int[4 * n](); // FIX #2
        buildSegmentTree(0, 0, n - 1, segmentTree, heights);
        return segmentTree;
    }

    int queryST(int start, int end, int i, int l, int r,
                int segmentTree[], vector<int> &heights)
    {
        if (l > end || r < start)
            return -1;
        if (l >= start && r <= end)
            return segmentTree[i];

        int mid = l + (r - l) / 2;

        int leftIndex = queryST(start, end, 2 * i + 1, l, mid, segmentTree, heights);
        int rightIndex = queryST(start, end, 2 * i + 2, mid + 1, r, segmentTree, heights);

        if (leftIndex == -1)
            return rightIndex;
        if (rightIndex == -1)
            return leftIndex;

        return (heights[leftIndex] >= heights[rightIndex]) ? leftIndex : rightIndex;
    }

    int RMIQ(int segmentTree[], vector<int> &heights, int n, int start, int end)
    {
        return queryST(start, end, 0, 0, n - 1, segmentTree, heights);
    }

    vector<int> leftmostBuildingQueries(vector<int> &heights,
                                        vector<vector<int>> &queries)
    {
        int n = heights.size();
        int *segmentTree = constructST(heights, n);

        vector<int> result;
        for (auto &query : queries)
        {
            int min_idx = min(query[0], query[1]);
            int max_idx = max(query[0], query[1]);

            if (min_idx == max_idx || heights[max_idx] > heights[min_idx])
            {
                result.push_back(max_idx);
                continue;
            }

            int l = max_idx + 1;
            int r = n - 1;
            int result_idx = INT_MAX;

            while (l <= r)
            {
                int mid = l + (r - l) / 2;
                int idx = RMIQ(segmentTree, heights, n, l, mid);

                if (idx != -1 && heights[idx] > max(heights[min_idx], heights[max_idx]))
                { // FIX #3
                    result_idx = min(result_idx, idx);
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }

            result.push_back(result_idx == INT_MAX ? -1 : result_idx);
        }

        return result;
    }
};

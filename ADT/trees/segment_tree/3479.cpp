//Tc = O(n.logn)
// Sc = O(4 *n)

class Solution {
public:
    void buildST(int i, int l, int r, vector<int>& baskets,
                 vector<int>& segmentTree) {
        if (l == r) {
            segmentTree[i] = baskets[l];
            return;
        }
        int mid = l + (r - l) / 2;
        buildST(2 * i + 1, l, mid, baskets, segmentTree);
        buildST(2 * i + 2, mid + 1, r, baskets, segmentTree);
        segmentTree[i] = max(segmentTree[2 * i + 1], segmentTree[2 * i + 2]);
    }
    bool query(int i, int l, int r, vector<int>& segmentTree, int fruit) {
        if (segmentTree[i] < fruit) {
            return false;
        }
        if (l == r) {
            segmentTree[i] = -1;
            return true;
        }
        int mid = l + (r - l) / 2;
        bool placed = false;
        if (segmentTree[2 * i + 1] >= fruit) {
            placed = query(2 * i + 1, l, mid, segmentTree, fruit);
        } else {
            placed = query(2 * i + 2, mid + 1, r, segmentTree, fruit);
        }
        segmentTree[i] = max(segmentTree[2 * i + 1], segmentTree[2 * i + 2]);
        return placed;
    }
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        vector<int> segmentTree(4 * n);
        buildST(0, 0, n - 1, baskets, segmentTree);

        int unplaced = 0;
        for (int& fruit : fruits) {
            if (!query(0, 0, n - 1, segmentTree, fruit)) {
                unplaced++;
            }
        }
        return unplaced;
    }
};
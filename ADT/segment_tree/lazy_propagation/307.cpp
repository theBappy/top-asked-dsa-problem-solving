// Tc = O(n)
// Sc = O(n)
// Will give T.L.E
class NumArray {
public:
    vector<int> num;
    int n;
    NumArray(vector<int>& nums) {
        num = nums;
        n = nums.size();
    }

    void update(int index, int val) { num[index] = val; }

    int sumRange(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += num[i];
        }
        return sum;
    }
};


// Now option solve with Segment Tree Method
//T.C : Constructor: O(n), where n is length of nums array
//  Update, sumRange: O(logN)
//S.C : O(n)
class NumArray {
public:
    int n;
    vector<int> st;
    void buildST(int i, int l, int r, vector<int>& nums) {
        if (l == r) {
            st[i] = nums[l];
            return;
        }
        int mid = l + (r - l) / 2;
        buildST(2 * i + 1, l, mid, nums);
        buildST(2 * i + 2, mid + 1, r, nums);
        st[i] = st[2 * i + 1] + st[2 * i + 2];
    }
    void updateST(int index, int val, int i, int l, int r) {
        if (l == r) {
            st[i] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (index <= mid) {
            updateST(index, val, 2 * i + 1, l, mid);
        } else {
            updateST(index, val, 2 * i + 2, mid + 1, r);
        }
        st[i] = st[2 * i + 1] + st[2 * i + 2];
    }
    int query(int start, int end, int i, int l, int r) {
        if (l > end || r < start) {
            return 0;
        }
        if (l >= start && r <= end) {
            return st[i];
        }
        int mid = l + (r - l) / 2;
        return query(start, end, 2 * i + 1, l, mid) +
               query(start, end, 2 * i + 2, mid + 1, r);
    }
    NumArray(vector<int>& nums) {
        n = nums.size();
        st.resize(4 * n);
        buildST(0, 0, n - 1, nums);
    }
    void update(int index, int val) { updateST(index, val, 0, 0, n - 1); }

    int sumRange(int left, int right) {
        return query(left, right, 0, 0, n - 1);
    }
};




